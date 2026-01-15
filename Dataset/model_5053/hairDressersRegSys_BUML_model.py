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
hairDressersRegSys_Service = Class(name="hairDressersRegSys::Service")
hairDressersRegSys_Discounts = Class(name="hairDressersRegSys::Discounts")
hairDressersRegSys_Payment = Class(name="hairDressersRegSys::Payment")
hairDressersRegSys_Customer = Class(name="hairDressersRegSys::Customer")
hairDressersRegSys_Appointment = Class(name="hairDressersRegSys::Appointment")
hairDressersRegSys_Invoice = Class(name="hairDressersRegSys::Invoice")
hairDressersRegSys_Products = Class(name="hairDressersRegSys::Products")
hairDressersRegSys_Person = Class(name="hairDressersRegSys::Person")
hairDressersRegSys_Styling = Class(name="hairDressersRegSys::Styling")
Service = Class(name="Service")
hairDressersRegSys_Haircuts = Class(name="hairDressersRegSys::Haircuts")
hairDressersRegSys_Other = Class(name="hairDressersRegSys::Other")
Person = Class(name="Person")
hairDressersRegSys_ServiceEmployee = Class(name="hairDressersRegSys::ServiceEmployee")

# hairDressersRegSys_Service class attributes and methods
hairDressersRegSys_Service_Name: Property = Property(name="Name", type=StringType)
hairDressersRegSys_Service_Description: Property = Property(name="Description", type=StringType)
hairDressersRegSys_Service_CostPerHour: Property = Property(name="CostPerHour", type=StringType)
hairDressersRegSys_Service_Time: Property = Property(name="Time", type=DateType)
hairDressersRegSys_Service_m_AddService: Method = Method(name="AddService", parameters={})
hairDressersRegSys_Service_m_RemoveService: Method = Method(name="RemoveService", parameters={})
hairDressersRegSys_Service_m_ViewAllServices: Method = Method(name="ViewAllServices", parameters={})
hairDressersRegSys_Service.attributes={hairDressersRegSys_Service_Name, hairDressersRegSys_Service_Time, hairDressersRegSys_Service_Description, hairDressersRegSys_Service_CostPerHour}
hairDressersRegSys_Service.methods={hairDressersRegSys_Service_m_RemoveService, hairDressersRegSys_Service_m_AddService, hairDressersRegSys_Service_m_ViewAllServices}

# hairDressersRegSys_Discounts class attributes and methods
hairDressersRegSys_Discounts_Name: Property = Property(name="Name", type=StringType)
hairDressersRegSys_Discounts_Description: Property = Property(name="Description", type=StringType)
hairDressersRegSys_Discounts_Percentage: Property = Property(name="Percentage", type=IntegerType)
hairDressersRegSys_Discounts.attributes={hairDressersRegSys_Discounts_Percentage, hairDressersRegSys_Discounts_Name, hairDressersRegSys_Discounts_Description}

# hairDressersRegSys_Payment class attributes and methods
hairDressersRegSys_Payment_PaymentMethod: Property = Property(name="PaymentMethod", type=StringType)
hairDressersRegSys_Payment_Date: Property = Property(name="Date", type=DateType)
hairDressersRegSys_Payment_AmountPaid: Property = Property(name="AmountPaid", type=StringType)
hairDressersRegSys_Payment_m_MakePayment: Method = Method(name="MakePayment", parameters={})
hairDressersRegSys_Payment.attributes={hairDressersRegSys_Payment_Date, hairDressersRegSys_Payment_AmountPaid, hairDressersRegSys_Payment_PaymentMethod}
hairDressersRegSys_Payment.methods={hairDressersRegSys_Payment_m_MakePayment}

# hairDressersRegSys_Customer class attributes and methods
hairDressersRegSys_Customer_CustomerId: Property = Property(name="CustomerId", type=IntegerType)
hairDressersRegSys_Customer_m_PlaceAppointment: Method = Method(name="PlaceAppointment", parameters={})
hairDressersRegSys_Customer_m_AddNewCustomer: Method = Method(name="AddNewCustomer", parameters={})
hairDressersRegSys_Customer.attributes={hairDressersRegSys_Customer_CustomerId}
hairDressersRegSys_Customer.methods={hairDressersRegSys_Customer_m_PlaceAppointment, hairDressersRegSys_Customer_m_AddNewCustomer}

