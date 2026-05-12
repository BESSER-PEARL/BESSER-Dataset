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
Tourist_management_system_Component = Class(name="Tourist_management_system_Component")
T = Class(name="T")
Tourist_Actor = Class(name="Tourist_Actor")
Admin_Actor = Class(name="Admin_Actor")
Actor_Actor = Class(name="Actor_Actor")
Actor2_Actor = Class(name="Actor2_Actor")
Tourist_management_system2_Component = Class(name="Tourist_management_system2_Component")
T1 = Class(name="T1")
Log_in__Sign_up_external = Class(name="Log_in__Sign_up_external")
System_maintenance_external = Class(name="System_maintenance_external")
Request_package_external = Class(name="Request_package_external")
Give_description_external = Class(name="Give_description_external")
View_package_external = Class(name="View_package_external")
Log_in__log_out_external = Class(name="Log_in__log_out_external")
Verification_external = Class(name="Verification_external")
Manage_questions_external = Class(name="Manage_questions_external")
Update_member_profile_external = Class(name="Update_member_profile_external")
Book_package_external = Class(name="Book_package_external")

# Tourist_management_system_Component class attributes and methods

# T class attributes and methods

# Tourist_Actor class attributes and methods

# Admin_Actor class attributes and methods

# Actor_Actor class attributes and methods

# Actor2_Actor class attributes and methods

# Tourist_management_system2_Component class attributes and methods

# T1 class attributes and methods

# Log_in__Sign_up_external class attributes and methods

# System_maintenance_external class attributes and methods

# Request_package_external class attributes and methods

# Give_description_external class attributes and methods

# View_package_external class attributes and methods

# Log_in__log_out_external class attributes and methods

# Verification_external class attributes and methods

# Manage_questions_external class attributes and methods

# Update_member_profile_external class attributes and methods

# Book_package_external class attributes and methods

# Relationships
Librarian_Return_book: BinaryAssociation = BinaryAssociation(
    name="Librarian_Return_book",
    ends={
        Property(name="librarian13", type=Admin_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="return_book12", type=Manage_questions_external, multiplicity=Multiplicity(0, 1))
    }
)
Member_Inquiry_for_membership: BinaryAssociation = BinaryAssociation(
    name="Member_Inquiry_for_membership",
    ends={
        Property(name="inquiry_for_membership0", type=Log_in__Sign_up_external, multiplicity=Multiplicity(0, 1)),
        Property(name="member1", type=Tourist_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Member_Request_book: BinaryAssociation = BinaryAssociation(
    name="Member_Request_book",
    ends={
        Property(name="request_book2", type=Request_package_external, multiplicity=Multiplicity(0, 1)),
        Property(name="member3", type=Tourist_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Member_Request_book_return: BinaryAssociation = BinaryAssociation(
    name="Member_Request_book_return",
    ends={
        Property(name="request_book_return4", type=Give_description_external, multiplicity=Multiplicity(0, 1)),
        Property(name="member5", type=Tourist_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Member_Search_books: BinaryAssociation = BinaryAssociation(
    name="Member_Search_books",
    ends={
        Property(name="search_books6", type=View_package_external, multiplicity=Multiplicity(0, 1)),
        Property(name="member7", type=Tourist_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Librarian_Issue_member_card: BinaryAssociation = BinaryAssociation(
    name="Librarian_Issue_member_card",
    ends={
        Property(name="issue_member_card8", type=Log_in__log_out_external, multiplicity=Multiplicity(0, 1)),
        Property(name="librarian9", type=Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Librarian_Issue_book: BinaryAssociation = BinaryAssociation(
    name="Librarian_Issue_book",
    ends={
        Property(name="issue_book10", type=Verification_external, multiplicity=Multiplicity(0, 1)),
        Property(name="librarian11", type=Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Librarian_Update_member_profile: BinaryAssociation = BinaryAssociation(
    name="Librarian_Update_member_profile",
    ends={
        Property(name="update_member_profile14", type=System_maintenance_external, multiplicity=Multiplicity(0, 1)),
        Property(name="librarian15", type=Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Librarian_Maintain_book_in_records: BinaryAssociation = BinaryAssociation(
    name="Librarian_Maintain_book_in_records",
    ends={
        Property(name="maintain_book_in_records16", type=Update_member_profile_external, multiplicity=Multiplicity(0, 1)),
        Property(name="librarian17", type=Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Member_Cancel_membership: BinaryAssociation = BinaryAssociation(
    name="Member_Cancel_membership",
    ends={
        Property(name="cancel_membership18", type=Book_package_external, multiplicity=Multiplicity(0, 1)),
        Property(name="member19", type=Tourist_Actor, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="f55a5eeb_a140_4cf8_8638_56b0db3fe5ca",
    types={Tourist_management_system_Component, T, Tourist_Actor, Admin_Actor, Actor_Actor, Actor2_Actor, Tourist_management_system2_Component, T1, Log_in__Sign_up_external, System_maintenance_external, Request_package_external, Give_description_external, View_package_external, Log_in__log_out_external, Verification_external, Manage_questions_external, Update_member_profile_external, Book_package_external},
    associations={Librarian_Return_book, Member_Inquiry_for_membership, Member_Request_book, Member_Request_book_return, Member_Search_books, Librarian_Issue_member_card, Librarian_Issue_book, Librarian_Update_member_profile, Librarian_Maintain_book_in_records, Member_Cancel_membership},
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