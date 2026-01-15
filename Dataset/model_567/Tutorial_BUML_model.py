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
tutorial_Library = Class(name="tutorial::Library")
tutorial_Book = Class(name="tutorial::Book")
tutorial_Loan = Class(name="tutorial::Loan")
tutorial_Member = Class(name="tutorial::Member")

# tutorial_Library class attributes and methods
tutorial_Library_name: Property = Property(name="name", type=BooleanType)
tutorial_Library.attributes={tutorial_Library_name}

# tutorial_Book class attributes and methods
tutorial_Book_name: Property = Property(name="name", type=StringType)
tutorial_Book_copies: Property = Property(name="copies", type=StringType)
tutorial_Book_m_isAvailable: Method = Method(name="isAvailable", parameters={})
tutorial_Book.attributes={tutorial_Book_name, tutorial_Book_copies}
tutorial_Book.methods={tutorial_Book_m_isAvailable}

# tutorial_Loan class attributes and methods
tutorial_Loan_date: Property = Property(name="date", type=DateType)
tutorial_Loan.attributes={tutorial_Loan_date}

# tutorial_Member class attributes and methods
tutorial_Member_name: Property = Property(name="name", type=StringType)
tutorial_Member.attributes={tutorial_Member_name}

# Relationships
library6: BinaryAssociation = BinaryAssociation(
    name="library6",
    ends={
        Property(name="8", type=tutorial_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="7", type=tutorial_Library, multiplicity=Multiplicity(0, 1))
    }
)
loans9: BinaryAssociation = BinaryAssociation(
    name="loans9",
    ends={
        Property(name="tutorial_Loan10", type=tutorial_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="tutorial_Book", type=tutorial_Loan, multiplicity=Multiplicity(0, 9999))
    }
)
library11: BinaryAssociation = BinaryAssociation(
    name="library11",
    ends={
        Property(name="13", type=tutorial_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="12", type=tutorial_Library, multiplicity=Multiplicity(0, 1))
    }
)
books0: BinaryAssociation = BinaryAssociation(
    name="books0",
    ends={
        Property(name="1", type=tutorial_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="", type=tutorial_Book, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
loans2: BinaryAssociation = BinaryAssociation(
    name="loans2",
    ends={
        Property(name="tutorial_Loan", type=tutorial_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="tutorial_Library", type=tutorial_Loan, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
members3: BinaryAssociation = BinaryAssociation(
    name="members3",
    ends={
        Property(name="5", type=tutorial_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="4", type=tutorial_Member, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
member22: BinaryAssociation = BinaryAssociation(
    name="member22",
    ends={
        Property(name="tutorial_Member24", type=tutorial_Loan, multiplicity=Multiplicity(1, 1)),
        Property(name="tutorial_Loan23", type=tutorial_Member, multiplicity=Multiplicity(1, 1))
    }
)
loans14: BinaryAssociation = BinaryAssociation(
    name="loans14",
    ends={
        Property(name="tutorial_Loan15", type=tutorial_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="tutorial_Member", type=tutorial_Loan, multiplicity=Multiplicity(0, 9999))
    }
)
books16: BinaryAssociation = BinaryAssociation(
    name="books16",
    ends={
        Property(name="tutorial_Book18", type=tutorial_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="tutorial_Member17", type=tutorial_Book, multiplicity=Multiplicity(0, 9999))
    }
)
book19: BinaryAssociation = BinaryAssociation(
    name="book19",
    ends={
        Property(name="tutorial_Book21", type=tutorial_Loan, multiplicity=Multiplicity(1, 1)),
        Property(name="tutorial_Loan20", type=tutorial_Book, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="tutorial",
    types={tutorial_Library, tutorial_Book, tutorial_Loan, tutorial_Member},
    associations={library6, loans9, library11, books0, loans2, members3, member22, loans14, books16, book19},
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