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
patron__Actor = Class(name="patron__Actor")
Librarian__Actor = Class(name="Librarian__Actor")
check_out__UseCase = Class(name="check_out__UseCase")
reserve_UseCase = Class(name="reserve_UseCase")
return__UseCase = Class(name="return__UseCase")
renew_UseCase = Class(name="renew_UseCase")
organize_books_UseCase = Class(name="organize_books_UseCase")
help_people_with_research__UseCase = Class(name="help_people_with_research__UseCase")
retire_books_UseCase = Class(name="retire_books_UseCase")
replace_books_with_updated_info_UseCase = Class(name="replace_books_with_updated_info_UseCase")
UseCase_UseCase = Class(name="UseCase_UseCase")
UseCase2_UseCase = Class(name="UseCase2_UseCase")
UseCase3_UseCase = Class(name="UseCase3_UseCase")
UseCase4_UseCase = Class(name="UseCase4_UseCase")
renew_magazine_subscr_UseCase = Class(name="renew_magazine_subscr_UseCase")
Order_new_books_UseCase = Class(name="Order_new_books_UseCase")
library_management__patron = Class(name="library_management__patron")
library_management__librarian = Class(name="library_management__librarian")
library_management__Library = Class(name="library_management__Library")

# patron__Actor class attributes and methods

# Librarian__Actor class attributes and methods

# check_out__UseCase class attributes and methods

# reserve_UseCase class attributes and methods

# return__UseCase class attributes and methods

# renew_UseCase class attributes and methods

# organize_books_UseCase class attributes and methods

# help_people_with_research__UseCase class attributes and methods

# retire_books_UseCase class attributes and methods

# replace_books_with_updated_info_UseCase class attributes and methods

# UseCase_UseCase class attributes and methods

# UseCase2_UseCase class attributes and methods

# UseCase3_UseCase class attributes and methods

# UseCase4_UseCase class attributes and methods

# renew_magazine_subscr_UseCase class attributes and methods

# Order_new_books_UseCase class attributes and methods

# library_management__patron class attributes and methods
library_management__patron_PayFIne_Dt_date_: Property = Property(name="PayFIne_Dt_date_", type=IntegerType)
library_management__patron.attributes={library_management__patron_PayFIne_Dt_date_}

# library_management__librarian class attributes and methods
library_management__librarian_CollectFIne_fine_: Property = Property(name="CollectFIne_fine_", type=IntegerType)
library_management__librarian.attributes={library_management__librarian_CollectFIne_fine_}

# library_management__Library class attributes and methods
library_management__Library_Books: Property = Property(name="Books", type=StringType)
library_management__Library_Softwares: Property = Property(name="Softwares", type=StringType)
library_management__Library_Videos: Property = Property(name="Videos", type=StringType)
library_management__Library_Computers: Property = Property(name="Computers", type=StringType)
library_management__Library_CD: Property = Property(name="CD", type=StringType)
library_management__Library.attributes={library_management__Library_Videos, library_management__Library_Softwares, library_management__Library_Computers, library_management__Library_Books, library_management__Library_CD}

# Relationships
patron__reserve: BinaryAssociation = BinaryAssociation(
    name="patron__reserve",
    ends={
        Property(name="reserve0", type=reserve_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="patron1", type=patron__Actor, multiplicity=Multiplicity(0, 1))
    }
)
patron__return: BinaryAssociation = BinaryAssociation(
    name="patron__return",
    ends={
        Property(name="return2", type=return__UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="patron3", type=patron__Actor, multiplicity=Multiplicity(0, 1))
    }
)
patron__check_out: BinaryAssociation = BinaryAssociation(
    name="patron__check_out",
    ends={
        Property(name="check_out4", type=check_out__UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="patron5", type=patron__Actor, multiplicity=Multiplicity(0, 1))
    }
)
patron__renew: BinaryAssociation = BinaryAssociation(
    name="patron__renew",
    ends={
        Property(name="renew6", type=renew_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="patron7", type=patron__Actor, multiplicity=Multiplicity(0, 1))
    }
)
check_out__Librarian: BinaryAssociation = BinaryAssociation(
    name="check_out__Librarian",
    ends={
        Property(name="librarian8", type=Librarian__Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="check_out9", type=check_out__UseCase, multiplicity=Multiplicity(0, 1))
    }
)
reserve_Librarian: BinaryAssociation = BinaryAssociation(
    name="reserve_Librarian",
    ends={
        Property(name="librarian10", type=Librarian__Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="reserve11", type=reserve_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
return__Librarian: BinaryAssociation = BinaryAssociation(
    name="return__Librarian",
    ends={
        Property(name="librarian12", type=Librarian__Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="return13", type=return__UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Librarian__renew: BinaryAssociation = BinaryAssociation(
    name="Librarian__renew",
    ends={
        Property(name="renew14", type=renew_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="librarian15", type=Librarian__Actor, multiplicity=Multiplicity(0, 1))
    }
)
organize_books_Librarian: BinaryAssociation = BinaryAssociation(
    name="organize_books_Librarian",
    ends={
        Property(name="librarian16", type=Librarian__Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="organize_books17", type=organize_books_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Librarian__help_people_with_research: BinaryAssociation = BinaryAssociation(
    name="Librarian__help_people_with_research",
    ends={
        Property(name="help_people_with_research18", type=help_people_with_research__UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="librarian19", type=Librarian__Actor, multiplicity=Multiplicity(0, 1))
    }
)
Librarian__retire_books: BinaryAssociation = BinaryAssociation(
    name="Librarian__retire_books",
    ends={
        Property(name="retire_books20", type=retire_books_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="librarian21", type=Librarian__Actor, multiplicity=Multiplicity(0, 1))
    }
)
Librarian__replace_books_with_updated_info: BinaryAssociation = BinaryAssociation(
    name="Librarian__replace_books_with_updated_info",
    ends={
        Property(name="replace_books_with_updated_info22", type=replace_books_with_updated_info_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="librarian23", type=Librarian__Actor, multiplicity=Multiplicity(0, 1))
    }
)
Librarian__renew_magazine_subscr: BinaryAssociation = BinaryAssociation(
    name="Librarian__renew_magazine_subscr",
    ends={
        Property(name="renew_magazine_subscr24", type=renew_magazine_subscr_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="librarian25", type=Librarian__Actor, multiplicity=Multiplicity(0, 1))
    }
)
Librarian__Order_new_books: BinaryAssociation = BinaryAssociation(
    name="Librarian__Order_new_books",
    ends={
        Property(name="order_new_books26", type=Order_new_books_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="librarian27", type=Librarian__Actor, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_0dFVEK3xEee6S77dw3LIvQ",
    types={patron__Actor, Librarian__Actor, check_out__UseCase, reserve_UseCase, return__UseCase, renew_UseCase, organize_books_UseCase, help_people_with_research__UseCase, retire_books_UseCase, replace_books_with_updated_info_UseCase, UseCase_UseCase, UseCase2_UseCase, UseCase3_UseCase, UseCase4_UseCase, renew_magazine_subscr_UseCase, Order_new_books_UseCase, library_management__patron, library_management__librarian, library_management__Library},
    associations={patron__reserve, patron__return, patron__check_out, patron__renew, check_out__Librarian, reserve_Librarian, return__Librarian, Librarian__renew, organize_books_Librarian, Librarian__help_people_with_research, Librarian__retire_books, Librarian__replace_books_with_updated_info, Librarian__renew_magazine_subscr, Librarian__Order_new_books},
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