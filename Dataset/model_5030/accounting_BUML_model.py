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
InvoiceState: Enumeration = Enumeration(
    name="InvoiceState",
    literals={
            EnumerationLiteral(name="New"),
			EnumerationLiteral(name="Invoiced"),
			EnumerationLiteral(name="Paid")
    }
)

# Classes
accounting_NamedElement = Class(name="accounting::NamedElement", is_abstract=True)
accounting_Client = Class(name="accounting::Client")
NamedElement = Class(name="NamedElement")
accounting_Project = Class(name="accounting::Project")
accounting_Order = Class(name="accounting::Order")
accounting_Employee = Class(name="accounting::Employee")
accounting_WorkPackage = Class(name="accounting::WorkPackage")
accounting_Clients = Class(name="accounting::Clients")
accounting_Employees = Class(name="accounting::Employees")
accounting_Deliverable = Class(name="accounting::Deliverable")
accounting_Invoice = Class(name="accounting::Invoice")

# accounting_NamedElement class attributes and methods
accounting_NamedElement_name: Property = Property(name="name", type=StringType)
accounting_NamedElement.attributes={accounting_NamedElement_name}

# accounting_Client class attributes and methods

# NamedElement class attributes and methods

# accounting_Project class attributes and methods

# accounting_Order class attributes and methods
accounting_Order_id: Property = Property(name="id", type=StringType)
accounting_Order_paymentOffset: Property = Property(name="paymentOffset", type=IntegerType)
accounting_Order_pricePerUnit: Property = Property(name="pricePerUnit", type=FloatType)
accounting_Order_m_validateUnitAmount: Method = Method(name="validateUnitAmount", parameters={Parameter(name='diagnosticChain'), Parameter(name='context')}, type=BooleanType)
accounting_Order.attributes={accounting_Order_id, accounting_Order_paymentOffset, accounting_Order_pricePerUnit}
accounting_Order.methods={accounting_Order_m_validateUnitAmount}

# accounting_Employee class attributes and methods
accounting_Employee_emails: Property = Property(name="emails", type=StringType)
accounting_Employee.attributes={accounting_Employee_emails}

# accounting_WorkPackage class attributes and methods
accounting_WorkPackage_date: Property = Property(name="date", type=DateType)
accounting_WorkPackage_hours: Property = Property(name="hours", type=FloatType)
accounting_WorkPackage_task: Property = Property(name="task", type=StringType)
accounting_WorkPackage_comment: Property = Property(name="comment", type=StringType)
accounting_WorkPackage.attributes={accounting_WorkPackage_comment, accounting_WorkPackage_date, accounting_WorkPackage_hours, accounting_WorkPackage_task}

# accounting_Clients class attributes and methods

# accounting_Employees class attributes and methods

# accounting_Deliverable class attributes and methods
accounting_Deliverable_dueDate: Property = Property(name="dueDate", type=DateType)
accounting_Deliverable_unitAmount: Property = Property(name="unitAmount", type=FloatType)
accounting_Deliverable.attributes={accounting_Deliverable_unitAmount, accounting_Deliverable_dueDate}

# accounting_Invoice class attributes and methods
accounting_Invoice_id: Property = Property(name="id", type=StringType)
accounting_Invoice_unitAmount: Property = Property(name="unitAmount", type=FloatType)
accounting_Invoice_invoiceDate: Property = Property(name="invoiceDate", type=DateType)
accounting_Invoice_dueDate: Property = Property(name="dueDate", type=DateType)
accounting_Invoice_state: Property = Property(name="state", type=StringType)
accounting_Invoice.attributes={accounting_Invoice_state, accounting_Invoice_dueDate, accounting_Invoice_unitAmount, accounting_Invoice_invoiceDate, accounting_Invoice_id}

