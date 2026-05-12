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
customer = Class(name="customer")
payement = Class(name="payement")
ticket = Class(name="ticket")
admin = Class(name="admin")
flights = Class(name="flights")
cash = Class(name="cash")
credit_card = Class(name="credit_card")

# customer class attributes and methods
customer_name: Property = Property(name="name", type=StringType)
customer_address: Property = Property(name="address", type=StringType)
customer_age: Property = Property(name="age", type=IntegerType)
customer_source: Property = Property(name="source", type=StringType)
customer.attributes={customer_source, customer_name, customer_age, customer_address}

# payement class attributes and methods
payement_customer_info: Property = Property(name="customer_info", type=StringType)
payement_pay_amt: Property = Property(name="pay_amt", type=IntegerType)
payement_transc_id: Property = Property(name="transc_id", type=IntegerType)
payement_pay_date: Property = Property(name="pay_date", type=IntegerType)
payement_paymethod: Property = Property(name="paymethod", type=StringType)
payement.attributes={payement_pay_amt, payement_transc_id, payement_pay_date, payement_customer_info, payement_paymethod}

# ticket class attributes and methods
ticket_tiketno_: Property = Property(name="tiketno_", type=IntegerType)
ticket_source: Property = Property(name="source", type=StringType)
ticket_dest: Property = Property(name="dest", type=StringType)
ticket_custid: Property = Property(name="custid", type=IntegerType)
ticket_attribute: Property = Property(name="attribute", type=StringType)
ticket.attributes={ticket_source, ticket_tiketno_, ticket_custid, ticket_dest, ticket_attribute}

# admin class attributes and methods
admin_username: Property = Property(name="username", type=StringType)
admin_pwd: Property = Property(name="pwd", type=StringType)
admin_name_of_flight: Property = Property(name="name_of_flight", type=StringType)
admin_type: Property = Property(name="type", type=StringType)
admin_seats: Property = Property(name="seats", type=IntegerType)
admin_cost: Property = Property(name="cost", type=IntegerType)
admin.attributes={admin_username, admin_type, admin_name_of_flight, admin_pwd, admin_seats, admin_cost}

# flights class attributes and methods
flights_number: Property = Property(name="number", type=IntegerType)
flights_time: Property = Property(name="time", type=IntegerType)
flights_name: Property = Property(name="name", type=StringType)
flights_dest: Property = Property(name="dest", type=StringType)
flights_depart: Property = Property(name="depart", type=StringType)
flights.attributes={flights_time, flights_number, flights_dest, flights_depart, flights_name}

# cash class attributes and methods

# credit_card class attributes and methods

# Relationships
payement_customer: BinaryAssociation = BinaryAssociation(
    name="payement_customer",
    ends={
        Property(name="customer0", type=customer, multiplicity=Multiplicity(0, 1)),
        Property(name="payement1", type=payement, multiplicity=Multiplicity(1, 1))
    }
)
customer_ticket: BinaryAssociation = BinaryAssociation(
    name="customer_ticket",
    ends={
        Property(name="ticket2", type=ticket, multiplicity=Multiplicity(0, 1)),
        Property(name="customer3", type=customer, multiplicity=Multiplicity(1, 9999))
    }
)
customer_admin: BinaryAssociation = BinaryAssociation(
    name="customer_admin",
    ends={
        Property(name="admin4", type=admin, multiplicity=Multiplicity(1, 1)),
        Property(name="customer5", type=customer, multiplicity=Multiplicity(1, 9999))
    }
)
customer_flights: BinaryAssociation = BinaryAssociation(
    name="customer_flights",
    ends={
        Property(name="flights6", type=flights, multiplicity=Multiplicity(1, 1)),
        Property(name="customer7", type=customer, multiplicity=Multiplicity(1, 9999))
    }
)
admin_flights: BinaryAssociation = BinaryAssociation(
    name="admin_flights",
    ends={
        Property(name="flights8", type=flights, multiplicity=Multiplicity(1, 9999)),
        Property(name="admin9", type=admin, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="ab615982_2fe5_40a5_bb7e_abdfb8feeeba",
    types={customer, payement, ticket, admin, flights, cash, credit_card},
    associations={payement_customer, customer_ticket, customer_admin, customer_flights, admin_flights},
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