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
Type: Enumeration = Enumeration(
    name="Type",
    literals={
            EnumerationLiteral(name="asd")
    }
)

# Classes
tutorial_Library = Class(name="tutorial::Library")
tutorial_Member = Class(name="tutorial::Member")
tutorial_Book = Class(name="tutorial::Book")
tutorial_Loan = Class(name="tutorial::Loan")
SubOrg1_sb1C = Class(name="SubOrg1::sb1C")
tutorial_Organization_Librarian = Class(name="tutorial::Organization::Librarian")
Employee = Class(name="Employee")
SubOrg2_sb2C = Class(name="SubOrg2::sb2C")
tutorial_Organization_Ref = Class(name="tutorial::Organization::Ref")
Library = Class(name="Library")
Organization_tutorial_Item = Class(name="Organization::tutorial::Item")
tutorial_SubOrg1_sb1C = Class(name="tutorial::SubOrg1::sb1C")
tutorial_SubOrg2_sb2C = Class(name="tutorial::SubOrg2::sb2C")

# tutorial_Library class attributes and methods
tutorial_Library_name: Property = Property(name="name", type=StringType)
tutorial_Library.attributes={tutorial_Library_name}

# tutorial_Member class attributes and methods
tutorial_Member_name: Property = Property(name="name", type=StringType)
tutorial_Member_m_tespOP: Method = Method(name="tespOP", parameters={})
tutorial_Member.attributes={tutorial_Member_name}
tutorial_Member.methods={tutorial_Member_m_tespOP}

# tutorial_Book class attributes and methods
tutorial_Book_copies: Property = Property(name="copies", type=StringType)
tutorial_Book_name: Property = Property(name="name", type=StringType)
tutorial_Book_m_isAvailable: Method = Method(name="isAvailable", parameters={Parameter(name='param1'), Parameter(name='param2')}, type=BooleanType)
tutorial_Book.attributes={tutorial_Book_name, tutorial_Book_copies}
tutorial_Book.methods={tutorial_Book_m_isAvailable}

# tutorial_Loan class attributes and methods
tutorial_Loan_date: Property = Property(name="date", type=DateType)
tutorial_Loan.attributes={tutorial_Loan_date}

# SubOrg1_sb1C class attributes and methods

# tutorial_Organization_Librarian class attributes and methods
tutorial_Organization_Librarian_m_orgOpp: Method = Method(name="orgOpp", parameters={}, type=StringType)
tutorial_Organization_Librarian.methods={tutorial_Organization_Librarian_m_orgOpp}

# Employee class attributes and methods

# SubOrg2_sb2C class attributes and methods

# tutorial_Organization_Ref class attributes and methods

# Library class attributes and methods

# Organization_tutorial_Item class attributes and methods

# tutorial_SubOrg1_sb1C class attributes and methods

# tutorial_SubOrg2_sb2C class attributes and methods

# Relationships
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
loans1: BinaryAssociation = BinaryAssociation(
    name="loans1",
    ends={
        Property(name="tutorial_Loan", type=tutorial_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="tutorial_Library", type=tutorial_Loan, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
library4: BinaryAssociation = BinaryAssociation(
    name="library4",
    ends={
        Property(name="Library", type=tutorial_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="books", type=tutorial_Library, multiplicity=Multiplicity(0, 1))
    }
)
book14: BinaryAssociation = BinaryAssociation(
    name="book14",
    ends={
        Property(name="SubOrg1_sb1C", type=tutorial_Loan, multiplicity=Multiplicity(1, 1)),
        Property(name="tutorial_Loan15", type=SubOrg1_sb1C, multiplicity=Multiplicity(1, 1))
    }
)
loans5: BinaryAssociation = BinaryAssociation(
    name="loans5",
    ends={
        Property(name="tutorial_Loan6", type=tutorial_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="tutorial_Book", type=tutorial_Loan, multiplicity=Multiplicity(0, 9999))
    }
)
library7: BinaryAssociation = BinaryAssociation(
    name="library7",
    ends={
        Property(name="Library8", type=tutorial_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="members", type=tutorial_Library, multiplicity=Multiplicity(0, 1))
    }
)
loans9: BinaryAssociation = BinaryAssociation(
    name="loans9",
    ends={
        Property(name="tutorial_Loan10", type=tutorial_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="tutorial_Member", type=tutorial_Loan, multiplicity=Multiplicity(0, 9999))
    }
)
books11: BinaryAssociation = BinaryAssociation(
    name="books11",
    ends={
        Property(name="tutorial_Book13", type=tutorial_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="tutorial_Member12", type=tutorial_Book, multiplicity=Multiplicity(0, 9999))
    }
)
member16: BinaryAssociation = BinaryAssociation(
    name="member16",
    ends={
        Property(name="tutorial_Member18", type=tutorial_Loan, multiplicity=Multiplicity(1, 1)),
        Property(name="tutorial_Loan17", type=tutorial_Member, multiplicity=Multiplicity(1, 1))
    }
)
workOn19: BinaryAssociation = BinaryAssociation(
    name="workOn19",
    ends={
        Property(name="SubOrg2_sb2C", type=tutorial_Organization_Librarian, multiplicity=Multiplicity(1, 1)),
        Property(name="tutorial_Organization_Librarian", type=SubOrg2_sb2C, multiplicity=Multiplicity(0, 1))
    }
)
RefOutsideEcore20: BinaryAssociation = BinaryAssociation(
    name="RefOutsideEcore20",
    ends={
        Property(name="Organization_tutorial_Item", type=tutorial_Organization_Ref, multiplicity=Multiplicity(1, 1)),
        Property(name="tutorial_Organization_Ref", type=Organization_tutorial_Item, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_tutorial_Organization_Librarian_Employee = Generalization(general=Employee, specific=tutorial_Organization_Librarian)
gen_tutorial_Organization_Ref_Library = Generalization(general=Library, specific=tutorial_Organization_Ref)

# Domain Model
domain_model = DomainModel(
    name="tutorial",
    types={tutorial_Library, tutorial_Member, tutorial_Book, tutorial_Loan, SubOrg1_sb1C, tutorial_Organization_Librarian, Employee, SubOrg2_sb2C, tutorial_Organization_Ref, Library, Organization_tutorial_Item, tutorial_SubOrg1_sb1C, tutorial_SubOrg2_sb2C, Type},
    associations={members2, books0, loans1, library4, book14, loans5, library7, loans9, books11, member16, workOn19, RefOutsideEcore20},
    generalizations={gen_tutorial_Organization_Librarian_Employee, gen_tutorial_Organization_Ref_Library},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)