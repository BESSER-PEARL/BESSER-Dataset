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
Award: Enumeration = Enumeration(
    name="Award",
    literals={
            EnumerationLiteral(name="Unspecified"),
			EnumerationLiteral(name="GrandChampion"),
			EnumerationLiteral(name="ReserveChampion"),
			EnumerationLiteral(name="BlueRibbon"),
			EnumerationLiteral(name="RedRibbon"),
			EnumerationLiteral(name="WhiteRibbon"),
			EnumerationLiteral(name="PinkRibbon")
    }
)

# Classes
fair_Exhibit = Class(name="fair::Exhibit")
fair_Fair = Class(name="fair::Fair")
fair_YouthClub = Class(name="fair::YouthClub")
fair_Division = Class(name="fair::Division")
fair_Premises = Class(name="fair::Premises")
fair_Person = Class(name="fair::Person")
fair_Animal = Class(name="fair::Animal")
fair_Lot = Class(name="fair::Lot")
fair_Department = Class(name="fair::Department")
fair_Class = Class(name="fair::Class")
fair_YoungPerson = Class(name="fair::YoungPerson")
Person = Class(name="Person")

# fair_Exhibit class attributes and methods
fair_Exhibit_name: Property = Property(name="name", type=StringType)
fair_Exhibit_number: Property = Property(name="number", type=IntegerType)
fair_Exhibit_comments: Property = Property(name="comments", type=StringType)
fair_Exhibit_salesOrder: Property = Property(name="salesOrder", type=IntegerType)
fair_Exhibit_inAuction: Property = Property(name="inAuction", type=BooleanType)
fair_Exhibit_award: Property = Property(name="award", type=StringType)
fair_Exhibit.attributes={fair_Exhibit_number, fair_Exhibit_inAuction, fair_Exhibit_name, fair_Exhibit_award, fair_Exhibit_comments, fair_Exhibit_salesOrder}

# fair_Fair class attributes and methods
fair_Fair_name: Property = Property(name="name", type=StringType)
fair_Fair_comments: Property = Property(name="comments", type=StringType)
fair_Fair_m_exhibits: Method = Method(name="exhibits", parameters={}, type=StringType)
fair_Fair.attributes={fair_Fair_name, fair_Fair_comments}
fair_Fair.methods={fair_Fair_m_exhibits}

# fair_YouthClub class attributes and methods
fair_YouthClub_name: Property = Property(name="name", type=StringType)
fair_YouthClub_comments: Property = Property(name="comments", type=StringType)
fair_YouthClub.attributes={fair_YouthClub_comments, fair_YouthClub_name}

# fair_Division class attributes and methods
fair_Division_name: Property = Property(name="name", type=StringType)
fair_Division_comments: Property = Property(name="comments", type=StringType)
fair_Division_description: Property = Property(name="description", type=StringType)
fair_Division.attributes={fair_Division_description, fair_Division_name, fair_Division_comments}

# fair_Premises class attributes and methods

# fair_Person class attributes and methods
fair_Person_zipCode: Property = Property(name="zipCode", type=StringType)
fair_Person_name: Property = Property(name="name", type=StringType)
fair_Person_comments: Property = Property(name="comments", type=StringType)
fair_Person_firstName: Property = Property(name="firstName", type=StringType)
fair_Person_lastName: Property = Property(name="lastName", type=StringType)
fair_Person_phone: Property = Property(name="phone", type=StringType)
fair_Person_street: Property = Property(name="street", type=StringType)
fair_Person_city: Property = Property(name="city", type=StringType)
fair_Person_state: Property = Property(name="state", type=StringType)
fair_Person_pin: Property = Property(name="pin", type=StringType)
fair_Person_salesOrder: Property = Property(name="salesOrder", type=IntegerType)
fair_Person_exhibitorNumber: Property = Property(name="exhibitorNumber", type=IntegerType)
fair_Person_email: Property = Property(name="email", type=StringType)
fair_Person.attributes={fair_Person_street, fair_Person_phone, fair_Person_lastName, fair_Person_firstName, fair_Person_salesOrder, fair_Person_pin, fair_Person_comments, fair_Person_city, fair_Person_state, fair_Person_name, fair_Person_zipCode, fair_Person_email, fair_Person_exhibitorNumber}

# fair_Animal class attributes and methods

# fair_Lot class attributes and methods
fair_Lot_name: Property = Property(name="name", type=StringType)
fair_Lot_comments: Property = Property(name="comments", type=StringType)
fair_Lot_description: Property = Property(name="description", type=StringType)
fair_Lot.attributes={fair_Lot_comments, fair_Lot_description, fair_Lot_name}

# fair_Department class attributes and methods
fair_Department_name: Property = Property(name="name", type=StringType)
fair_Department_comments: Property = Property(name="comments", type=StringType)
fair_Department_description: Property = Property(name="description", type=StringType)
fair_Department.attributes={fair_Department_comments, fair_Department_description, fair_Department_name}

# fair_Class class attributes and methods
fair_Class_name: Property = Property(name="name", type=StringType)
fair_Class_comments: Property = Property(name="comments", type=StringType)
fair_Class_description: Property = Property(name="description", type=StringType)
fair_Class.attributes={fair_Class_name, fair_Class_comments, fair_Class_description}

# fair_YoungPerson class attributes and methods

# Person class attributes and methods

