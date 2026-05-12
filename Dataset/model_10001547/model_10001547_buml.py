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
Restaurant = Class(name="Restaurant")
Table = Class(name="Table")
Payment = Class(name="Payment")
Booking = Class(name="Booking")
Table_booking_time = Class(name="Table_booking_time")
Customer = Class(name="Customer")

# Restaurant class attributes and methods
Restaurant_booking: Property = Property(name="booking", type=IntegerType)
Restaurant_time: Property = Property(name="time", type=IntegerType)
Restaurant.attributes={Restaurant_time, Restaurant_booking}

# Table class attributes and methods
Table_table_number: Property = Property(name="table_number", type=IntegerType)
Table_total_person: Property = Property(name="total_person", type=IntegerType)
Table.attributes={Table_table_number, Table_total_person}

# Payment class attributes and methods
Payment_pay_hotel: Property = Property(name="pay_hotel", type=IntegerType)
Payment_paytm: Property = Property(name="paytm", type=IntegerType)
Payment_credit_card: Property = Property(name="credit_card", type=IntegerType)
Payment_debit_card: Property = Property(name="debit_card", type=IntegerType)
Payment.attributes={Payment_pay_hotel, Payment_debit_card, Payment_credit_card, Payment_paytm}

# Booking class attributes and methods
Booking_customer_name: Property = Property(name="customer_name", type=StringType)
Booking_arrival_time: Property = Property(name="arrival_time", type=IntegerType)
Booking_table_number: Property = Property(name="table_number", type=IntegerType)
Booking.attributes={Booking_arrival_time, Booking_table_number, Booking_customer_name}

# Table_booking_time class attributes and methods
Table_booking_time_start_time: Property = Property(name="start_time", type=IntegerType)
Table_booking_time_end_time: Property = Property(name="end_time", type=IntegerType)
Table_booking_time.attributes={Table_booking_time_start_time, Table_booking_time_end_time}

# Customer class attributes and methods
Customer_cust_id: Property = Property(name="cust_id", type=IntegerType)
Customer_name: Property = Property(name="name", type=StringType)
Customer_mobile: Property = Property(name="mobile", type=IntegerType)
Customer_email: Property = Property(name="email", type=StringType)
Customer_Address: Property = Property(name="Address", type=StringType)
Customer.attributes={Customer_cust_id, Customer_mobile, Customer_email, Customer_name, Customer_Address}

# Relationships
Table_booking_time_Payment: BinaryAssociation = BinaryAssociation(
    name="Table_booking_time_Payment",
    ends={
        Property(name="payment6", type=Payment, multiplicity=Multiplicity(0, 1)),
        Property(name="table_booking_time7", type=Table_booking_time, multiplicity=Multiplicity(0, 1))
    }
)
Restaurant_Table: BinaryAssociation = BinaryAssociation(
    name="Restaurant_Table",
    ends={
        Property(name="table8", type=Table, multiplicity=Multiplicity(0, 1)),
        Property(name="restaurant9", type=Restaurant, multiplicity=Multiplicity(0, 1))
    }
)
Table_Booking: BinaryAssociation = BinaryAssociation(
    name="Table_Booking",
    ends={
        Property(name="booking0", type=Booking, multiplicity=Multiplicity(0, 1)),
        Property(name="table1", type=Table, multiplicity=Multiplicity(0, 1))
    }
)
Restaurant_Customer: BinaryAssociation = BinaryAssociation(
    name="Restaurant_Customer",
    ends={
        Property(name="customer2", type=Customer, multiplicity=Multiplicity(0, 1)),
        Property(name="restaurant3", type=Restaurant, multiplicity=Multiplicity(0, 1))
    }
)
Booking_Table_booking_time: BinaryAssociation = BinaryAssociation(
    name="Booking_Table_booking_time",
    ends={
        Property(name="table_booking_time4", type=Table_booking_time, multiplicity=Multiplicity(0, 1)),
        Property(name="booking5", type=Booking, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_EwdYsPCoEee2hpeWh535Sw",
    types={Restaurant, Table, Payment, Booking, Table_booking_time, Customer},
    associations={Table_booking_time_Payment, Restaurant_Table, Table_Booking, Restaurant_Customer, Booking_Table_booking_time},
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