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
StreetType: Enumeration = Enumeration(
    name="StreetType",
    literals={
            EnumerationLiteral(name="Street"),
			EnumerationLiteral(name="Road")
    }
)

# Classes
rental_Address = Class(name="rental::Address")
rental_RentalAgency = Class(name="rental::RentalAgency")
rental_RentalObject = Class(name="rental::RentalObject")
rental_Customer = Class(name="rental::Customer")
rental_Rental = Class(name="rental::Rental")
rental_License = Class(name="rental::License")
rental_Car = Class(name="rental::Car")
RentalObject = Class(name="RentalObject")
rental_Device = Class(name="rental::Device")

# rental_Address class attributes and methods
rental_Address_streetType: Property = Property(name="streetType", type=StringType)
rental_Address_number: Property = Property(name="number", type=IntegerType)
rental_Address_zipCode: Property = Property(name="zipCode", type=StringType)
rental_Address_city: Property = Property(name="city", type=StringType)
rental_Address_streetName: Property = Property(name="streetName", type=StringType)
rental_Address.attributes={rental_Address_city, rental_Address_zipCode, rental_Address_number, rental_Address_streetType, rental_Address_streetName}

# rental_RentalAgency class attributes and methods
rental_RentalAgency_name: Property = Property(name="name", type=StringType)
rental_RentalAgency_m_isAvailable: Method = Method(name="isAvailable", parameters={Parameter(name='rentedObject'), Parameter(name='from'), Parameter(name='to')}, type=BooleanType)
rental_RentalAgency_m_book: Method = Method(name="book", parameters={Parameter(name='customer'), Parameter(name='rentedObject'), Parameter(name='to'), Parameter(name='from')}, type=StringType)
rental_RentalAgency.attributes={rental_RentalAgency_name}
rental_RentalAgency.methods={rental_RentalAgency_m_book, rental_RentalAgency_m_isAvailable}

# rental_RentalObject class attributes and methods
rental_RentalObject_ID: Property = Property(name="ID", type=StringType)
rental_RentalObject_name: Property = Property(name="name", type=StringType)
rental_RentalObject_available: Property = Property(name="available", type=BooleanType)
rental_RentalObject_m_rent: Method = Method(name="rent", parameters={Parameter(name='customer')}, type=StringType)
rental_RentalObject.attributes={rental_RentalObject_ID, rental_RentalObject_available, rental_RentalObject_name}
rental_RentalObject.methods={rental_RentalObject_m_rent}

# rental_Customer class attributes and methods
rental_Customer_firstName: Property = Property(name="firstName", type=StringType)
rental_Customer_lastName: Property = Property(name="lastName", type=StringType)
rental_Customer_m_getDisplayName: Method = Method(name="getDisplayName", parameters={}, type=StringType)
rental_Customer_m_addLicense: Method = Method(name="addLicense", parameters={Parameter(name='license')})
rental_Customer.attributes={rental_Customer_firstName, rental_Customer_lastName}
rental_Customer.methods={rental_Customer_m_getDisplayName, rental_Customer_m_addLicense}

# rental_Rental class attributes and methods
rental_Rental_startDate: Property = Property(name="startDate", type=DateType)
rental_Rental_endDate: Property = Property(name="endDate", type=DateType)
rental_Rental_m_nbDaysBooked: Method = Method(name="nbDaysBooked", parameters={}, type=IntegerType)
rental_Rental.attributes={rental_Rental_startDate, rental_Rental_endDate}
rental_Rental.methods={rental_Rental_m_nbDaysBooked}

# rental_License class attributes and methods
rental_License_number: Property = Property(name="number", type=IntegerType)
rental_License_validityDate: Property = Property(name="validityDate", type=DateType)
rental_License_m_isValid: Method = Method(name="isValid", parameters={}, type=BooleanType)
rental_License.attributes={rental_License_number, rental_License_validityDate}
rental_License.methods={rental_License_m_isValid}

# rental_Car class attributes and methods
rental_Car_licensePlate: Property = Property(name="licensePlate", type=StringType)
rental_Car.attributes={rental_Car_licensePlate}

# RentalObject class attributes and methods

# rental_Device class attributes and methods
rental_Device_serialNumber: Property = Property(name="serialNumber", type=StringType)
rental_Device_width: Property = Property(name="width", type=IntegerType)
rental_Device_height: Property = Property(name="height", type=IntegerType)
rental_Device_length: Property = Property(name="length", type=IntegerType)
rental_Device.attributes={rental_Device_serialNumber, rental_Device_length, rental_Device_height, rental_Device_width}