# hairDressersRegSys_Appointment class attributes and methods
hairDressersRegSys_Appointment_Date: Property = Property(name="Date", type=DateType)
hairDressersRegSys_Appointment_StartTime: Property = Property(name="StartTime", type=DateType)
hairDressersRegSys_Appointment_EndTime: Property = Property(name="EndTime", type=DateType)
hairDressersRegSys_Appointment_m_ViewSchedule: Method = Method(name="ViewSchedule", parameters={})
hairDressersRegSys_Appointment_m_AddAppointment: Method = Method(name="AddAppointment", parameters={})
hairDressersRegSys_Appointment.attributes={hairDressersRegSys_Appointment_EndTime, hairDressersRegSys_Appointment_Date, hairDressersRegSys_Appointment_StartTime}
hairDressersRegSys_Appointment.methods={hairDressersRegSys_Appointment_m_AddAppointment, hairDressersRegSys_Appointment_m_ViewSchedule}

# hairDressersRegSys_Invoice class attributes and methods
hairDressersRegSys_Invoice_Date: Property = Property(name="Date", type=StringType)
hairDressersRegSys_Invoice_InvoiceNumber: Property = Property(name="InvoiceNumber", type=IntegerType)
hairDressersRegSys_Invoice_Total: Property = Property(name="Total", type=StringType)
hairDressersRegSys_Invoice_m_CalculateTotal: Method = Method(name="CalculateTotal", parameters={})
hairDressersRegSys_Invoice_m_GetDiscount: Method = Method(name="GetDiscount", parameters={})
hairDressersRegSys_Invoice.attributes={hairDressersRegSys_Invoice_InvoiceNumber, hairDressersRegSys_Invoice_Total, hairDressersRegSys_Invoice_Date}
hairDressersRegSys_Invoice.methods={hairDressersRegSys_Invoice_m_CalculateTotal, hairDressersRegSys_Invoice_m_GetDiscount}

# hairDressersRegSys_Products class attributes and methods
hairDressersRegSys_Products_Name: Property = Property(name="Name", type=StringType)
hairDressersRegSys_Products_Description: Property = Property(name="Description", type=StringType)
hairDressersRegSys_Products_Price: Property = Property(name="Price", type=StringType)
hairDressersRegSys_Products_m_AddProduct: Method = Method(name="AddProduct", parameters={})
hairDressersRegSys_Products_m_ViewTotalStock: Method = Method(name="ViewTotalStock", parameters={})
hairDressersRegSys_Products.attributes={hairDressersRegSys_Products_Description, hairDressersRegSys_Products_Name, hairDressersRegSys_Products_Price}
hairDressersRegSys_Products.methods={hairDressersRegSys_Products_m_ViewTotalStock, hairDressersRegSys_Products_m_AddProduct}

# hairDressersRegSys_Person class attributes and methods
hairDressersRegSys_Person_FirstName: Property = Property(name="FirstName", type=StringType)
hairDressersRegSys_Person_LastName: Property = Property(name="LastName", type=StringType)
hairDressersRegSys_Person_Address: Property = Property(name="Address", type=StringType)
hairDressersRegSys_Person_DateOfBirth: Property = Property(name="DateOfBirth", type=DateType)
hairDressersRegSys_Person_m_GetAge: Method = Method(name="GetAge", parameters={}, type=IntegerType)
hairDressersRegSys_Person.attributes={hairDressersRegSys_Person_FirstName, hairDressersRegSys_Person_LastName, hairDressersRegSys_Person_DateOfBirth, hairDressersRegSys_Person_Address}
hairDressersRegSys_Person.methods={hairDressersRegSys_Person_m_GetAge}

# hairDressersRegSys_Styling class attributes and methods
hairDressersRegSys_Styling_IsWash: Property = Property(name="IsWash", type=BooleanType)
hairDressersRegSys_Styling.attributes={hairDressersRegSys_Styling_IsWash}