# Relationships
youthClubs0: BinaryAssociation = BinaryAssociation(
    name="youthClubs0",
    ends={
        Property(name="fair_YouthClub", type=fair_Fair, multiplicity=Multiplicity(1, 1)),
        Property(name="fair_Fair", type=fair_YouthClub, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
divisions1: BinaryAssociation = BinaryAssociation(
    name="divisions1",
    ends={
        Property(name="fair_Division", type=fair_Fair, multiplicity=Multiplicity(1, 1)),
        Property(name="fair_Fair2", type=fair_Division, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
premises3: BinaryAssociation = BinaryAssociation(
    name="premises3",
    ends={
        Property(name="fair_Premises", type=fair_Fair, multiplicity=Multiplicity(1, 1)),
        Property(name="fair_Fair4", type=fair_Premises, multiplicity=Multiplicity(1, 1))
    }
)
people5: BinaryAssociation = BinaryAssociation(
    name="people5",
    ends={
        Property(name="fair_Person", type=fair_Fair, multiplicity=Multiplicity(1, 1)),
        Property(name="fair_Fair6", type=fair_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superintendents17: BinaryAssociation = BinaryAssociation(
    name="superintendents17",
    ends={
        Property(name="fair_Person18", type=fair_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="fair_Department", type=fair_Person, multiplicity=Multiplicity(0, 9999))
    }
)
division19: BinaryAssociation = BinaryAssociation(
    name="division19",
    ends={
        Property(name="Division", type=fair_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="departments", type=fair_Division, multiplicity=Multiplicity(1, 1))
    }
)
animal7: BinaryAssociation = BinaryAssociation(
    name="animal7",
    ends={
        Property(name="fair_Animal", type=fair_Exhibit, multiplicity=Multiplicity(1, 1)),
        Property(name="fair_Exhibit", type=fair_Animal, multiplicity=Multiplicity(1, 1))
    }
)
exhibitor8: BinaryAssociation = BinaryAssociation(
    name="exhibitor8",
    ends={
        Property(name="fair_Person10", type=fair_Exhibit, multiplicity=Multiplicity(1, 1)),
        Property(name="fair_Exhibit9", type=fair_Person, multiplicity=Multiplicity(1, 1))
    }
)
lot11: BinaryAssociation = BinaryAssociation(
    name="lot11",
    ends={
        Property(name="Lot", type=fair_Exhibit, multiplicity=Multiplicity(1, 1)),
        Property(name="exhibits", type=fair_Lot, multiplicity=Multiplicity(1, 1))
    }
)
contacts12: BinaryAssociation = BinaryAssociation(
    name="contacts12",
    ends={
        Property(name="fair_Person14", type=fair_YouthClub, multiplicity=Multiplicity(1, 1)),
        Property(name="fair_YouthClub13", type=fair_Person, multiplicity=Multiplicity(1, 9999))
    }
)
departments15: BinaryAssociation = BinaryAssociation(
    name="departments15",
    ends={
        Property(name="Department", type=fair_Division, multiplicity=Multiplicity(1, 1)),
        Property(name="division", type=fair_Department, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
classes16: BinaryAssociation = BinaryAssociation(
    name="classes16",
    ends={
        Property(name="Class", type=fair_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="department", type=fair_Class, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
lots20: BinaryAssociation = BinaryAssociation(
    name="lots20",
    ends={
        Property(name="Lot21", type=fair_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="class", type=fair_Lot, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
judges22: BinaryAssociation = BinaryAssociation(
    name="judges22",
    ends={
        Property(name="fair_Person23", type=fair_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="fair_Class", type=fair_Person, multiplicity=Multiplicity(1, 9999))
    }
)
department24: BinaryAssociation = BinaryAssociation(
    name="department24",
    ends={
        Property(name="Department25", type=fair_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="classes", type=fair_Department, multiplicity=Multiplicity(1, 1))
    }
)
exhibits26: BinaryAssociation = BinaryAssociation(
    name="exhibits26",
    ends={
        Property(name="Exhibit", type=fair_Lot, multiplicity=Multiplicity(1, 1)),
        Property(name="lot", type=fair_Exhibit, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
class27: BinaryAssociation = BinaryAssociation(
    name="class27",
    ends={
        Property(name="Class28", type=fair_Lot, multiplicity=Multiplicity(1, 1)),
        Property(name="lots", type=fair_Class, multiplicity=Multiplicity(1, 1))
    }
)
parents29: BinaryAssociation = BinaryAssociation(
    name="parents29",
    ends={
        Property(name="fair_Person30", type=fair_YoungPerson, multiplicity=Multiplicity(1, 1)),
        Property(name="fair_YoungPerson", type=fair_Person, multiplicity=Multiplicity(1, 9999))
    }
)
club31: BinaryAssociation = BinaryAssociation(
    name="club31",
    ends={
        Property(name="fair_YouthClub33", type=fair_YoungPerson, multiplicity=Multiplicity(1, 1)),
        Property(name="fair_YoungPerson32", type=fair_YouthClub, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_fair_YoungPerson_Person = Generalization(general=Person, specific=fair_YoungPerson)

# Domain Model
domain_model = DomainModel(
    name="fair",
    types={fair_Exhibit, fair_Fair, fair_YouthClub, fair_Division, fair_Premises, fair_Person, fair_Animal, fair_Lot, fair_Department, fair_Class, fair_YoungPerson, Person, Award},
    associations={youthClubs0, divisions1, premises3, people5, superintendents17, division19, animal7, exhibitor8, lot11, contacts12, departments15, classes16, lots20, judges22, department24, exhibits26, class27, parents29, club31},
    generalizations={gen_fair_YoungPerson_Person},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)