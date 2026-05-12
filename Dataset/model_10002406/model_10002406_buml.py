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
Blue_Sea_Cruise_Booking_Cancellation_Component = Class(name="Blue_Sea_Cruise_Booking_Cancellation_Component")
T = Class(name="T")
Member_Actor = Class(name="Member_Actor")
Customer_Actor = Class(name="Customer_Actor")
Inquiry_for_membership_external = Class(name="Inquiry_for_membership_external")
Request_book_external = Class(name="Request_book_external")
Update_member_profile_external = Class(name="Update_member_profile_external")
Maintain_book_in_records_external = Class(name="Maintain_book_in_records_external")
Cancel_membership_external = Class(name="Cancel_membership_external")
Request_book_return_external = Class(name="Request_book_return_external")
Search_books_external = Class(name="Search_books_external")
Cruise_Booking_Email_phone_external = Class(name="Cruise_Booking_Email_phone_external")
Cruise_Booking_Walkin_external = Class(name="Cruise_Booking_Walkin_external")
mt_K7ZUTEeqqGZh46IEtXQ_external = Class(name="mt_K7ZUTEeqqGZh46IEtXQ_external")

# Blue_Sea_Cruise_Booking_Cancellation_Component class attributes and methods

# T class attributes and methods

# Member_Actor class attributes and methods

# Customer_Actor class attributes and methods

# Inquiry_for_membership_external class attributes and methods

# Request_book_external class attributes and methods

# Update_member_profile_external class attributes and methods

# Maintain_book_in_records_external class attributes and methods

# Cancel_membership_external class attributes and methods

# Request_book_return_external class attributes and methods

# Search_books_external class attributes and methods

# Cruise_Booking_Email_phone_external class attributes and methods

# Cruise_Booking_Walkin_external class attributes and methods

# mt_K7ZUTEeqqGZh46IEtXQ_external class attributes and methods

# Relationships
Member_Inquiry_for_membership: BinaryAssociation = BinaryAssociation(
    name="Member_Inquiry_for_membership",
    ends={
        Property(name="inquiry_for_membership0", type=Inquiry_for_membership_external, multiplicity=Multiplicity(0, 1)),
        Property(name="member1", type=Member_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Member_Request_book: BinaryAssociation = BinaryAssociation(
    name="Member_Request_book",
    ends={
        Property(name="request_book2", type=Request_book_external, multiplicity=Multiplicity(0, 1)),
        Property(name="member3", type=Member_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Librarian_Return_book: BinaryAssociation = BinaryAssociation(
    name="Librarian_Return_book",
    ends={
        Property(name="return_book12", type=mt_K7ZUTEeqqGZh46IEtXQ_external, multiplicity=Multiplicity(0, 1)),
        Property(name="librarian13", type=Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Librarian_Update_member_profile: BinaryAssociation = BinaryAssociation(
    name="Librarian_Update_member_profile",
    ends={
        Property(name="update_member_profile14", type=Update_member_profile_external, multiplicity=Multiplicity(0, 1)),
        Property(name="librarian15", type=Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Librarian_Maintain_book_in_records: BinaryAssociation = BinaryAssociation(
    name="Librarian_Maintain_book_in_records",
    ends={
        Property(name="maintain_book_in_records16", type=Maintain_book_in_records_external, multiplicity=Multiplicity(0, 1)),
        Property(name="librarian17", type=Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Member_Cancel_membership: BinaryAssociation = BinaryAssociation(
    name="Member_Cancel_membership",
    ends={
        Property(name="cancel_membership18", type=Cancel_membership_external, multiplicity=Multiplicity(0, 1)),
        Property(name="member19", type=Member_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Member_Request_book_return: BinaryAssociation = BinaryAssociation(
    name="Member_Request_book_return",
    ends={
        Property(name="request_book_return4", type=Request_book_return_external, multiplicity=Multiplicity(0, 1)),
        Property(name="member5", type=Member_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Member_Search_books: BinaryAssociation = BinaryAssociation(
    name="Member_Search_books",
    ends={
        Property(name="search_books6", type=Search_books_external, multiplicity=Multiplicity(0, 1)),
        Property(name="member7", type=Member_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Librarian_Issue_member_card: BinaryAssociation = BinaryAssociation(
    name="Librarian_Issue_member_card",
    ends={
        Property(name="issue_member_card8", type=Cruise_Booking_Email_phone_external, multiplicity=Multiplicity(0, 1)),
        Property(name="librarian9", type=Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Librarian_Issue_book: BinaryAssociation = BinaryAssociation(
    name="Librarian_Issue_book",
    ends={
        Property(name="issue_book10", type=Cruise_Booking_Walkin_external, multiplicity=Multiplicity(0, 1)),
        Property(name="librarian11", type=Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="afd5caf4_acc9_4bd9_b76b_747898d96b3c",
    types={Blue_Sea_Cruise_Booking_Cancellation_Component, T, Member_Actor, Customer_Actor, Inquiry_for_membership_external, Request_book_external, Update_member_profile_external, Maintain_book_in_records_external, Cancel_membership_external, Request_book_return_external, Search_books_external, Cruise_Booking_Email_phone_external, Cruise_Booking_Walkin_external, mt_K7ZUTEeqqGZh46IEtXQ_external},
    associations={Member_Inquiry_for_membership, Member_Request_book, Librarian_Return_book, Librarian_Update_member_profile, Librarian_Maintain_book_in_records, Member_Cancel_membership, Member_Request_book_return, Member_Search_books, Librarian_Issue_member_card, Librarian_Issue_book},
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