# Service class attributes and methods

# hairDressersRegSys_Haircuts class attributes and methods
hairDressersRegSys_Haircuts_IsWash: Property = Property(name="IsWash", type=BooleanType)
hairDressersRegSys_Haircuts_IsShave: Property = Property(name="IsShave", type=BooleanType)
hairDressersRegSys_Haircuts_IsCut: Property = Property(name="IsCut", type=BooleanType)
hairDressersRegSys_Haircuts.attributes={hairDressersRegSys_Haircuts_IsCut, hairDressersRegSys_Haircuts_IsShave, hairDressersRegSys_Haircuts_IsWash}

# hairDressersRegSys_Other class attributes and methods
hairDressersRegSys_Other_AdditionalInformation: Property = Property(name="AdditionalInformation", type=StringType)
hairDressersRegSys_Other.attributes={hairDressersRegSys_Other_AdditionalInformation}

# Person class attributes and methods

# hairDressersRegSys_ServiceEmployee class attributes and methods
hairDressersRegSys_ServiceEmployee_Role: Property = Property(name="Role", type=StringType)
hairDressersRegSys_ServiceEmployee_EmployeeId: Property = Property(name="EmployeeId", type=IntegerType)
hairDressersRegSys_ServiceEmployee_m_RemoveAppointment: Method = Method(name="RemoveAppointment", parameters={})
hairDressersRegSys_ServiceEmployee_m_MakeAppointment: Method = Method(name="MakeAppointment", parameters={})
hairDressersRegSys_ServiceEmployee_m_AddNewEmployee: Method = Method(name="AddNewEmployee", parameters={})
hairDressersRegSys_ServiceEmployee_m_ViewAllAvailableEmployees: Method = Method(name="ViewAllAvailableEmployees", parameters={})
hairDressersRegSys_ServiceEmployee_m_ViewAppointments: Method = Method(name="ViewAppointments", parameters={})
hairDressersRegSys_ServiceEmployee.attributes={hairDressersRegSys_ServiceEmployee_Role, hairDressersRegSys_ServiceEmployee_EmployeeId}
hairDressersRegSys_ServiceEmployee.methods={hairDressersRegSys_ServiceEmployee_m_ViewAppointments, hairDressersRegSys_ServiceEmployee_m_MakeAppointment, hairDressersRegSys_ServiceEmployee_m_RemoveAppointment, hairDressersRegSys_ServiceEmployee_m_ViewAllAvailableEmployees, hairDressersRegSys_ServiceEmployee_m_AddNewEmployee}

