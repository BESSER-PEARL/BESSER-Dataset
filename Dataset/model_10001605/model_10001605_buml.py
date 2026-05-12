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
Cancel_Membership_UseCase = Class(name="Cancel_Membership_UseCase")
Suspend_Membership_UseCase = Class(name="Suspend_Membership_UseCase")
Amend_Membership_details_UseCase = Class(name="Amend_Membership_details_UseCase")
Chief_Librarian_Actor = Class(name="Chief_Librarian_Actor")
Charge_fine_for_Late_Book_UseCase = Class(name="Charge_fine_for_Late_Book_UseCase")
Collect_Fine_UseCase = Class(name="Collect_Fine_UseCase")
Purchase_Books_UseCase = Class(name="Purchase_Books_UseCase")
Withdraw_Books_UseCase = Class(name="Withdraw_Books_UseCase")
Carry_Out_Stock_Check_UseCase = Class(name="Carry_Out_Stock_Check_UseCase")
Books = Class(name="Books")
Library_Members = Class(name="Library_Members")
Reservations = Class(name="Reservations")
Checkout_Librarian_Actor = Class(name="Checkout_Librarian_Actor")
Issue_Book_UseCase = Class(name="Issue_Book_UseCase")
Return_Item_UseCase = Class(name="Return_Item_UseCase")
Make_Reservation_UseCase = Class(name="Make_Reservation_UseCase")
Inform_Memeber_when_Item_Available_UseCase = Class(name="Inform_Memeber_when_Item_Available_UseCase")
Head_Librarian_Actor = Class(name="Head_Librarian_Actor")
Create_New_Member_UseCase = Class(name="Create_New_Member_UseCase")

# Cancel_Membership_UseCase class attributes and methods

# Suspend_Membership_UseCase class attributes and methods

# Amend_Membership_details_UseCase class attributes and methods

# Chief_Librarian_Actor class attributes and methods

# Charge_fine_for_Late_Book_UseCase class attributes and methods

# Collect_Fine_UseCase class attributes and methods

# Purchase_Books_UseCase class attributes and methods

# Withdraw_Books_UseCase class attributes and methods

# Carry_Out_Stock_Check_UseCase class attributes and methods

# Books class attributes and methods
Books_Title: Property = Property(name="Title", type=StringType)
Books.attributes={Books_Title}

# Library_Members class attributes and methods
Library_Members_Name: Property = Property(name="Name", type=StringType)
Library_Members.attributes={Library_Members_Name}

# Reservations class attributes and methods

# Checkout_Librarian_Actor class attributes and methods

# Issue_Book_UseCase class attributes and methods

# Return_Item_UseCase class attributes and methods

# Make_Reservation_UseCase class attributes and methods

# Inform_Memeber_when_Item_Available_UseCase class attributes and methods

# Head_Librarian_Actor class attributes and methods

# Create_New_Member_UseCase class attributes and methods