# Relationships
projects0: BinaryAssociation = BinaryAssociation(
    name="projects0",
    ends={
        Property(name="Project", type=accounting_Client, multiplicity=Multiplicity(1, 1)),
        Property(name="client", type=accounting_Project, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
client1: BinaryAssociation = BinaryAssociation(
    name="client1",
    ends={
        Property(name="Client", type=accounting_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="projects", type=accounting_Client, multiplicity=Multiplicity(1, 1))
    }
)
orders2: BinaryAssociation = BinaryAssociation(
    name="orders2",
    ends={
        Property(name="Order", type=accounting_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="project", type=accounting_Order, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
order8: BinaryAssociation = BinaryAssociation(
    name="order8",
    ends={
        Property(name="Order9", type=accounting_Deliverable, multiplicity=Multiplicity(1, 1)),
        Property(name="deliverables", type=accounting_Order, multiplicity=Multiplicity(1, 1))
    }
)
advisor10: BinaryAssociation = BinaryAssociation(
    name="advisor10",
    ends={
        Property(name="accounting_Employee", type=accounting_Invoice, multiplicity=Multiplicity(1, 1)),
        Property(name="accounting_Invoice", type=accounting_Employee, multiplicity=Multiplicity(0, 1))
    }
)
order11: BinaryAssociation = BinaryAssociation(
    name="order11",
    ends={
        Property(name="Order12", type=accounting_Invoice, multiplicity=Multiplicity(1, 1)),
        Property(name="invoices", type=accounting_Order, multiplicity=Multiplicity(1, 1))
    }
)
work13: BinaryAssociation = BinaryAssociation(
    name="work13",
    ends={
        Property(name="accounting_WorkPackage", type=accounting_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="accounting_Employee14", type=accounting_WorkPackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
project15: BinaryAssociation = BinaryAssociation(
    name="project15",
    ends={
        Property(name="accounting_Project", type=accounting_WorkPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="accounting_WorkPackage16", type=accounting_Project, multiplicity=Multiplicity(1, 1))
    }
)
clients17: BinaryAssociation = BinaryAssociation(
    name="clients17",
    ends={
        Property(name="accounting_Client", type=accounting_Clients, multiplicity=Multiplicity(1, 1)),
        Property(name="accounting_Clients", type=accounting_Client, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
employees18: BinaryAssociation = BinaryAssociation(
    name="employees18",
    ends={
        Property(name="accounting_Employee19", type=accounting_Employees, multiplicity=Multiplicity(1, 1)),
        Property(name="accounting_Employees", type=accounting_Employee, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
project3: BinaryAssociation = BinaryAssociation(
    name="project3",
    ends={
        Property(name="Project4", type=accounting_Order, multiplicity=Multiplicity(1, 1)),
        Property(name="orders", type=accounting_Project, multiplicity=Multiplicity(1, 1))
    }
)
deliverables5: BinaryAssociation = BinaryAssociation(
    name="deliverables5",
    ends={
        Property(name="Deliverable", type=accounting_Order, multiplicity=Multiplicity(1, 1)),
        Property(name="order", type=accounting_Deliverable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
invoices6: BinaryAssociation = BinaryAssociation(
    name="invoices6",
    ends={
        Property(name="Invoice", type=accounting_Order, multiplicity=Multiplicity(1, 1)),
        Property(name="order7", type=accounting_Invoice, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_accounting_Client_NamedElement = Generalization(general=NamedElement, specific=accounting_Client)
gen_accounting_Project_NamedElement = Generalization(general=NamedElement, specific=accounting_Project)
gen_accounting_Employee_NamedElement = Generalization(general=NamedElement, specific=accounting_Employee)

# Domain Model
domain_model = DomainModel(
    name="accounting",
    types={accounting_NamedElement, accounting_Client, NamedElement, accounting_Project, accounting_Order, accounting_Employee, accounting_WorkPackage, accounting_Clients, accounting_Employees, accounting_Deliverable, accounting_Invoice, InvoiceState},
    associations={projects0, client1, orders2, order8, advisor10, order11, work13, project15, clients17, employees18, project3, deliverables5, invoices6},
    generalizations={gen_accounting_Client_NamedElement, gen_accounting_Project_NamedElement, gen_accounting_Employee_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)