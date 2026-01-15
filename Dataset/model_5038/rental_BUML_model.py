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
rental_RentalObject = Class(name="rental::RentalObject")
rental_Rental = Class(name="rental::Rental")
rental_Customer = Class(name="rental::Customer")
rental_Address = Class(name="rental::Address")
rental_License = Class(name="rental::License")
rental_RentalAgency = Class(name="rental::RentalAgency")

# rental_RentalObject class attributes and methods
rental_RentalObject_ID: Property = Property(name="ID", type=StringType)
rental_RentalObject_name: Property = Property(name="name", type=StringType)
rental_RentalObject_picture: Property = Property(name="picture", type=StringType)
rental_RentalObject_m_rent: Method = Method(name="rent", parameters={Parameter(name='customer')}, type=StringType)
rental_RentalObject_m_isAvailable: Method = Method(name="isAvailable", parameters={}, type=BooleanType)
rental_RentalObject.attributes={rental_RentalObject_picture, rental_RentalObject_name, rental_RentalObject_ID}
rental_RentalObject.methods={rental_RentalObject_m_rent, rental_RentalObject_m_isAvailable}

# rental_Rental class attributes and methods
rental_Rental_startDate: Property = Property(name="startDate", type=DateType)
rental_Rental_endDate: Property = Property(name="endDate", type=DateType)
rental_Rental_m_nbDaysBooked: Method = Method(name="nbDaysBooked", parameters={}, type=IntegerType)
rental_Rental_m_end: Method = Method(name="end", parameters={}, type=IntegerType)
rental_Rental_m_start: Method = Method(name="start", parameters={}, type=IntegerType)
rental_Rental_m_nbDaysRented: Method = Method(name="nbDaysRented", parameters={}, type=IntegerType)
rental_Rental.attributes={rental_Rental_endDate, rental_Rental_startDate}
rental_Rental.methods={rental_Rental_m_nbDaysRented, rental_Rental_m_start, rental_Rental_m_end, rental_Rental_m_nbDaysBooked}

# rental_Customer class attributes and methods
rental_Customer_firstName: Property = Property(name="firstName", type=StringType)
rental_Customer_lastName: Property = Property(name="lastName", type=StringType)
rental_Customer_m_getDisplayName: Method = Method(name="getDisplayName", parameters={}, type=StringType)
rental_Customer.attributes={rental_Customer_firstName, rental_Customer_lastName}
rental_Customer.methods={rental_Customer_m_getDisplayName}

# rental_Address class attributes and methods
rental_Address_streetType: Property = Property(name="streetType", type=StringType)
rental_Address_number: Property = Property(name="number", type=IntegerType)
rental_Address_zipCode: Property = Property(name="zipCode", type=StringType)
rental_Address_city: Property = Property(name="city", type=StringType)
rental_Address_streetName: Property = Property(name="streetName", type=StringType)
rental_Address.attributes={rental_Address_streetType, rental_Address_city, rental_Address_zipCode, rental_Address_number, rental_Address_streetName}

# rental_License class attributes and methods
rental_License_number: Property = Property(name="number", type=IntegerType)
rental_License_validityDate: Property = Property(name="validityDate", type=DateType)
rental_License.attributes={rental_License_validityDate, rental_License_number}

# rental_RentalAgency class attributes and methods
rental_RentalAgency_name: Property = Property(name="name", type=StringType)
rental_RentalAgency_m_book: Method = Method(name="book", parameters={Parameter(name='from'), Parameter(name='to'), Parameter(name='customer'), Parameter(name='rentedObject')}, type=StringType)
rental_RentalAgency_m_addCustomer: Method = Method(name="addCustomer", parameters={Parameter(name='customer')})
rental_RentalAgency_m_addObject: Method = Method(name="addObject", parameters={Parameter(name='object')})
rental_RentalAgency.attributes={rental_RentalAgency_name}
rental_RentalAgency.methods={rental_RentalAgency_m_addObject, rental_RentalAgency_m_addCustomer, rental_RentalAgency_m_book}