# Relationships
address0: BinaryAssociation = BinaryAssociation(
    name="address0",
    ends={
        Property(name="rental_Address", type=rental_RentalAgency, multiplicity=Multiplicity(1, 1)),
        Property(name="rental_RentalAgency", type=rental_Address, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parentAgency10: BinaryAssociation = BinaryAssociation(
    name="parentAgency10",
    ends={
        Property(name="RentalAgency11", type=rental_RentalObject, multiplicity=Multiplicity(1, 1)),
        Property(name="objectsToRent", type=rental_RentalAgency, multiplicity=Multiplicity(1, 1))
    }
)
objectsToRent1: BinaryAssociation = BinaryAssociation(
    name="objectsToRent1",
    ends={
        Property(name="RentalObject", type=rental_RentalAgency, multiplicity=Multiplicity(1, 1)),
        Property(name="parentAgency", type=rental_RentalObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
customers2: BinaryAssociation = BinaryAssociation(
    name="customers2",
    ends={
        Property(name="Customer", type=rental_RentalAgency, multiplicity=Multiplicity(1, 1)),
        Property(name="parentAgency3", type=rental_Customer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rentals4: BinaryAssociation = BinaryAssociation(
    name="rentals4",
    ends={
        Property(name="Rental", type=rental_RentalAgency, multiplicity=Multiplicity(1, 1)),
        Property(name="parentAgency5", type=rental_Rental, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
address6: BinaryAssociation = BinaryAssociation(
    name="address6",
    ends={
        Property(name="rental_Address7", type=rental_Customer, multiplicity=Multiplicity(1, 1)),
        Property(name="rental_Customer", type=rental_Address, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
licenses8: BinaryAssociation = BinaryAssociation(
    name="licenses8",
    ends={
        Property(name="License", type=rental_Customer, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=rental_License, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentAgency9: BinaryAssociation = BinaryAssociation(
    name="parentAgency9",
    ends={
        Property(name="RentalAgency", type=rental_Customer, multiplicity=Multiplicity(1, 1)),
        Property(name="customers", type=rental_RentalAgency, multiplicity=Multiplicity(1, 1))
    }
)
owner12: BinaryAssociation = BinaryAssociation(
    name="owner12",
    ends={
        Property(name="Customer13", type=rental_License, multiplicity=Multiplicity(1, 1)),
        Property(name="licenses", type=rental_Customer, multiplicity=Multiplicity(0, 1))
    }
)
EReference014: BinaryAssociation = BinaryAssociation(
    name="EReference014",
    ends={
        Property(name="rental_Customer15", type=rental_License, multiplicity=Multiplicity(1, 1)),
        Property(name="rental_License", type=rental_Customer, multiplicity=Multiplicity(0, 1))
    }
)
customer16: BinaryAssociation = BinaryAssociation(
    name="customer16",
    ends={
        Property(name="rental_Customer17", type=rental_Rental, multiplicity=Multiplicity(1, 1)),
        Property(name="rental_Rental", type=rental_Customer, multiplicity=Multiplicity(1, 1))
    }
)
rentedObject18: BinaryAssociation = BinaryAssociation(
    name="rentedObject18",
    ends={
        Property(name="rental_RentalObject", type=rental_Rental, multiplicity=Multiplicity(1, 1)),
        Property(name="rental_Rental19", type=rental_RentalObject, multiplicity=Multiplicity(1, 1))
    }
)
parentAgency20: BinaryAssociation = BinaryAssociation(
    name="parentAgency20",
    ends={
        Property(name="RentalAgency21", type=rental_Rental, multiplicity=Multiplicity(1, 1)),
        Property(name="rentals", type=rental_RentalAgency, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_rental_Car_RentalObject = Generalization(general=RentalObject, specific=rental_Car)
gen_rental_Device_RentalObject = Generalization(general=RentalObject, specific=rental_Device)

# Domain Model
domain_model = DomainModel(
    name="rental",
    types={rental_Address, rental_RentalAgency, rental_RentalObject, rental_Customer, rental_Rental, rental_License, rental_Car, RentalObject, rental_Device, StreetType},
    associations={address0, parentAgency10, objectsToRent1, customers2, rentals4, address6, licenses8, parentAgency9, owner12, EReference014, customer16, rentedObject18, parentAgency20},
    generalizations={gen_rental_Car_RentalObject, gen_rental_Device_RentalObject},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)