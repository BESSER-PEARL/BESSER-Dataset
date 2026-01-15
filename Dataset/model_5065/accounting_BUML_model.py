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
accounting_Project = Class(name="accounting::Project")
accounting_Deliverable = Class(name="accounting::Deliverable")
accounting_Invoice = Class(name="accounting::Invoice")
accounting_Employee = Class(name="accounting::Employee")
accounting_NamedElement = Class(name="accounting::NamedElement", is_abstract=True)
accounting_Order = Class(name="accounting::Order")
accounting_ClientDatabase = Class(name="accounting::ClientDatabase")
accounting_EmployeeDatabase = Class(name="accounting::EmployeeDatabase")
accounting_Client = Class(name="accounting::Client")
NamedElement = Class(name="NamedElement")

# accounting_Project class attributes and methods

# accounting_Deliverable class attributes and methods
accounting_Deliverable_dueDate: Property = Property(name="dueDate", type=DateType)
accounting_Deliverable_unitAmount: Property = Property(name="unitAmount", type=FloatType)
accounting_Deliverable.attributes={accounting_Deliverable_dueDate, accounting_Deliverable_unitAmount}

# accounting_Invoice class attributes and methods
accounting_Invoice_id: Property = Property(name="id", type=StringType)
accounting_Invoice_unitAmount: Property = Property(name="unitAmount", type=FloatType)
accounting_Invoice_invoiceDate: Property = Property(name="invoiceDate", type=DateType)
accounting_Invoice_state: Property = Property(name="state", type=StringType)
accounting_Invoice.attributes={accounting_Invoice_state, accounting_Invoice_invoiceDate, accounting_Invoice_unitAmount, accounting_Invoice_id}

# accounting_Employee class attributes and methods
accounting_Employee_emails: Property = Property(name="emails", type=StringType)
accounting_Employee.attributes={accounting_Employee_emails}

# accounting_NamedElement class attributes and methods
accounting_NamedElement_name: Property = Property(name="name", type=StringType)
accounting_NamedElement.attributes={accounting_NamedElement_name}

# accounting_Order class attributes and methods
accounting_Order_id: Property = Property(name="id", type=StringType)
accounting_Order_paymentOffset: Property = Property(name="paymentOffset", type=IntegerType)
accounting_Order_pricePerUnit: Property = Property(name="pricePerUnit", type=FloatType)
accounting_Order_m_validateUnitAmount: Method = Method(name="validateUnitAmount", parameters={Parameter(name='context'), Parameter(name='diagnosticChain')}, type=BooleanType)
accounting_Order.attributes={accounting_Order_id, accounting_Order_paymentOffset, accounting_Order_pricePerUnit}
accounting_Order.methods={accounting_Order_m_validateUnitAmount}

# accounting_ClientDatabase class attributes and methods

# accounting_EmployeeDatabase class attributes and methods

# accounting_Client class attributes and methods

# NamedElement class attributes and methods

# Relationships
project0: BinaryAssociation = BinaryAssociation(
    name="project0",
    ends={
        Property(name="Project", type=accounting_Order, multiplicity=Multiplicity(1, 1)),
        Property(name="orders", type=accounting_Project, multiplicity=Multiplicity(1, 1))
    }
)
deliverables1: BinaryAssociation = BinaryAssociation(
    name="deliverables1",
    ends={
        Property(name="Deliverable", type=accounting_Order, multiplicity=Multiplicity(1, 1)),
        Property(name="order", type=accounting_Deliverable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
invoices2: BinaryAssociation = BinaryAssociation(
    name="invoices2",
    ends={
        Property(name="Invoice", type=accounting_Order, multiplicity=Multiplicity(1, 1)),
        Property(name="order3", type=accounting_Invoice, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
order4: BinaryAssociation = BinaryAssociation(
    name="order4",
    ends={
        Property(name="Order", type=accounting_Deliverable, multiplicity=Multiplicity(1, 1)),
        Property(name="deliverables", type=accounting_Order, multiplicity=Multiplicity(1, 1))
    }
)
advisor5: BinaryAssociation = BinaryAssociation(
    name="advisor5",
    ends={
        Property(name="accounting_Employee", type=accounting_Invoice, multiplicity=Multiplicity(1, 1)),
        Property(name="accounting_Invoice", type=accounting_Employee, multiplicity=Multiplicity(0, 1))
    }
)
order6: BinaryAssociation = BinaryAssociation(
    name="order6",
    ends={
        Property(name="Order7", type=accounting_Invoice, multiplicity=Multiplicity(1, 1)),
        Property(name="invoices", type=accounting_Order, multiplicity=Multiplicity(1, 1))
    }
)
clients15: BinaryAssociation = BinaryAssociation(
    name="clients15",
    ends={
        Property(name="accounting_Client", type=accounting_ClientDatabase, multiplicity=Multiplicity(1, 1)),
        Property(name="accounting_ClientDatabase", type=accounting_Client, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
employees16: BinaryAssociation = BinaryAssociation(
    name="employees16",
    ends={
        Property(name="accounting_Employee17", type=accounting_EmployeeDatabase, multiplicity=Multiplicity(1, 1)),
        Property(name="accounting_EmployeeDatabase", type=accounting_Employee, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
projects8: BinaryAssociation = BinaryAssociation(
    name="projects8",
    ends={
        Property(name="Project9", type=accounting_Client, multiplicity=Multiplicity(1, 1)),
        Property(name="client", type=accounting_Project, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
client10: BinaryAssociation = BinaryAssociation(
    name="client10",
    ends={
        Property(name="Client", type=accounting_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="projects", type=accounting_Client, multiplicity=Multiplicity(1, 1))
    }
)
orders11: BinaryAssociation = BinaryAssociation(
    name="orders11",
    ends={
        Property(name="Order12", type=accounting_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="project", type=accounting_Order, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
liason13: BinaryAssociation = BinaryAssociation(
    name="liason13",
    ends={
        Property(name="accounting_Employee14", type=accounting_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="accounting_Project", type=accounting_Employee, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_accounting_Employee_NamedElement = Generalization(general=NamedElement, specific=accounting_Employee)
gen_accounting_Client_NamedElement = Generalization(general=NamedElement, specific=accounting_Client)
gen_accounting_Project_NamedElement = Generalization(general=NamedElement, specific=accounting_Project)

# Domain Model
domain_model = DomainModel(
    name="accounting",
    types={accounting_Project, accounting_Deliverable, accounting_Invoice, accounting_Employee, accounting_NamedElement, accounting_Order, accounting_ClientDatabase, accounting_EmployeeDatabase, accounting_Client, NamedElement, InvoiceState},
    associations={project0, deliverables1, invoices2, order4, advisor5, order6, clients15, employees16, projects8, client10, orders11, liason13},
    generalizations={gen_accounting_Employee_NamedElement, gen_accounting_Client_NamedElement, gen_accounting_Project_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)