# Relationships
Checkout_Librarian_Issue_Book: BinaryAssociation = BinaryAssociation(
    name="Checkout_Librarian_Issue_Book",
    ends={
        Property(name="issue_Book0", type=Issue_Book_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="checkout_Librarian1", type=Checkout_Librarian_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Checkout_Librarian_Return_Item: BinaryAssociation = BinaryAssociation(
    name="Checkout_Librarian_Return_Item",
    ends={
        Property(name="return_Item2", type=Return_Item_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="checkout_Librarian3", type=Checkout_Librarian_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Checkout_Librarian_Make_Reservation: BinaryAssociation = BinaryAssociation(
    name="Checkout_Librarian_Make_Reservation",
    ends={
        Property(name="make_Reservation4", type=Make_Reservation_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="checkout_Librarian5", type=Checkout_Librarian_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Checkout_Librarian_Inform_Memeber_when_Item_Available: BinaryAssociation = BinaryAssociation(
    name="Checkout_Librarian_Inform_Memeber_when_Item_Available",
    ends={
        Property(name="inform_Memeber_when_Item_Available6", type=Inform_Memeber_when_Item_Available_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="checkout_Librarian7", type=Checkout_Librarian_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Head_Librarian_Create_New_Member: BinaryAssociation = BinaryAssociation(
    name="Head_Librarian_Create_New_Member",
    ends={
        Property(name="create_New_Member8", type=Create_New_Member_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="head_Librarian9", type=Head_Librarian_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Head_Librarian_Cancel_Membership: BinaryAssociation = BinaryAssociation(
    name="Head_Librarian_Cancel_Membership",
    ends={
        Property(name="cancel_Membership10", type=Cancel_Membership_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="head_Librarian11", type=Head_Librarian_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Head_Librarian_Suspend_Membership: BinaryAssociation = BinaryAssociation(
    name="Head_Librarian_Suspend_Membership",
    ends={
        Property(name="suspend_Membership12", type=Suspend_Membership_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="head_Librarian13", type=Head_Librarian_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Head_Librarian_Amend_Membership_details: BinaryAssociation = BinaryAssociation(
    name="Head_Librarian_Amend_Membership_details",
    ends={
        Property(name="amend_Membership_details14", type=Amend_Membership_details_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="head_Librarian15", type=Head_Librarian_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Chief_Librarian_Charge_fine_for_Late_Book: BinaryAssociation = BinaryAssociation(
    name="Chief_Librarian_Charge_fine_for_Late_Book",
    ends={
        Property(name="charge_fine_for_Late_Book16", type=Charge_fine_for_Late_Book_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="chief_Librarian17", type=Chief_Librarian_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Chief_Librarian_Collect_Fine: BinaryAssociation = BinaryAssociation(
    name="Chief_Librarian_Collect_Fine",
    ends={
        Property(name="collect_Fine18", type=Collect_Fine_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="chief_Librarian19", type=Chief_Librarian_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Chief_Librarian_Purchase_Books: BinaryAssociation = BinaryAssociation(
    name="Chief_Librarian_Purchase_Books",
    ends={
        Property(name="purchase_Books20", type=Purchase_Books_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="chief_Librarian21", type=Chief_Librarian_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Head_Librarian_Purchase_Books: BinaryAssociation = BinaryAssociation(
    name="Head_Librarian_Purchase_Books",
    ends={
        Property(name="purchase_Books22", type=Purchase_Books_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="head_Librarian23", type=Head_Librarian_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Chief_Librarian_Withdraw_Books: BinaryAssociation = BinaryAssociation(
    name="Chief_Librarian_Withdraw_Books",
    ends={
        Property(name="withdraw_Books24", type=Withdraw_Books_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="chief_Librarian25", type=Chief_Librarian_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Head_Librarian_Withdraw_Books: BinaryAssociation = BinaryAssociation(
    name="Head_Librarian_Withdraw_Books",
    ends={
        Property(name="withdraw_Books26", type=Withdraw_Books_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="head_Librarian27", type=Head_Librarian_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Chief_Librarian_Carry_Out_Stock_Check: BinaryAssociation = BinaryAssociation(
    name="Chief_Librarian_Carry_Out_Stock_Check",
    ends={
        Property(name="carry_Out_Stock_Check28", type=Carry_Out_Stock_Check_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="chief_Librarian29", type=Chief_Librarian_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Head_Librarian_Carry_Out_Stock_Check: BinaryAssociation = BinaryAssociation(
    name="Head_Librarian_Carry_Out_Stock_Check",
    ends={
        Property(name="carry_Out_Stock_Check30", type=Carry_Out_Stock_Check_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="head_Librarian31", type=Head_Librarian_Actor, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_IxKZgNH_Eeib2vfQ4l86Yg",
    types={Cancel_Membership_UseCase, Suspend_Membership_UseCase, Amend_Membership_details_UseCase, Chief_Librarian_Actor, Charge_fine_for_Late_Book_UseCase, Collect_Fine_UseCase, Purchase_Books_UseCase, Withdraw_Books_UseCase, Carry_Out_Stock_Check_UseCase, Books, Library_Members, Reservations, Checkout_Librarian_Actor, Issue_Book_UseCase, Return_Item_UseCase, Make_Reservation_UseCase, Inform_Memeber_when_Item_Available_UseCase, Head_Librarian_Actor, Create_New_Member_UseCase},
    associations={Checkout_Librarian_Issue_Book, Checkout_Librarian_Return_Item, Checkout_Librarian_Make_Reservation, Checkout_Librarian_Inform_Memeber_when_Item_Available, Head_Librarian_Create_New_Member, Head_Librarian_Cancel_Membership, Head_Librarian_Suspend_Membership, Head_Librarian_Amend_Membership_details, Chief_Librarian_Charge_fine_for_Late_Book, Chief_Librarian_Collect_Fine, Chief_Librarian_Purchase_Books, Head_Librarian_Purchase_Books, Chief_Librarian_Withdraw_Books, Head_Librarian_Withdraw_Books, Chief_Librarian_Carry_Out_Stock_Check, Head_Librarian_Carry_Out_Stock_Check},
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