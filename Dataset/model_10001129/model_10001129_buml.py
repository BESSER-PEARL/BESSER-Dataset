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
Library_Management_Component = Class(name="Library_Management_Component")
T = Class(name="T")
COMPUTER_Actor = Class(name="COMPUTER_Actor")
PLAYER_Actor = Class(name="PLAYER_Actor")
choose_paper_external = Class(name="choose_paper_external")
choose_rock_external = Class(name="choose_rock_external")
choose_scissor_external = Class(name="choose_scissor_external")

# Library_Management_Component class attributes and methods

# T class attributes and methods

# COMPUTER_Actor class attributes and methods

# PLAYER_Actor class attributes and methods

# choose_paper_external class attributes and methods

# choose_rock_external class attributes and methods

# choose_scissor_external class attributes and methods

# Relationships
Member_Inquiry_for_membership: BinaryAssociation = BinaryAssociation(
    name="Member_Inquiry_for_membership",
    ends={
        Property(name="inquiry_for_membership0", type=choose_paper_external, multiplicity=Multiplicity(0, 1)),
        Property(name="member1", type=COMPUTER_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Member_Request_book: BinaryAssociation = BinaryAssociation(
    name="Member_Request_book",
    ends={
        Property(name="request_book2", type=choose_rock_external, multiplicity=Multiplicity(0, 1)),
        Property(name="member3", type=COMPUTER_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Member_Request_book_return: BinaryAssociation = BinaryAssociation(
    name="Member_Request_book_return",
    ends={
        Property(name="request_book_return4", type=choose_rock_external, multiplicity=Multiplicity(0, 1)),
        Property(name="member5", type=COMPUTER_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Member_Search_books: BinaryAssociation = BinaryAssociation(
    name="Member_Search_books",
    ends={
        Property(name="search_books6", type=choose_paper_external, multiplicity=Multiplicity(0, 1)),
        Property(name="member7", type=COMPUTER_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Librarian_Issue_member_card: BinaryAssociation = BinaryAssociation(
    name="Librarian_Issue_member_card",
    ends={
        Property(name="issue_member_card8", type=choose_scissor_external, multiplicity=Multiplicity(0, 1)),
        Property(name="librarian9", type=PLAYER_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Librarian_Issue_book: BinaryAssociation = BinaryAssociation(
    name="Librarian_Issue_book",
    ends={
        Property(name="issue_book10", type=choose_paper_external, multiplicity=Multiplicity(0, 1)),
        Property(name="librarian11", type=PLAYER_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Librarian_Return_book: BinaryAssociation = BinaryAssociation(
    name="Librarian_Return_book",
    ends={
        Property(name="return_book12", type=choose_scissor_external, multiplicity=Multiplicity(0, 1)),
        Property(name="librarian13", type=PLAYER_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Librarian_Update_member_profile: BinaryAssociation = BinaryAssociation(
    name="Librarian_Update_member_profile",
    ends={
        Property(name="update_member_profile14", type=choose_paper_external, multiplicity=Multiplicity(0, 1)),
        Property(name="librarian15", type=PLAYER_Actor, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_8969f5b4_f27c_41ba_9855_f0404a4d7ed6",
    types={Library_Management_Component, T, COMPUTER_Actor, PLAYER_Actor, choose_paper_external, choose_rock_external, choose_scissor_external},
    associations={Member_Inquiry_for_membership, Member_Request_book, Member_Request_book_return, Member_Search_books, Librarian_Issue_member_card, Librarian_Issue_book, Librarian_Return_book, Librarian_Update_member_profile},
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