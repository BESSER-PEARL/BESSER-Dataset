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
tutorial_Loan = Class(name="tutorial::Loan")
tutorial_Member = Class(name="tutorial::Member")
tutorial_Library = Class(name="tutorial::Library")
tutorial_Book = Class(name="tutorial::Book")

# tutorial_Loan class attributes and methods
tutorial_Loan_date: Property = Property(name="date", type=DateType)
tutorial_Loan.attributes={tutorial_Loan_date}

# tutorial_Member class attributes and methods
tutorial_Member_name: Property = Property(name="name", type=StringType)
tutorial_Member.attributes={tutorial_Member_name}

# tutorial_Library class attributes and methods
tutorial_Library_name: Property = Property(name="name", type=StringType)
tutorial_Library_m_findBook: Method = Method(name="findBook", parameters={Parameter(name='bookName')}, type=StringType)
tutorial_Library.attributes={tutorial_Library_name}
tutorial_Library.methods={tutorial_Library_m_findBook}

# tutorial_Book class attributes and methods
tutorial_Book_name: Property = Property(name="name", type=StringType)
tutorial_Book_copies: Property = Property(name="copies", type=StringType)
tutorial_Book_m_isAvailable: Method = Method(name="isAvailable", parameters={}, type=StringType)
tutorial_Book.attributes={tutorial_Book_name, tutorial_Book_copies}
tutorial_Book.methods={tutorial_Book_m_isAvailable}

# Relationships
loans1: BinaryAssociation = BinaryAssociation(
    name="loans1",
    ends={
        Property(name="tutorial_Loan", type=tutorial_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="tutorial_Library", type=tutorial_Loan, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
members2: BinaryAssociation = BinaryAssociation(
    name="members2",
    ends={
        Property(name="Member", type=tutorial_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library3", type=tutorial_Member, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
books0: BinaryAssociation = BinaryAssociation(
    name="books0",
    ends={
        Property(name="Book", type=tutorial_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library", type=tutorial_Book, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
library7: BinaryAssociation = BinaryAssociation(
    name="library7",
    ends={
        Property(name="Library8", type=tutorial_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="members", type=tutorial_Library, multiplicity=Multiplicity(0, 1))
    }
)
book9: BinaryAssociation = BinaryAssociation(
    name="book9",
    ends={
        Property(name="tutorial_Book11", type=tutorial_Loan, multiplicity=Multiplicity(1, 1)),
        Property(name="tutorial_Loan10", type=tutorial_Book, multiplicity=Multiplicity(0, 1))
    }
)
member12: BinaryAssociation = BinaryAssociation(
    name="member12",
    ends={
        Property(name="tutorial_Member", type=tutorial_Loan, multiplicity=Multiplicity(1, 1)),
        Property(name="tutorial_Loan13", type=tutorial_Member, multiplicity=Multiplicity(0, 1))
    }
)
library4: BinaryAssociation = BinaryAssociation(
    name="library4",
    ends={
        Property(name="Library", type=tutorial_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="books", type=tutorial_Library, multiplicity=Multiplicity(0, 1))
    }
)
loans5: BinaryAssociation = BinaryAssociation(
    name="loans5",
    ends={
        Property(name="tutorial_Loan6", type=tutorial_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="tutorial_Book", type=tutorial_Loan, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="tutorial",
    types={tutorial_Loan, tutorial_Member, tutorial_Library, tutorial_Book},
    associations={loans1, members2, books0, library7, book9, member12, library4, loans5},
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