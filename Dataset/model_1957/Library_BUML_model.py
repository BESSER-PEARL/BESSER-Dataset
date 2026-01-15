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
library_Model = Class(name="library::Model")
library_Command = Class(name="library::Command")
library_ShowUserAccount = Class(name="library::ShowUserAccount")
library_Search = Class(name="library::Search")
Command = Class(name="Command")
library_AddAuthor = Class(name="library::AddAuthor")
library_Author = Class(name="library::Author")
library_ByYear = Class(name="library::ByYear")
Search = Class(name="Search")
library_ByAuthor = Class(name="library::ByAuthor")
library_Lend = Class(name="library::Lend")
library_Add = Class(name="library::Add")
library_AddUser = Class(name="library::AddUser")
library_Remove = Class(name="library::Remove")
library_Return = Class(name="library::Return")
library_Check = Class(name="library::Check")
library_Show = Class(name="library::Show")

# library_Model class attributes and methods

# library_Command class attributes and methods

# library_ShowUserAccount class attributes and methods
library_ShowUserAccount_firstname: Property = Property(name="firstname", type=StringType)
library_ShowUserAccount_secondname: Property = Property(name="secondname", type=StringType)
library_ShowUserAccount.attributes={library_ShowUserAccount_firstname, library_ShowUserAccount_secondname}

# library_Search class attributes and methods

# Command class attributes and methods

# library_AddAuthor class attributes and methods
library_AddAuthor_isbn: Property = Property(name="isbn", type=StringType)
library_AddAuthor.attributes={library_AddAuthor_isbn}

# library_Author class attributes and methods
library_Author_firstname: Property = Property(name="firstname", type=StringType)
library_Author_secondname: Property = Property(name="secondname", type=StringType)
library_Author.attributes={library_Author_firstname, library_Author_secondname}

# library_ByYear class attributes and methods
library_ByYear_year: Property = Property(name="year", type=StringType)
library_ByYear.attributes={library_ByYear_year}

# Search class attributes and methods

# library_ByAuthor class attributes and methods

# library_Lend class attributes and methods
library_Lend_isbn: Property = Property(name="isbn", type=StringType)
library_Lend_firstname: Property = Property(name="firstname", type=StringType)
library_Lend_secondname: Property = Property(name="secondname", type=StringType)
library_Lend.attributes={library_Lend_firstname, library_Lend_isbn, library_Lend_secondname}

# library_Add class attributes and methods
library_Add_isbn: Property = Property(name="isbn", type=StringType)
library_Add_title: Property = Property(name="title", type=StringType)
library_Add_year: Property = Property(name="year", type=StringType)
library_Add.attributes={library_Add_year, library_Add_isbn, library_Add_title}

# library_AddUser class attributes and methods
library_AddUser_firstname: Property = Property(name="firstname", type=StringType)
library_AddUser_secondname: Property = Property(name="secondname", type=StringType)
library_AddUser_age: Property = Property(name="age", type=StringType)
library_AddUser.attributes={library_AddUser_secondname, library_AddUser_age, library_AddUser_firstname}

# library_Remove class attributes and methods
library_Remove_isbn: Property = Property(name="isbn", type=StringType)
library_Remove.attributes={library_Remove_isbn}

# library_Return class attributes and methods
library_Return_isbn: Property = Property(name="isbn", type=StringType)
library_Return_firstname: Property = Property(name="firstname", type=StringType)
library_Return_secondname: Property = Property(name="secondname", type=StringType)
library_Return.attributes={library_Return_secondname, library_Return_isbn, library_Return_firstname}

# library_Check class attributes and methods
library_Check_isbn: Property = Property(name="isbn", type=StringType)
library_Check.attributes={library_Check_isbn}

# library_Show class attributes and methods
library_Show_what: Property = Property(name="what", type=StringType)
library_Show.attributes={library_Show_what}

# Relationships
commands0: BinaryAssociation = BinaryAssociation(
    name="commands0",
    ends={
        Property(name="library_Model", type=library_Command, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="library_Command", type=library_Model, multiplicity=Multiplicity(1, 1))
    }
)
author1: BinaryAssociation = BinaryAssociation(
    name="author1",
    ends={
        Property(name="library_Author", type=library_AddAuthor, multiplicity=Multiplicity(1, 1)),
        Property(name="library_AddAuthor", type=library_Author, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
author2: BinaryAssociation = BinaryAssociation(
    name="author2",
    ends={
        Property(name="library_Author3", type=library_ByAuthor, multiplicity=Multiplicity(1, 1)),
        Property(name="library_ByAuthor", type=library_Author, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
authors4: BinaryAssociation = BinaryAssociation(
    name="authors4",
    ends={
        Property(name="library_Author5", type=library_Add, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Add", type=library_Author, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_library_ShowUserAccount_Command = Generalization(general=Command, specific=library_ShowUserAccount)
gen_library_Search_Command = Generalization(general=Command, specific=library_Search)
gen_library_AddAuthor_Command = Generalization(general=Command, specific=library_AddAuthor)
gen_library_ByYear_Search = Generalization(general=Search, specific=library_ByYear)
gen_library_ByAuthor_Search = Generalization(general=Search, specific=library_ByAuthor)
gen_library_Lend_Command = Generalization(general=Command, specific=library_Lend)
gen_library_Add_Command = Generalization(general=Command, specific=library_Add)
gen_library_AddUser_Command = Generalization(general=Command, specific=library_AddUser)
gen_library_Remove_Command = Generalization(general=Command, specific=library_Remove)
gen_library_Return_Command = Generalization(general=Command, specific=library_Return)
gen_library_Check_Command = Generalization(general=Command, specific=library_Check)
gen_library_Show_Command = Generalization(general=Command, specific=library_Show)

# Domain Model
domain_model = DomainModel(
    name="library",
    types={library_Model, library_Command, library_ShowUserAccount, library_Search, Command, library_AddAuthor, library_Author, library_ByYear, Search, library_ByAuthor, library_Lend, library_Add, library_AddUser, library_Remove, library_Return, library_Check, library_Show},
    associations={commands0, author1, author2, authors4},
    generalizations={gen_library_ShowUserAccount_Command, gen_library_Search_Command, gen_library_AddAuthor_Command, gen_library_ByYear_Search, gen_library_ByAuthor_Search, gen_library_Lend_Command, gen_library_Add_Command, gen_library_AddUser_Command, gen_library_Remove_Command, gen_library_Return_Command, gen_library_Check_Command, gen_library_Show_Command},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)