# Relationships
address3: BinaryAssociation = BinaryAssociation(
    name="address3",
    ends={
        Property(name="rental_Address4", type=rental_RentalAgency, multiplicity=Multiplicity(1, 1)),
        Property(name="rental_RentalAgency", type=rental_Address, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
objectsToRent5: BinaryAssociation = BinaryAssociation(
    name="objectsToRent5",
    ends={
        Property(name="RentalObject", type=rental_RentalAgency, multiplicity=Multiplicity(1, 1)),
        Property(name="parentAgency", type=rental_RentalObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
customers6: BinaryAssociation = BinaryAssociation(
    name="customers6",
    ends={
        Property(name="Customer", type=rental_RentalAgency, multiplicity=Multiplicity(1, 1)),
        Property(name="parentAgency7", type=rental_Customer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rentals8: BinaryAssociation = BinaryAssociation(
    name="rentals8",
    ends={
        Property(name="rental_Rental", type=rental_RentalAgency, multiplicity=Multiplicity(1, 1)),
        Property(name="rental_RentalAgency9", type=rental_Rental, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
address0: BinaryAssociation = BinaryAssociation(
    name="address0",
    ends={
        Property(name="rental_Address", type=rental_Customer, multiplicity=Multiplicity(1, 1)),
        Property(name="rental_Customer", type=rental_Address, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
licenses1: BinaryAssociation = BinaryAssociation(
    name="licenses1",
    ends={
        Property(name="License", type=rental_Customer, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=rental_License, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentAgency2: BinaryAssociation = BinaryAssociation(
    name="parentAgency2",
    ends={
        Property(name="RentalAgency", type=rental_Customer, multiplicity=Multiplicity(1, 1)),
        Property(name="customers", type=rental_RentalAgency, multiplicity=Multiplicity(1, 1))
    }
)
parentAgency19: BinaryAssociation = BinaryAssociation(
    name="parentAgency19",
    ends={
        Property(name="rental_RentalAgency21", type=rental_Rental, multiplicity=Multiplicity(1, 1)),
        Property(name="rental_Rental20", type=rental_RentalAgency, multiplicity=Multiplicity(1, 1))
    }
)
parentAgency10: BinaryAssociation = BinaryAssociation(
    name="parentAgency10",
    ends={
        Property(name="RentalAgency11", type=rental_RentalObject, multiplicity=Multiplicity(1, 1)),
        Property(name="objectsToRent", type=rental_RentalAgency, multiplicity=Multiplicity(1, 1))
    }
)
owner12: BinaryAssociation = BinaryAssociation(
    name="owner12",
    ends={
        Property(name="Customer13", type=rental_License, multiplicity=Multiplicity(1, 1)),
        Property(name="licenses", type=rental_Customer, multiplicity=Multiplicity(0, 1))
    }
)
customer14: BinaryAssociation = BinaryAssociation(
    name="customer14",
    ends={
        Property(name="rental_Customer16", type=rental_Rental, multiplicity=Multiplicity(1, 1)),
        Property(name="rental_Rental15", type=rental_Customer, multiplicity=Multiplicity(1, 1))
    }
)
rentedObject17: BinaryAssociation = BinaryAssociation(
    name="rentedObject17",
    ends={
        Property(name="rental_RentalObject", type=rental_Rental, multiplicity=Multiplicity(1, 1)),
        Property(name="rental_Rental18", type=rental_RentalObject, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="rental",
    types={rental_RentalObject, rental_Rental, rental_Customer, rental_Address, rental_License, rental_RentalAgency, StreetType},
    associations={address3, objectsToRent5, customers6, rentals8, address0, licenses1, parentAgency2, parentAgency19, parentAgency10, owner12, customer14, rentedObject17},
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