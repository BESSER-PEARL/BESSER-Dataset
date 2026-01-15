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
remember_Customers = Class(name="remember::Customers")
remember_Folder = Class(name="remember::Folder")
Node = Class(name="Node")
remember_Task = Class(name="remember::Task")
remember_Customer = Class(name="remember::Customer")
remember_Project = Class(name="remember::Project")
remember_TimeSpent = Class(name="remember::TimeSpent")
remember_Node = Class(name="remember::Node", is_abstract=True)
remember_KeyManager = Class(name="remember::KeyManager")
remember_KeyIdPair = Class(name="remember::KeyIdPair")
remember_InvoiceSpecification = Class(name="remember::InvoiceSpecification")
remember_Year = Class(name="remember::Year")
remember_Years = Class(name="remember::Years")

# remember_Customers class attributes and methods

# remember_Folder class attributes and methods

# Node class attributes and methods

# remember_Task class attributes and methods
remember_Task_taskId: Property = Property(name="taskId", type=IntegerType)
remember_Task_priority: Property = Property(name="priority", type=StringType)
remember_Task_status: Property = Property(name="status", type=StringType)
remember_Task_budget: Property = Property(name="budget", type=StringType)
remember_Task_text: Property = Property(name="text", type=StringType)
remember_Task_done: Property = Property(name="done", type=BooleanType)
remember_Task.attributes={remember_Task_priority, remember_Task_taskId, remember_Task_done, remember_Task_budget, remember_Task_status, remember_Task_text}

# remember_Customer class attributes and methods
remember_Customer_customerId: Property = Property(name="customerId", type=StringType)
remember_Customer_name: Property = Property(name="name", type=StringType)
remember_Customer.attributes={remember_Customer_name, remember_Customer_customerId}

# remember_Project class attributes and methods
remember_Project_projectId: Property = Property(name="projectId", type=StringType)
remember_Project_projectNumber: Property = Property(name="projectNumber", type=StringType)
remember_Project_description: Property = Property(name="description", type=StringType)
remember_Project.attributes={remember_Project_projectId, remember_Project_description, remember_Project_projectNumber}

# remember_TimeSpent class attributes and methods
remember_TimeSpent_invoiced: Property = Property(name="invoiced", type=BooleanType)
remember_TimeSpent_timeSpentId: Property = Property(name="timeSpentId", type=StringType)
remember_TimeSpent_date: Property = Property(name="date", type=DateType)
remember_TimeSpent_minutes: Property = Property(name="minutes", type=IntegerType)
remember_TimeSpent_comment: Property = Property(name="comment", type=StringType)
remember_TimeSpent.attributes={remember_TimeSpent_minutes, remember_TimeSpent_comment, remember_TimeSpent_date, remember_TimeSpent_invoiced, remember_TimeSpent_timeSpentId}

# remember_Node class attributes and methods
remember_Node_nodeId: Property = Property(name="nodeId", type=StringType)
remember_Node_nodeType: Property = Property(name="nodeType", type=StringType)
remember_Node_parentNodeId: Property = Property(name="parentNodeId", type=StringType)
remember_Node_parentNodeType: Property = Property(name="parentNodeType", type=StringType)
remember_Node_sequence: Property = Property(name="sequence", type=IntegerType)
remember_Node_name: Property = Property(name="name", type=StringType)
remember_Node_description: Property = Property(name="description", type=StringType)
remember_Node_dateCreated: Property = Property(name="dateCreated", type=DateType)
remember_Node_dateModified: Property = Property(name="dateModified", type=DateType)
remember_Node_markedForDeletion: Property = Property(name="markedForDeletion", type=BooleanType)
remember_Node.attributes={remember_Node_name, remember_Node_description, remember_Node_dateCreated, remember_Node_nodeType, remember_Node_parentNodeId, remember_Node_parentNodeType, remember_Node_nodeId, remember_Node_dateModified, remember_Node_sequence, remember_Node_markedForDeletion}

