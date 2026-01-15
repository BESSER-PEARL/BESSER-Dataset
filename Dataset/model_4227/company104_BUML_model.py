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
Hierarchy: Enumeration = Enumeration(
    name="Hierarchy",
    literals={
            EnumerationLiteral(name="Supervisor"),
			EnumerationLiteral(name="Subordinate")
    }
)

RoleType: Enumeration = Enumeration(
    name="RoleType",
    literals={
            EnumerationLiteral(name="Composite"),
			EnumerationLiteral(name="Decision"),
			EnumerationLiteral(name="Transformation"),
			EnumerationLiteral(name="Control")
    }
)

ObjectiveType: Enumeration = Enumeration(
    name="ObjectiveType",
    literals={
            EnumerationLiteral(name="None"),
			EnumerationLiteral(name="Strategic"),
			EnumerationLiteral(name="Tactic"),
			EnumerationLiteral(name="Operational")
    }
)

ObjectiveNature: Enumeration = Enumeration(
    name="ObjectiveNature",
    literals={
            EnumerationLiteral(name="None"),
			EnumerationLiteral(name="Performance"),
			EnumerationLiteral(name="Quality"),
			EnumerationLiteral(name="Delay"),
			EnumerationLiteral(name="Cost"),
			EnumerationLiteral(name="Environmental"),
			EnumerationLiteral(name="Legal"),
			EnumerationLiteral(name="Human"),
			EnumerationLiteral(name="Economical"),
			EnumerationLiteral(name="Other")
    }
)

# Classes
company104_Company = Class(name="company104::Company")
company104_Agency = Class(name="company104::Agency")
company104_Goal = Class(name="company104::Goal")
company104_Department = Class(name="company104::Department")
Function = Class(name="Function")
company104_Room = Class(name="company104::Room")
company104_NamedElement = Class(name="company104::NamedElement", is_abstract=True)
company104_Flow = Class(name="company104::Flow")
NamedElement = Class(name="NamedElement")
company104_Function = Class(name="company104::Function", is_abstract=True)
company104_Employee = Class(name="company104::Employee")
company104_HierarchyLink = Class(name="company104::HierarchyLink")
company104_Workstation = Class(name="company104::Workstation")
Interval = Class(name="Interval")
company104_Objective = Class(name="company104::Objective")
company104_ObjectiveReach = Class(name="company104::ObjectiveReach")
company104_Interval = Class(name="company104::Interval", is_abstract=True)

# company104_Company class attributes and methods

# company104_Agency class attributes and methods
company104_Agency_Accronym: Property = Property(name="Accronym", type=StringType)
company104_Agency_Status: Property = Property(name="Status", type=StringType)
company104_Agency.attributes={company104_Agency_Status, company104_Agency_Accronym}

# company104_Goal class attributes and methods
company104_Goal_statement: Property = Property(name="statement", type=StringType)
company104_Goal.attributes={company104_Goal_statement}

# company104_Department class attributes and methods

# Function class attributes and methods

# company104_Room class attributes and methods

# company104_NamedElement class attributes and methods
company104_NamedElement_name: Property = Property(name="name", type=StringType)
company104_NamedElement.attributes={company104_NamedElement_name}

# company104_Flow class attributes and methods

# NamedElement class attributes and methods

# company104_Function class attributes and methods

# company104_Employee class attributes and methods
company104_Employee_fullName: Property = Property(name="fullName", type=StringType)
company104_Employee_socialSecurityNumber: Property = Property(name="socialSecurityNumber", type=StringType)
company104_Employee_address: Property = Property(name="address", type=IntegerType)
company104_Employee.attributes={company104_Employee_address, company104_Employee_fullName, company104_Employee_socialSecurityNumber}

# company104_HierarchyLink class attributes and methods
company104_HierarchyLink_hierarchy: Property = Property(name="hierarchy", type=StringType)
company104_HierarchyLink.attributes={company104_HierarchyLink_hierarchy}

# company104_Workstation class attributes and methods
company104_Workstation_ProfileDescription: Property = Property(name="ProfileDescription", type=StringType)
company104_Workstation.attributes={company104_Workstation_ProfileDescription}

