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
library_Writer = Class(name="library::Writer", is_abstract=True)
library_Book = Class(name="library::Book")
library_Library = Class(name="library::Library")
library_GuideBookWriter = Class(name="library::GuideBookWriter")
Writer = Class(name="Writer")
library_SpecialistBookWriter = Class(name="library::SpecialistBookWriter")

# library_Writer class attributes and methods
library_Writer_name: Property = Property(name="name", type=StringType)
library_Writer.attributes={library_Writer_name}

# library_Book class attributes and methods
library_Book_pages: Property = Property(name="pages", type=StringType)
library_Book_title: Property = Property(name="title", type=StringType)
library_Book_ISBN: Property = Property(name="ISBN", type=StringType)
library_Book.attributes={library_Book_pages, library_Book_ISBN, library_Book_title}

# library_Library class attributes and methods
library_Library_name: Property = Property(name="name", type=StringType)
library_Library.attributes={library_Library_name}

# library_GuideBookWriter class attributes and methods
library_GuideBookWriter_countries: Property = Property(name="countries", type=StringType)
library_GuideBookWriter.attributes={library_GuideBookWriter_countries}

# Writer class attributes and methods

# library_SpecialistBookWriter class attributes and methods
library_SpecialistBookWriter_subject: Property = Property(name="subject", type=StringType)
library_SpecialistBookWriter.attributes={library_SpecialistBookWriter_subject}

# Relationships
author0: BinaryAssociation = BinaryAssociation(
    name="author0",
    ends={
        Property(name="library_Writer", type=library_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Book", type=library_Writer, multiplicity=Multiplicity(1, 1))
    }
)
books1: BinaryAssociation = BinaryAssociation(
    name="books1",
    ends={
        Property(name="library_Book2", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library", type=library_Book, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_library_GuideBookWriter_Writer = Generalization(general=Writer, specific=library_GuideBookWriter)
gen_library_SpecialistBookWriter_Writer = Generalization(general=Writer, specific=library_SpecialistBookWriter)

# Domain Model
domain_model = DomainModel(
    name="library",
    types={library_Writer, library_Book, library_Library, library_GuideBookWriter, Writer, library_SpecialistBookWriter},
    associations={author0, books1},
    generalizations={gen_library_GuideBookWriter_Writer, gen_library_SpecialistBookWriter_Writer},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)