# Relationships
products4: BinaryAssociation = BinaryAssociation(
    name="products4",
    ends={
        Property(name="Products", type=hairDressersRegSys_Invoice, multiplicity=Multiplicity(1, 1)),
        Property(name="invoice", type=hairDressersRegSys_Products, multiplicity=Multiplicity(0, 1))
    }
)
discounts5: BinaryAssociation = BinaryAssociation(
    name="discounts5",
    ends={
        Property(name="Discounts", type=hairDressersRegSys_Invoice, multiplicity=Multiplicity(1, 1)),
        Property(name="invoice6", type=hairDressersRegSys_Discounts, multiplicity=Multiplicity(0, 1))
    }
)
payment7: BinaryAssociation = BinaryAssociation(
    name="payment7",
    ends={
        Property(name="Payment", type=hairDressersRegSys_Invoice, multiplicity=Multiplicity(1, 1)),
        Property(name="invoice8", type=hairDressersRegSys_Payment, multiplicity=Multiplicity(0, 1))
    }
)
customer9: BinaryAssociation = BinaryAssociation(
    name="customer9",
    ends={
        Property(name="Customer", type=hairDressersRegSys_Discounts, multiplicity=Multiplicity(1, 1)),
        Property(name="discounts", type=hairDressersRegSys_Customer, multiplicity=Multiplicity(0, 9999))
    }
)
invoice10: BinaryAssociation = BinaryAssociation(
    name="invoice10",
    ends={
        Property(name="Invoice12", type=hairDressersRegSys_Discounts, multiplicity=Multiplicity(1, 1)),
        Property(name="discounts11", type=hairDressersRegSys_Invoice, multiplicity=Multiplicity(0, 9999))
    }
)
appointment0: BinaryAssociation = BinaryAssociation(
    name="appointment0",
    ends={
        Property(name="hairDressersRegSys_Appointment", type=hairDressersRegSys_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="hairDressersRegSys_Service", type=hairDressersRegSys_Appointment, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
invoice1: BinaryAssociation = BinaryAssociation(
    name="invoice1",
    ends={
        Property(name="hairDressersRegSys_Invoice", type=hairDressersRegSys_Appointment, multiplicity=Multiplicity(1, 1)),
        Property(name="hairDressersRegSys_Appointment2", type=hairDressersRegSys_Invoice, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
invoice3: BinaryAssociation = BinaryAssociation(
    name="invoice3",
    ends={
        Property(name="Invoice", type=hairDressersRegSys_Products, multiplicity=Multiplicity(1, 1)),
        Property(name="products", type=hairDressersRegSys_Invoice, multiplicity=Multiplicity(0, 1))
    }
)
appointment17: BinaryAssociation = BinaryAssociation(
    name="appointment17",
    ends={
        Property(name="hairDressersRegSys_Appointment18", type=hairDressersRegSys_ServiceEmployee, multiplicity=Multiplicity(1, 1)),
        Property(name="hairDressersRegSys_ServiceEmployee", type=hairDressersRegSys_Appointment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
invoice19: BinaryAssociation = BinaryAssociation(
    name="invoice19",
    ends={
        Property(name="Invoice20", type=hairDressersRegSys_Payment, multiplicity=Multiplicity(1, 1)),
        Property(name="payment", type=hairDressersRegSys_Invoice, multiplicity=Multiplicity(1, 9999))
    }
)
appointment13: BinaryAssociation = BinaryAssociation(
    name="appointment13",
    ends={
        Property(name="hairDressersRegSys_Appointment14", type=hairDressersRegSys_Customer, multiplicity=Multiplicity(1, 1)),
        Property(name="hairDressersRegSys_Customer", type=hairDressersRegSys_Appointment, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
discounts15: BinaryAssociation = BinaryAssociation(
    name="discounts15",
    ends={
        Property(name="Discounts16", type=hairDressersRegSys_Customer, multiplicity=Multiplicity(1, 1)),
        Property(name="customer", type=hairDressersRegSys_Discounts, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_hairDressersRegSys_Styling_Service = Generalization(general=Service, specific=hairDressersRegSys_Styling)
gen_hairDressersRegSys_Haircuts_Service = Generalization(general=Service, specific=hairDressersRegSys_Haircuts)
gen_hairDressersRegSys_Other_Service = Generalization(general=Service, specific=hairDressersRegSys_Other)
gen_hairDressersRegSys_Customer_Person = Generalization(general=Person, specific=hairDressersRegSys_Customer)
gen_hairDressersRegSys_ServiceEmployee_Person = Generalization(general=Person, specific=hairDressersRegSys_ServiceEmployee)

# Domain Model
domain_model = DomainModel(
    name="hairDressersRegSys",
    types={hairDressersRegSys_Service, hairDressersRegSys_Discounts, hairDressersRegSys_Payment, hairDressersRegSys_Customer, hairDressersRegSys_Appointment, hairDressersRegSys_Invoice, hairDressersRegSys_Products, hairDressersRegSys_Person, hairDressersRegSys_Styling, Service, hairDressersRegSys_Haircuts, hairDressersRegSys_Other, Person, hairDressersRegSys_ServiceEmployee},
    associations={products4, discounts5, payment7, customer9, invoice10, appointment0, invoice1, invoice3, appointment17, invoice19, appointment13, discounts15},
    generalizations={gen_hairDressersRegSys_Styling_Service, gen_hairDressersRegSys_Haircuts_Service, gen_hairDressersRegSys_Other_Service, gen_hairDressersRegSys_Customer_Person, gen_hairDressersRegSys_ServiceEmployee_Person},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)