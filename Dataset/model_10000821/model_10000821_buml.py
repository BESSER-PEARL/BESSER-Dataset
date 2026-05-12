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
CardType: Enumeration = Enumeration(
    name="CardType",
    literals={
            
    }
)

Size: Enumeration = Enumeration(
    name="Size",
    literals={
            
    }
)

# Classes
Management_Manager = Class(name="Management_Manager")
Management_DirectorTest = Class(name="Management_DirectorTest")
Management_ManagerTest = Class(name="Management_ManagerTest")
Staff_Employee = Class(name="Staff_Employee", is_abstract=True)
techStaff_DatabaseAdmin = Class(name="techStaff_DatabaseAdmin")
techStaff_Developer = Class(name="techStaff_Developer")
techStaff_DatabaseAdminTest = Class(name="techStaff_DatabaseAdminTest")
techStaff_DeveloperTest = Class(name="techStaff_DeveloperTest")
Class_ = Class(name="Class")
Product = Class(name="Product")
TransportationProduct = Class(name="TransportationProduct")
Flight = Class(name="Flight")
Travel = Class(name="Travel")
Taxi = Class(name="Taxi")
Fashion = Class(name="Fashion")
Ticket = Class(name="Ticket")
GiftCard = Class(name="GiftCard")
Management_Director = Class(name="Management_Director")

# Management_Manager class attributes and methods
Management_Manager_deptName: Property = Property(name="deptName", type=StringType)
Management_Manager.attributes={Management_Manager_deptName}

# Management_DirectorTest class attributes and methods

# Management_ManagerTest class attributes and methods

# Staff_Employee class attributes and methods
Staff_Employee_name: Property = Property(name="name", type=StringType)
Staff_Employee_nationalInsurance: Property = Property(name="nationalInsurance", type=StringType)
Staff_Employee_salary: Property = Property(name="salary", type=FloatType)
Staff_Employee.attributes={Staff_Employee_name, Staff_Employee_nationalInsurance, Staff_Employee_salary}

# techStaff_DatabaseAdmin class attributes and methods

# techStaff_Developer class attributes and methods

# techStaff_DatabaseAdminTest class attributes and methods

# techStaff_DeveloperTest class attributes and methods

# Class class attributes and methods

# Product class attributes and methods
Product_title: Property = Property(name="title", type=StringType)
Product_creationDate: Property = Property(name="creationDate", type=DateType)
Product_price: Property = Property(name="price", type=FloatType)
Product_supportDiscount: Property = Property(name="supportDiscount", type=BooleanType)
Product.attributes={Product_title, Product_supportDiscount, Product_price, Product_creationDate}

# TransportationProduct class attributes and methods
TransportationProduct_destination: Property = Property(name="destination", type=StringType)
TransportationProduct_source: Property = Property(name="source", type=StringType)
TransportationProduct_distance: Property = Property(name="distance", type=FloatType)
TransportationProduct.attributes={TransportationProduct_distance, TransportationProduct_source, TransportationProduct_destination}

# Flight class attributes and methods
Flight_hasConnection: Property = Property(name="hasConnection", type=BooleanType)
Flight.attributes={Flight_hasConnection}

# Travel class attributes and methods

# Taxi class attributes and methods
Taxi_isVip: Property = Property(name="isVip", type=BooleanType)
Taxi.attributes={Taxi_isVip}

# Fashion class attributes and methods
Fashion_size: Property = Property(name="size", type=Size)
Fashion_category: Property = Property(name="category", type=StringType)
Fashion_increaseBy: Property = Property(name="increaseBy", type=IntegerType)
Fashion.attributes={Fashion_category, Fashion_size, Fashion_increaseBy}

# Ticket class attributes and methods
Ticket_eventCity: Property = Property(name="eventCity", type=StringType)
Ticket_eventCountry: Property = Property(name="eventCountry", type=StringType)
Ticket_isLastMinute: Property = Property(name="isLastMinute", type=BooleanType)
Ticket.attributes={Ticket_eventCity, Ticket_isLastMinute, Ticket_eventCountry}

# GiftCard class attributes and methods
GiftCard_cardType: Property = Property(name="cardType", type=CardType)
GiftCard_isPresent: Property = Property(name="isPresent", type=BooleanType)
GiftCard.attributes={GiftCard_cardType, GiftCard_isPresent}

# Management_Director class attributes and methods
Management_Director_budget: Property = Property(name="budget", type=FloatType)
Management_Director.attributes={Management_Director_budget}

# Relationships
databaseAdmin_DatabaseAdminTest_DatabaseAdmin_2: BinaryAssociation = BinaryAssociation(
    name="databaseAdmin_DatabaseAdminTest_DatabaseAdmin_2",
    ends={
        Property(name="databaseadmintest0", type=techStaff_DatabaseAdminTest, multiplicity=Multiplicity(0, 1)),
        Property(name="databaseAdmin1", type=techStaff_DatabaseAdmin, multiplicity=Multiplicity(0, 1))
    }
)
developer_DeveloperTest_Developer_3: BinaryAssociation = BinaryAssociation(
    name="developer_DeveloperTest_Developer_3",
    ends={
        Property(name="developertest2", type=techStaff_DeveloperTest, multiplicity=Multiplicity(0, 1)),
        Property(name="developer3", type=techStaff_Developer, multiplicity=Multiplicity(0, 1))
    }
)
manager_ManagerTest_Manager_0: BinaryAssociation = BinaryAssociation(
    name="manager_ManagerTest_Manager_0",
    ends={
        Property(name="managertest4", type=Management_ManagerTest, multiplicity=Multiplicity(0, 1)),
        Property(name="manager5", type=Management_Manager, multiplicity=Multiplicity(0, 1))
    }
)
director_DirectorTest_Director_1: BinaryAssociation = BinaryAssociation(
    name="director_DirectorTest_Director_1",
    ends={
        Property(name="directortest6", type=Management_DirectorTest, multiplicity=Multiplicity(0, 1)),
        Property(name="director7", type=Management_Director, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_64d73a9a_d42d_4090_b6ce_9496e444dcf0",
    types={Management_Manager, Management_DirectorTest, Management_ManagerTest, Staff_Employee, techStaff_DatabaseAdmin, techStaff_Developer, techStaff_DatabaseAdminTest, techStaff_DeveloperTest, Class_, Product, TransportationProduct, Flight, Travel, Taxi, Fashion, Ticket, GiftCard, Management_Director, CardType, Size},
    associations={databaseAdmin_DatabaseAdminTest_DatabaseAdmin_2, developer_DeveloperTest_Developer_3, manager_ManagerTest_Manager_0, director_DirectorTest_Director_1},
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