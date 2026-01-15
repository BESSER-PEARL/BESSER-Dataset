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
RoleType: Enumeration = Enumeration(
    name="RoleType",
    literals={
            EnumerationLiteral(name="Composite"),
			EnumerationLiteral(name="Decision"),
			EnumerationLiteral(name="Transformation"),
			EnumerationLiteral(name="Control")
    }
)

Hierarchy: Enumeration = Enumeration(
    name="Hierarchy",
    literals={
            EnumerationLiteral(name="Supervisor"),
			EnumerationLiteral(name="Subordinate")
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
			EnumerationLiteral(name="Quality"),
			EnumerationLiteral(name="Delay"),
			EnumerationLiteral(name="Cost"),
			EnumerationLiteral(name="Environmental"),
			EnumerationLiteral(name="Legal"),
			EnumerationLiteral(name="Human"),
			EnumerationLiteral(name="Economical")
    }
)

# Classes
company106_Goal = Class(name="company106::Goal")
company106_Department = Class(name="company106::Department")
Function = Class(name="Function")
company106_Room = Class(name="company106::Room")
company106_NamedElement = Class(name="company106::NamedElement", is_abstract=True)
company106_Flow = Class(name="company106::Flow")
NamedElement = Class(name="NamedElement")
company106_Function = Class(name="company106::Function", is_abstract=True)
company106_Employee = Class(name="company106::Employee")
company106_HierarchyLink = Class(name="company106::HierarchyLink")
company106_Company = Class(name="company106::Company")
company106_Agency = Class(name="company106::Agency")
Interval = Class(name="Interval")
company106_Objective = Class(name="company106::Objective")
company106_Workstation = Class(name="company106::Workstation")
company106_Interval = Class(name="company106::Interval", is_abstract=True)
company106_Action = Class(name="company106::Action")
company106_ObjectiveReach = Class(name="company106::ObjectiveReach")

# company106_Goal class attributes and methods
company106_Goal_statement: Property = Property(name="statement", type=StringType)
company106_Goal.attributes={company106_Goal_statement}

# company106_Department class attributes and methods

# Function class attributes and methods

# company106_Room class attributes and methods

# company106_NamedElement class attributes and methods
company106_NamedElement_name: Property = Property(name="name", type=StringType)
company106_NamedElement.attributes={company106_NamedElement_name}

# company106_Flow class attributes and methods

# NamedElement class attributes and methods

# company106_Function class attributes and methods

# company106_Employee class attributes and methods
company106_Employee_fullName: Property = Property(name="fullName", type=StringType)
company106_Employee_socialSecurityNumber: Property = Property(name="socialSecurityNumber", type=StringType)
company106_Employee_address: Property = Property(name="address", type=IntegerType)
company106_Employee.attributes={company106_Employee_socialSecurityNumber, company106_Employee_address, company106_Employee_fullName}

# company106_HierarchyLink class attributes and methods
company106_HierarchyLink_hierarchy: Property = Property(name="hierarchy", type=StringType)
company106_HierarchyLink.attributes={company106_HierarchyLink_hierarchy}

# company106_Company class attributes and methods

# company106_Agency class attributes and methods
company106_Agency_acronym: Property = Property(name="acronym", type=StringType)
company106_Agency_status: Property = Property(name="status", type=StringType)
company106_Agency.attributes={company106_Agency_acronym, company106_Agency_status}

# Interval class attributes and methods

# company106_Objective class attributes and methods
company106_Objective_nature: Property = Property(name="nature", type=StringType)
company106_Objective_type: Property = Property(name="type", type=StringType)
company106_Objective_value: Property = Property(name="value", type=FloatType)
company106_Objective.attributes={company106_Objective_type, company106_Objective_nature, company106_Objective_value}

# company106_Workstation class attributes and methods
company106_Workstation_profileDescription: Property = Property(name="profileDescription", type=StringType)
company106_Workstation.attributes={company106_Workstation_profileDescription}

# company106_Interval class attributes and methods
company106_Interval_dateFrom: Property = Property(name="dateFrom", type=StringType)
company106_Interval_dateTo: Property = Property(name="dateTo", type=StringType)
company106_Interval.attributes={company106_Interval_dateTo, company106_Interval_dateFrom}

