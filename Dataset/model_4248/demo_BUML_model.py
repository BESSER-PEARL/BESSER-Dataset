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
demo_model_Address = Class(name="demo::model::Address")
demo_model_Company = Class(name="demo::model::Company")
demo_model_Employee = Class(name="demo::model::Employee")

# demo_model_Address class attributes and methods
demo_model_Address_city: Property = Property(name="city", type=StringType)
demo_model_Address_street: Property = Property(name="street", type=StringType)
demo_model_Address_zipcode: Property = Property(name="zipcode", type=IntegerType)
demo_model_Address_state: Property = Property(name="state", type=StringType)
demo_model_Address_country: Property = Property(name="country", type=StringType)
demo_model_Address.attributes={demo_model_Address_state, demo_model_Address_zipcode, demo_model_Address_street, demo_model_Address_country, demo_model_Address_city}

# demo_model_Company class attributes and methods
demo_model_Company_name: Property = Property(name="name", type=StringType)
demo_model_Company.attributes={demo_model_Company_name}

# demo_model_Employee class attributes and methods
demo_model_Employee_firstname: Property = Property(name="firstname", type=StringType)
demo_model_Employee_lastname: Property = Property(name="lastname", type=StringType)
demo_model_Employee_position: Property = Property(name="position", type=StringType)
demo_model_Employee_email: Property = Property(name="email", type=StringType)
demo_model_Employee_phone: Property = Property(name="phone", type=StringType)
demo_model_Employee_birthday: Property = Property(name="birthday", type=DateType)
demo_model_Employee.attributes={demo_model_Employee_firstname, demo_model_Employee_position, demo_model_Employee_lastname, demo_model_Employee_phone, demo_model_Employee_email, demo_model_Employee_birthday}

# Relationships
employees0: BinaryAssociation = BinaryAssociation(
    name="employees0",
    ends={
        Property(name="Employee", type=demo_model_Company, multiplicity=Multiplicity(1, 1)),
        Property(name="company", type=demo_model_Employee, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
company1: BinaryAssociation = BinaryAssociation(
    name="company1",
    ends={
        Property(name="Company", type=demo_model_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="employees", type=demo_model_Company, multiplicity=Multiplicity(0, 1))
    }
)
address2: BinaryAssociation = BinaryAssociation(
    name="address2",
    ends={
        Property(name="demo_model_Address", type=demo_model_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="demo_model_Employee", type=demo_model_Address, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="demo_model",
    types={demo_model_Address, demo_model_Company, demo_model_Employee},
    associations={employees0, company1, address2},
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