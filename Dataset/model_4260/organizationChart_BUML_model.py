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
StructureType: Enumeration = Enumeration(
    name="StructureType",
    literals={
            EnumerationLiteral(name="team"),
			EnumerationLiteral(name="service"),
			EnumerationLiteral(name="department"),
			EnumerationLiteral(name="businessUnit"),
			EnumerationLiteral(name="division")
    }
)

# Classes
organizationchart_Employee = Class(name="organizationchart::Employee")
organizationchart_OrganizationalStructure = Class(name="organizationchart::OrganizationalStructure")
organizationchart_Location = Class(name="organizationchart::Location")
organizationchart_Function = Class(name="organizationchart::Function")
organizationchart_Organization = Class(name="organizationchart::Organization")

# organizationchart_Employee class attributes and methods
organizationchart_Employee_firstname: Property = Property(name="firstname", type=StringType)
organizationchart_Employee_lastname: Property = Property(name="lastname", type=StringType)
organizationchart_Employee_title: Property = Property(name="title", type=StringType)
organizationchart_Employee_trigraph: Property = Property(name="trigraph", type=StringType)
organizationchart_Employee.attributes={organizationchart_Employee_title, organizationchart_Employee_firstname, organizationchart_Employee_lastname, organizationchart_Employee_trigraph}

# organizationchart_OrganizationalStructure class attributes and methods
organizationchart_OrganizationalStructure_name: Property = Property(name="name", type=StringType)
organizationchart_OrganizationalStructure_type: Property = Property(name="type", type=StringType)
organizationchart_OrganizationalStructure.attributes={organizationchart_OrganizationalStructure_name, organizationchart_OrganizationalStructure_type}

# organizationchart_Location class attributes and methods
organizationchart_Location_name: Property = Property(name="name", type=StringType)
organizationchart_Location.attributes={organizationchart_Location_name}

# organizationchart_Function class attributes and methods
organizationchart_Function_name: Property = Property(name="name", type=StringType)
organizationchart_Function.attributes={organizationchart_Function_name}

# organizationchart_Organization class attributes and methods
organizationchart_Organization_name: Property = Property(name="name", type=StringType)
organizationchart_Organization.attributes={organizationchart_Organization_name}

# Relationships
subStructures20: BinaryAssociation = BinaryAssociation(
    name="subStructures20",
    ends={
        Property(name="organizationchart_OrganizationalStructure19", type=organizationchart_OrganizationalStructure, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="organizationchart_OrganizationalStructure21", type=organizationchart_OrganizationalStructure, multiplicity=Multiplicity(1, 1))
    }
)
owns22: BinaryAssociation = BinaryAssociation(
    name="owns22",
    ends={
        Property(name="organizationchart_Function", type=organizationchart_OrganizationalStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="organizationchart_OrganizationalStructure23", type=organizationchart_Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
manager24: BinaryAssociation = BinaryAssociation(
    name="manager24",
    ends={
        Property(name="Employee25", type=organizationchart_OrganizationalStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="leads", type=organizationchart_Employee, multiplicity=Multiplicity(0, 1))
    }
)
employees26: BinaryAssociation = BinaryAssociation(
    name="employees26",
    ends={
        Property(name="Employee27", type=organizationchart_Location, multiplicity=Multiplicity(1, 1)),
        Property(name="location", type=organizationchart_Employee, multiplicity=Multiplicity(0, 9999))
    }
)
manages1: BinaryAssociation = BinaryAssociation(
    name="manages1",
    ends={
        Property(name="Employee", type=organizationchart_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="manager", type=organizationchart_Employee, multiplicity=Multiplicity(0, 9999))
    }
)
belongsTo2: BinaryAssociation = BinaryAssociation(
    name="belongsTo2",
    ends={
        Property(name="OrganizationalStructure", type=organizationchart_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="employees", type=organizationchart_OrganizationalStructure, multiplicity=Multiplicity(0, 1))
    }
)
location3: BinaryAssociation = BinaryAssociation(
    name="location3",
    ends={
        Property(name="Location", type=organizationchart_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="employees4", type=organizationchart_Location, multiplicity=Multiplicity(0, 1))
    }
)
manager6: BinaryAssociation = BinaryAssociation(
    name="manager6",
    ends={
        Property(name="Employee7", type=organizationchart_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="manages", type=organizationchart_Employee, multiplicity=Multiplicity(0, 1))
    }
)
performs8: BinaryAssociation = BinaryAssociation(
    name="performs8",
    ends={
        Property(name="Function", type=organizationchart_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="isPerformedBy", type=organizationchart_Function, multiplicity=Multiplicity(0, 9999))
    }
)
leads9: BinaryAssociation = BinaryAssociation(
    name="leads9",
    ends={
        Property(name="OrganizationalStructure11", type=organizationchart_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="manager10", type=organizationchart_OrganizationalStructure, multiplicity=Multiplicity(0, 9999))
    }
)
employees12: BinaryAssociation = BinaryAssociation(
    name="employees12",
    ends={
        Property(name="organizationchart_Employee", type=organizationchart_Organization, multiplicity=Multiplicity(1, 1)),
        Property(name="organizationchart_Organization", type=organizationchart_Employee, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
structures13: BinaryAssociation = BinaryAssociation(
    name="structures13",
    ends={
        Property(name="organizationchart_OrganizationalStructure", type=organizationchart_Organization, multiplicity=Multiplicity(1, 1)),
        Property(name="organizationchart_Organization14", type=organizationchart_OrganizationalStructure, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
locations15: BinaryAssociation = BinaryAssociation(
    name="locations15",
    ends={
        Property(name="organizationchart_Location", type=organizationchart_Organization, multiplicity=Multiplicity(1, 1)),
        Property(name="organizationchart_Organization16", type=organizationchart_Location, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
employees17: BinaryAssociation = BinaryAssociation(
    name="employees17",
    ends={
        Property(name="Employee18", type=organizationchart_OrganizationalStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="belongsTo", type=organizationchart_Employee, multiplicity=Multiplicity(0, 9999))
    }
)
isPerformedBy28: BinaryAssociation = BinaryAssociation(
    name="isPerformedBy28",
    ends={
        Property(name="Employee29", type=organizationchart_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="performs", type=organizationchart_Employee, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="organizationchart",
    types={organizationchart_Employee, organizationchart_OrganizationalStructure, organizationchart_Location, organizationchart_Function, organizationchart_Organization, StructureType},
    associations={subStructures20, owns22, manager24, employees26, manages1, belongsTo2, location3, manager6, performs8, leads9, employees12, structures13, locations15, employees17, isPerformedBy28},
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