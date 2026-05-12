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
Check_In_Item_external = Class(name="Check_In_Item_external")
Request_Book_external = Class(name="Request_Book_external")
Check_Out_Item_external = Class(name="Check_Out_Item_external")
Reserve_Book_For_Semester_external = Class(name="Reserve_Book_For_Semester_external")
Manage_Reference_Materials_external = Class(name="Manage_Reference_Materials_external")
Organize_Books_external = Class(name="Organize_Books_external")
Renew_Magazine_Subscriptions_external = Class(name="Renew_Magazine_Subscriptions_external")
Order_New_Resources_external = Class(name="Order_New_Resources_external")
Extended_Checkout_external = Class(name="Extended_Checkout_external")
Manage_Computer_Terminals_external = Class(name="Manage_Computer_Terminals_external")
Patron_Actor = Class(name="Patron_Actor")
Student_Actor = Class(name="Student_Actor")
Library_Management_Component = Class(name="Library_Management_Component")
Faculty_Actor = Class(name="Faculty_Actor")
Library_Staff_Actor = Class(name="Library_Staff_Actor")
Patron = Class(name="Patron")
Student = Class(name="Student")
Faculty = Class(name="Faculty")

# Check_In_Item_external class attributes and methods

# Request_Book_external class attributes and methods

# Check_Out_Item_external class attributes and methods

# Reserve_Book_For_Semester_external class attributes and methods

# Manage_Reference_Materials_external class attributes and methods

# Organize_Books_external class attributes and methods

# Renew_Magazine_Subscriptions_external class attributes and methods

# Order_New_Resources_external class attributes and methods

# Extended_Checkout_external class attributes and methods

# Manage_Computer_Terminals_external class attributes and methods

# Patron_Actor class attributes and methods

# Student_Actor class attributes and methods

# Library_Management_Component class attributes and methods

# Faculty_Actor class attributes and methods

# Library_Staff_Actor class attributes and methods

# Patron class attributes and methods
Patron_isMember: Property = Property(name="isMember", type=BooleanType)
Patron.attributes={Patron_isMember}

# Student class attributes and methods

# Faculty class attributes and methods

# Relationships
Patron_Check_In_Books: BinaryAssociation = BinaryAssociation(
    name="Patron_Check_In_Books",
    ends={
        Property(name="check_In_Books0", type=Check_In_Item_external, multiplicity=Multiplicity(0, 1)),
        Property(name="patron1", type=Patron_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Patron_Request_Book: BinaryAssociation = BinaryAssociation(
    name="Patron_Request_Book",
    ends={
        Property(name="request_Book2", type=Request_Book_external, multiplicity=Multiplicity(0, 1)),
        Property(name="patron3", type=Patron_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Patron_Check_Out_Books: BinaryAssociation = BinaryAssociation(
    name="Patron_Check_Out_Books",
    ends={
        Property(name="check_Out_Books4", type=Check_Out_Item_external, multiplicity=Multiplicity(0, 1)),
        Property(name="patron5", type=Patron_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Library_Staff_Reserve_Book_For_Semester: BinaryAssociation = BinaryAssociation(
    name="Library_Staff_Reserve_Book_For_Semester",
    ends={
        Property(name="reserve_Book_For_Semester6", type=Reserve_Book_For_Semester_external, multiplicity=Multiplicity(0, 1)),
        Property(name="library_Staff7", type=Library_Staff_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Faculty_Reserve_Book_For_Semester: BinaryAssociation = BinaryAssociation(
    name="Faculty_Reserve_Book_For_Semester",
    ends={
        Property(name="reserve_Book_For_Semester8", type=Reserve_Book_For_Semester_external, multiplicity=Multiplicity(0, 1)),
        Property(name="faculty9", type=Faculty_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Library_Staff_Manage_Reference_Materirals: BinaryAssociation = BinaryAssociation(
    name="Library_Staff_Manage_Reference_Materirals",
    ends={
        Property(name="manage_Reference_Materirals10", type=Manage_Reference_Materials_external, multiplicity=Multiplicity(0, 1)),
        Property(name="library_Staff11", type=Library_Staff_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Library_Staff_Organize_Books: BinaryAssociation = BinaryAssociation(
    name="Library_Staff_Organize_Books",
    ends={
        Property(name="organize_Books12", type=Organize_Books_external, multiplicity=Multiplicity(0, 1)),
        Property(name="library_Staff13", type=Library_Staff_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Library_Staff_Renew_Magazine_Subscriptions: BinaryAssociation = BinaryAssociation(
    name="Library_Staff_Renew_Magazine_Subscriptions",
    ends={
        Property(name="renew_Magazine_Subscriptions14", type=Renew_Magazine_Subscriptions_external, multiplicity=Multiplicity(0, 1)),
        Property(name="library_Staff15", type=Library_Staff_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Library_Staff_Order_New_Resources: BinaryAssociation = BinaryAssociation(
    name="Library_Staff_Order_New_Resources",
    ends={
        Property(name="order_New_Resources16", type=Order_New_Resources_external, multiplicity=Multiplicity(0, 1)),
        Property(name="library_Staff17", type=Library_Staff_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Student_Extended_Checkout: BinaryAssociation = BinaryAssociation(
    name="Student_Extended_Checkout",
    ends={
        Property(name="extended_Checkout18", type=Extended_Checkout_external, multiplicity=Multiplicity(0, 1)),
        Property(name="student19", type=Student_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Faculty_Extended_Checkout: BinaryAssociation = BinaryAssociation(
    name="Faculty_Extended_Checkout",
    ends={
        Property(name="extended_Checkout20", type=Extended_Checkout_external, multiplicity=Multiplicity(0, 1)),
        Property(name="faculty21", type=Faculty_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Library_Staff_Manage_Computer_Terminals: BinaryAssociation = BinaryAssociation(
    name="Library_Staff_Manage_Computer_Terminals",
    ends={
        Property(name="manage_Computer_Terminals22", type=Manage_Computer_Terminals_external, multiplicity=Multiplicity(0, 1)),
        Property(name="library_Staff23", type=Library_Staff_Actor, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_b4Mf4MNvEeeWu_SLkciAbg",
    types={Check_In_Item_external, Request_Book_external, Check_Out_Item_external, Reserve_Book_For_Semester_external, Manage_Reference_Materials_external, Organize_Books_external, Renew_Magazine_Subscriptions_external, Order_New_Resources_external, Extended_Checkout_external, Manage_Computer_Terminals_external, Patron_Actor, Student_Actor, Library_Management_Component, Faculty_Actor, Library_Staff_Actor, Patron, Student, Faculty},
    associations={Patron_Check_In_Books, Patron_Request_Book, Patron_Check_Out_Books, Library_Staff_Reserve_Book_For_Semester, Faculty_Reserve_Book_For_Semester, Library_Staff_Manage_Reference_Materirals, Library_Staff_Organize_Books, Library_Staff_Renew_Magazine_Subscriptions, Library_Staff_Order_New_Resources, Student_Extended_Checkout, Faculty_Extended_Checkout, Library_Staff_Manage_Computer_Terminals},
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