# Interval class attributes and methods

# company104_Objective class attributes and methods
company104_Objective_nature: Property = Property(name="nature", type=StringType)
company104_Objective_type: Property = Property(name="type", type=StringType)
company104_Objective_value: Property = Property(name="value", type=FloatType)
company104_Objective.attributes={company104_Objective_type, company104_Objective_nature, company104_Objective_value}

# company104_ObjectiveReach class attributes and methods
company104_ObjectiveReach_value: Property = Property(name="value", type=FloatType)
company104_ObjectiveReach_statement: Property = Property(name="statement", type=StringType)
company104_ObjectiveReach.attributes={company104_ObjectiveReach_value, company104_ObjectiveReach_statement}

# company104_Interval class attributes and methods
company104_Interval_dateFrom: Property = Property(name="dateFrom", type=StringType)
company104_Interval_dateTo: Property = Property(name="dateTo", type=StringType)
company104_Interval.attributes={company104_Interval_dateTo, company104_Interval_dateFrom}

# Relationships
agencies0: BinaryAssociation = BinaryAssociation(
    name="agencies0",
    ends={
        Property(name="company104_Agency", type=company104_Company, multiplicity=Multiplicity(1, 1)),
        Property(name="company104_Company", type=company104_Agency, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
goals1: BinaryAssociation = BinaryAssociation(
    name="goals1",
    ends={
        Property(name="company104_Goal", type=company104_Company, multiplicity=Multiplicity(1, 1)),
        Property(name="company104_Company2", type=company104_Goal, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rooms3: BinaryAssociation = BinaryAssociation(
    name="rooms3",
    ends={
        Property(name="company104_Room", type=company104_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="company104_Department", type=company104_Room, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fromFunction4: BinaryAssociation = BinaryAssociation(
    name="fromFunction4",
    ends={
        Property(name="company104_Function", type=company104_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="company104_Flow", type=company104_Function, multiplicity=Multiplicity(0, 1))
    }
)
toFunction5: BinaryAssociation = BinaryAssociation(
    name="toFunction5",
    ends={
        Property(name="company104_Function7", type=company104_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="company104_Flow6", type=company104_Function, multiplicity=Multiplicity(0, 1))
    }
)
hierarchies8: BinaryAssociation = BinaryAssociation(
    name="hierarchies8",
    ends={
        Property(name="company104_HierarchyLink", type=company104_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="company104_Employee", type=company104_HierarchyLink, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
responsibleOf9: BinaryAssociation = BinaryAssociation(
    name="responsibleOf9",
    ends={
        Property(name="company104_Room11", type=company104_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="company104_Employee10", type=company104_Room, multiplicity=Multiplicity(0, 1))
    }
)
inChargeOf12: BinaryAssociation = BinaryAssociation(
    name="inChargeOf12",
    ends={
        Property(name="Workstation", type=company104_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="owners", type=company104_Workstation, multiplicity=Multiplicity(0, 1))
    }
)
fromEmployee13: BinaryAssociation = BinaryAssociation(
    name="fromEmployee13",
    ends={
        Property(name="company104_Employee15", type=company104_HierarchyLink, multiplicity=Multiplicity(1, 1)),
        Property(name="company104_HierarchyLink14", type=company104_Employee, multiplicity=Multiplicity(0, 1))
    }
)
toEmployee16: BinaryAssociation = BinaryAssociation(
    name="toEmployee16",
    ends={
        Property(name="company104_Employee18", type=company104_HierarchyLink, multiplicity=Multiplicity(1, 1)),
        Property(name="company104_HierarchyLink17", type=company104_Employee, multiplicity=Multiplicity(0, 1))
    }
)
parent20: BinaryAssociation = BinaryAssociation(
    name="parent20",
    ends={
        Property(name="company104_Room21", type=company104_Room, multiplicity=Multiplicity(1, 1)),
        Property(name="company104_Room19", type=company104_Room, multiplicity=Multiplicity(0, 9999))
    }
)
workstations22: BinaryAssociation = BinaryAssociation(
    name="workstations22",
    ends={
        Property(name="company104_Workstation", type=company104_Room, multiplicity=Multiplicity(1, 1)),
        Property(name="company104_Room23", type=company104_Workstation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owners24: BinaryAssociation = BinaryAssociation(
    name="owners24",
    ends={
        Property(name="Employee", type=company104_Workstation, multiplicity=Multiplicity(1, 1)),
        Property(name="inChargeOf", type=company104_Employee, multiplicity=Multiplicity(0, 9999))
    }
)
objectives25: BinaryAssociation = BinaryAssociation(
    name="objectives25",
    ends={
        Property(name="company104_Objective", type=company104_Goal, multiplicity=Multiplicity(1, 1)),
        Property(name="company104_Goal26", type=company104_Objective, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
departments27: BinaryAssociation = BinaryAssociation(
    name="departments27",
    ends={
        Property(name="company104_Department29", type=company104_Agency, multiplicity=Multiplicity(1, 1)),
        Property(name="company104_Agency28", type=company104_Department, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
employees30: BinaryAssociation = BinaryAssociation(
    name="employees30",
    ends={
        Property(name="company104_Employee32", type=company104_Agency, multiplicity=Multiplicity(1, 1)),
        Property(name="company104_Agency31", type=company104_Employee, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reacheds33: BinaryAssociation = BinaryAssociation(
    name="reacheds33",
    ends={
        Property(name="company104_ObjectiveReach", type=company104_Agency, multiplicity=Multiplicity(1, 1)),
        Property(name="company104_Agency34", type=company104_ObjectiveReach, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
trgObjective35: BinaryAssociation = BinaryAssociation(
    name="trgObjective35",
    ends={
        Property(name="company104_Objective37", type=company104_ObjectiveReach, multiplicity=Multiplicity(1, 1)),
        Property(name="company104_ObjectiveReach36", type=company104_Objective, multiplicity=Multiplicity(0, 1))
    }
)
srcAgency38: BinaryAssociation = BinaryAssociation(
    name="srcAgency38",
    ends={
        Property(name="company104_Agency40", type=company104_ObjectiveReach, multiplicity=Multiplicity(1, 1)),
        Property(name="company104_ObjectiveReach39", type=company104_Agency, multiplicity=Multiplicity(0, 1))
    }
)
flows41: BinaryAssociation = BinaryAssociation(
    name="flows41",
    ends={
        Property(name="company104_Flow43", type=company104_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="company104_Function42", type=company104_Flow, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_company104_Department_Function = Generalization(general=Function, specific=company104_Department)
gen_company104_Flow_NamedElement = Generalization(general=NamedElement, specific=company104_Flow)
gen_company104_Room_Function = Generalization(general=Function, specific=company104_Room)
gen_company104_Workstation_NamedElement = Generalization(general=NamedElement, specific=company104_Workstation)
gen_company104_Goal_Interval = Generalization(general=Interval, specific=company104_Goal)
gen_company104_Agency_Function = Generalization(general=Function, specific=company104_Agency)
gen_company104_Function_NamedElement = Generalization(general=NamedElement, specific=company104_Function)

# Domain Model
domain_model = DomainModel(
    name="company104",
    types={company104_Company, company104_Agency, company104_Goal, company104_Department, Function, company104_Room, company104_NamedElement, company104_Flow, NamedElement, company104_Function, company104_Employee, company104_HierarchyLink, company104_Workstation, Interval, company104_Objective, company104_ObjectiveReach, company104_Interval, Hierarchy, RoleType, ObjectiveType, ObjectiveNature},
    associations={agencies0, goals1, rooms3, fromFunction4, toFunction5, hierarchies8, responsibleOf9, inChargeOf12, fromEmployee13, toEmployee16, parent20, workstations22, owners24, objectives25, departments27, employees30, reacheds33, trgObjective35, srcAgency38, flows41},
    generalizations={gen_company104_Department_Function, gen_company104_Flow_NamedElement, gen_company104_Room_Function, gen_company104_Workstation_NamedElement, gen_company104_Goal_Interval, gen_company104_Agency_Function, gen_company104_Function_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)