# remember_KeyManager class attributes and methods

# remember_KeyIdPair class attributes and methods
remember_KeyIdPair_key: Property = Property(name="key", type=StringType)
remember_KeyIdPair_id: Property = Property(name="id", type=StringType)
remember_KeyIdPair.attributes={remember_KeyIdPair_id, remember_KeyIdPair_key}

# remember_InvoiceSpecification class attributes and methods
remember_InvoiceSpecification_month: Property = Property(name="month", type=IntegerType)
remember_InvoiceSpecification.attributes={remember_InvoiceSpecification_month}

# remember_Year class attributes and methods
remember_Year_year: Property = Property(name="year", type=IntegerType)
remember_Year.attributes={remember_Year_year}

# remember_Years class attributes and methods

# Relationships
folders2: BinaryAssociation = BinaryAssociation(
    name="folders2",
    ends={
        Property(name="Folder", type=remember_Folder, multiplicity=Multiplicity(1, 1)),
        Property(name="parent3", type=remember_Folder, multiplicity=Multiplicity(0, 9999))
    }
)
parent5: BinaryAssociation = BinaryAssociation(
    name="parent5",
    ends={
        Property(name="Folder6", type=remember_Folder, multiplicity=Multiplicity(1, 1)),
        Property(name="folders", type=remember_Folder, multiplicity=Multiplicity(0, 1))
    }
)
workspace7: BinaryAssociation = BinaryAssociation(
    name="workspace7",
    ends={
        Property(name="remember_Customers", type=remember_Folder, multiplicity=Multiplicity(1, 1)),
        Property(name="remember_Folder", type=remember_Customers, multiplicity=Multiplicity(0, 1))
    }
)
Tasks0: BinaryAssociation = BinaryAssociation(
    name="Tasks0",
    ends={
        Property(name="Task", type=remember_Folder, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=remember_Task, multiplicity=Multiplicity(0, 9999))
    }
)
customer11: BinaryAssociation = BinaryAssociation(
    name="customer11",
    ends={
        Property(name="Customer", type=remember_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="nodes", type=remember_Customer, multiplicity=Multiplicity(0, 1))
    }
)
project12: BinaryAssociation = BinaryAssociation(
    name="project12",
    ends={
        Property(name="Project", type=remember_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="nodes13", type=remember_Project, multiplicity=Multiplicity(0, 1))
    }
)
parent8: BinaryAssociation = BinaryAssociation(
    name="parent8",
    ends={
        Property(name="Folder9", type=remember_Task, multiplicity=Multiplicity(1, 1)),
        Property(name="Tasks", type=remember_Folder, multiplicity=Multiplicity(0, 1))
    }
)
timeSpent10: BinaryAssociation = BinaryAssociation(
    name="timeSpent10",
    ends={
        Property(name="TimeSpent", type=remember_Task, multiplicity=Multiplicity(1, 1)),
        Property(name="task", type=remember_TimeSpent, multiplicity=Multiplicity(0, 9999))
    }
)
nodes17: BinaryAssociation = BinaryAssociation(
    name="nodes17",
    ends={
        Property(name="Node", type=remember_Customer, multiplicity=Multiplicity(1, 1)),
        Property(name="customer18", type=remember_Node, multiplicity=Multiplicity(0, 9999))
    }
)
customer19: BinaryAssociation = BinaryAssociation(
    name="customer19",
    ends={
        Property(name="Customer20", type=remember_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="projects", type=remember_Customer, multiplicity=Multiplicity(1, 1))
    }
)
nodes21: BinaryAssociation = BinaryAssociation(
    name="nodes21",
    ends={
        Property(name="Node22", type=remember_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="project", type=remember_Node, multiplicity=Multiplicity(0, 9999))
    }
)
customers23: BinaryAssociation = BinaryAssociation(
    name="customers23",
    ends={
        Property(name="remember_Customer", type=remember_Customers, multiplicity=Multiplicity(1, 1)),
        Property(name="remember_Customers24", type=remember_Customer, multiplicity=Multiplicity(0, 9999))
    }
)
keyIdPairs14: BinaryAssociation = BinaryAssociation(
    name="keyIdPairs14",
    ends={
        Property(name="remember_KeyIdPair", type=remember_KeyManager, multiplicity=Multiplicity(1, 1)),
        Property(name="remember_KeyManager", type=remember_KeyIdPair, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
projects15: BinaryAssociation = BinaryAssociation(
    name="projects15",
    ends={
        Property(name="Project16", type=remember_Customer, multiplicity=Multiplicity(1, 1)),
        Property(name="customer", type=remember_Project, multiplicity=Multiplicity(0, 9999))
    }
)
project25: BinaryAssociation = BinaryAssociation(
    name="project25",
    ends={
        Property(name="remember_TimeSpent", type=remember_Project, multiplicity=Multiplicity(0, 1)),
        Property(name="remember_Project", type=remember_TimeSpent, multiplicity=Multiplicity(1, 1))
    }
)
task26: BinaryAssociation = BinaryAssociation(
    name="task26",
    ends={
        Property(name="Task27", type=remember_TimeSpent, multiplicity=Multiplicity(1, 1)),
        Property(name="timeSpent", type=remember_Task, multiplicity=Multiplicity(1, 1))
    }
)
invoiceSpecification28: BinaryAssociation = BinaryAssociation(
    name="invoiceSpecification28",
    ends={
        Property(name="InvoiceSpecification", type=remember_TimeSpent, multiplicity=Multiplicity(1, 1)),
        Property(name="timeSpent29", type=remember_InvoiceSpecification, multiplicity=Multiplicity(1, 1))
    }
)
invoiceSpecifications30: BinaryAssociation = BinaryAssociation(
    name="invoiceSpecifications30",
    ends={
        Property(name="InvoiceSpecification31", type=remember_Year, multiplicity=Multiplicity(1, 1)),
        Property(name="year", type=remember_InvoiceSpecification, multiplicity=Multiplicity(0, 9999))
    }
)
years32: BinaryAssociation = BinaryAssociation(
    name="years32",
    ends={
        Property(name="Years", type=remember_Year, multiplicity=Multiplicity(1, 1)),
        Property(name="year33", type=remember_Years, multiplicity=Multiplicity(1, 1))
    }
)
timeSpent34: BinaryAssociation = BinaryAssociation(
    name="timeSpent34",
    ends={
        Property(name="TimeSpent35", type=remember_InvoiceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="invoiceSpecification", type=remember_TimeSpent, multiplicity=Multiplicity(0, 9999))
    }
)
year36: BinaryAssociation = BinaryAssociation(
    name="year36",
    ends={
        Property(name="Year", type=remember_InvoiceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="invoiceSpecifications", type=remember_Year, multiplicity=Multiplicity(1, 1))
    }
)
year37: BinaryAssociation = BinaryAssociation(
    name="year37",
    ends={
        Property(name="Year38", type=remember_Years, multiplicity=Multiplicity(1, 1)),
        Property(name="years", type=remember_Year, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_remember_Task_Node = Generalization(general=Node, specific=remember_Task)
gen_remember_Folder_Node = Generalization(general=Node, specific=remember_Folder)

# Domain Model
domain_model = DomainModel(
    name="remember",
    types={remember_Customers, remember_Folder, Node, remember_Task, remember_Customer, remember_Project, remember_TimeSpent, remember_Node, remember_KeyManager, remember_KeyIdPair, remember_InvoiceSpecification, remember_Year, remember_Years},
    associations={folders2, parent5, workspace7, Tasks0, customer11, project12, parent8, timeSpent10, nodes17, customer19, nodes21, customers23, keyIdPairs14, projects15, project25, task26, invoiceSpecification28, invoiceSpecifications30, years32, timeSpent34, year36, year37},
    generalizations={gen_remember_Task_Node, gen_remember_Folder_Node},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)