# company106_Action class attributes and methods
company106_Action_statement: Property = Property(name="statement", type=StringType)
company106_Action.attributes={company106_Action_statement}

# company106_ObjectiveReach class attributes and methods
company106_ObjectiveReach_value: Property = Property(name="value", type=FloatType)
company106_ObjectiveReach_statement: Property = Property(name="statement", type=StringType)
company106_ObjectiveReach.attributes={company106_ObjectiveReach_statement, company106_ObjectiveReach_value}

# Relationships
agencies0: BinaryAssociation = BinaryAssociation(
    name="agencies0",
    ends={
        Property(name="company106_Agency", type=company106_Company, multiplicity=Multiplicity(1, 1)),
        Property(name="company106_Company", type=company106_Agency, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
goals1: BinaryAssociation = BinaryAssociation(
    name="goals1",
    ends={
        Property(name="company106_Goal", type=company106_Company, multiplicity=Multiplicity(1, 1)),
        Property(name="company106_Company2", type=company106_Goal, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rooms3: BinaryAssociation = BinaryAssociation(
    name="rooms3",
    ends={
        Property(name="company106_Room", type=company106_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="company106_Department", type=company106_Room, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fromFunction4: BinaryAssociation = BinaryAssociation(
    name="fromFunction4",
    ends={
        Property(name="company106_Function", type=company106_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="company106_Flow", type=company106_Function, multiplicity=Multiplicity(0, 1))
    }
)
toFunction5: BinaryAssociation = BinaryAssociation(
    name="toFunction5",
    ends={
        Property(name="company106_Function7", type=company106_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="company106_Flow6", type=company106_Function, multiplicity=Multiplicity(0, 1))
    }
)
hierarchies8: BinaryAssociation = BinaryAssociation(
    name="hierarchies8",
    ends={
        Property(name="company106_HierarchyLink", type=company106_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="company106_Employee", type=company106_HierarchyLink, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
responsibleOf9: BinaryAssociation = BinaryAssociation(
    name="responsibleOf9",
    ends={
        Property(name="company106_Room11", type=company106_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="company106_Employee10", type=company106_Room, multiplicity=Multiplicity(0, 1))
    }
)
parent20: BinaryAssociation = BinaryAssociation(
    name="parent20",
    ends={
        Property(name="company106_Room21", type=company106_Room, multiplicity=Multiplicity(1, 1)),
        Property(name="company106_Room19", type=company106_Room, multiplicity=Multiplicity(0, 9999))
    }
)
workstations22: BinaryAssociation = BinaryAssociation(
    name="workstations22",
    ends={
        Property(name="company106_Workstation", type=company106_Room, multiplicity=Multiplicity(1, 1)),
        Property(name="company106_Room23", type=company106_Workstation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owners24: BinaryAssociation = BinaryAssociation(
    name="owners24",
    ends={
        Property(name="Employee", type=company106_Workstation, multiplicity=Multiplicity(1, 1)),
        Property(name="inChargeOf", type=company106_Employee, multiplicity=Multiplicity(0, 9999))
    }
)
objectives25: BinaryAssociation = BinaryAssociation(
    name="objectives25",
    ends={
        Property(name="company106_Objective", type=company106_Goal, multiplicity=Multiplicity(1, 1)),
        Property(name="company106_Goal26", type=company106_Objective, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inChargeOf12: BinaryAssociation = BinaryAssociation(
    name="inChargeOf12",
    ends={
        Property(name="Workstation", type=company106_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="owners", type=company106_Workstation, multiplicity=Multiplicity(0, 1))
    }
)
fromEmployee13: BinaryAssociation = BinaryAssociation(
    name="fromEmployee13",
    ends={
        Property(name="company106_Employee15", type=company106_HierarchyLink, multiplicity=Multiplicity(1, 1)),
        Property(name="company106_HierarchyLink14", type=company106_Employee, multiplicity=Multiplicity(0, 1))
    }
)
toEmployee16: BinaryAssociation = BinaryAssociation(
    name="toEmployee16",
    ends={
        Property(name="company106_Employee18", type=company106_HierarchyLink, multiplicity=Multiplicity(1, 1)),
        Property(name="company106_HierarchyLink17", type=company106_Employee, multiplicity=Multiplicity(0, 1))
    }
)
trgObjective35: BinaryAssociation = BinaryAssociation(
    name="trgObjective35",
    ends={
        Property(name="company106_Objective37", type=company106_ObjectiveReach, multiplicity=Multiplicity(1, 1)),
        Property(name="company106_ObjectiveReach36", type=company106_Objective, multiplicity=Multiplicity(0, 1))
    }
)
srcAgency38: BinaryAssociation = BinaryAssociation(
    name="srcAgency38",
    ends={
        Property(name="company106_Agency40", type=company106_ObjectiveReach, multiplicity=Multiplicity(1, 1)),
        Property(name="company106_ObjectiveReach39", type=company106_Agency, multiplicity=Multiplicity(0, 1))
    }
)
actions41: BinaryAssociation = BinaryAssociation(
    name="actions41",
    ends={
        Property(name="company106_Action", type=company106_ObjectiveReach, multiplicity=Multiplicity(1, 1)),
        Property(name="company106_ObjectiveReach42", type=company106_Action, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
flows43: BinaryAssociation = BinaryAssociation(
    name="flows43",
    ends={
        Property(name="company106_Flow45", type=company106_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="company106_Function44", type=company106_Flow, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
departments27: BinaryAssociation = BinaryAssociation(
    name="departments27",
    ends={
        Property(name="company106_Department29", type=company106_Agency, multiplicity=Multiplicity(1, 1)),
        Property(name="company106_Agency28", type=company106_Department, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
employees30: BinaryAssociation = BinaryAssociation(
    name="employees30",
    ends={
        Property(name="company106_Employee32", type=company106_Agency, multiplicity=Multiplicity(1, 1)),
        Property(name="company106_Agency31", type=company106_Employee, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reacheds33: BinaryAssociation = BinaryAssociation(
    name="reacheds33",
    ends={
        Property(name="company106_ObjectiveReach", type=company106_Agency, multiplicity=Multiplicity(1, 1)),
        Property(name="company106_Agency34", type=company106_ObjectiveReach, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
flow46: BinaryAssociation = BinaryAssociation(
    name="flow46",
    ends={
        Property(name="company106_Flow48", type=company106_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="company106_Action47", type=company106_Flow, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_company106_Department_Function = Generalization(general=Function, specific=company106_Department)
gen_company106_Flow_NamedElement = Generalization(general=NamedElement, specific=company106_Flow)
gen_company106_Workstation_NamedElement = Generalization(general=NamedElement, specific=company106_Workstation)
gen_company106_Goal_Interval = Generalization(general=Interval, specific=company106_Goal)
gen_company106_Agency_Function = Generalization(general=Function, specific=company106_Agency)
gen_company106_Room_Function = Generalization(general=Function, specific=company106_Room)
gen_company106_Function_NamedElement = Generalization(general=NamedElement, specific=company106_Function)
gen_company106_Action_NamedElement = Generalization(general=NamedElement, specific=company106_Action)

# Domain Model
domain_model = DomainModel(
    name="company106",
    types={company106_Goal, company106_Department, Function, company106_Room, company106_NamedElement, company106_Flow, NamedElement, company106_Function, company106_Employee, company106_HierarchyLink, company106_Company, company106_Agency, Interval, company106_Objective, company106_Workstation, company106_Interval, company106_Action, company106_ObjectiveReach, RoleType, Hierarchy, ObjectiveType, ObjectiveNature},
    associations={agencies0, goals1, rooms3, fromFunction4, toFunction5, hierarchies8, responsibleOf9, parent20, workstations22, owners24, objectives25, inChargeOf12, fromEmployee13, toEmployee16, trgObjective35, srcAgency38, actions41, flows43, departments27, employees30, reacheds33, flow46},
    generalizations={gen_company106_Department_Function, gen_company106_Flow_NamedElement, gen_company106_Workstation_NamedElement, gen_company106_Goal_Interval, gen_company106_Agency_Function, gen_company106_Room_Function, gen_company106_Function_NamedElement, gen_company106_Action_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)