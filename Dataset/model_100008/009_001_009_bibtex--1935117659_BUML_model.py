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
Bibtex_BibtexEntry = Class(name="Bibtex_BibtexEntry")
Bibtex_Tag = Class(name="Bibtex_Tag")

# Bibtex_BibtexEntry class attributes and methods
Bibtex_BibtexEntry_Text: Property = Property(name="Text", type=StringType)
Bibtex_BibtexEntry_Title: Property = Property(name="Title", type=StringType)
Bibtex_BibtexEntry_Author: Property = Property(name="Author", type=StringType)
Bibtex_BibtexEntry_Journal: Property = Property(name="Journal", type=StringType)
Bibtex_BibtexEntry_Volume: Property = Property(name="Volume", type=StringType)
Bibtex_BibtexEntry_Pages: Property = Property(name="Pages", type=StringType)
Bibtex_BibtexEntry_Year: Property = Property(name="Year", type=StringType)
Bibtex_BibtexEntry_publicationFilePath: Property = Property(name="publicationFilePath", type=StringType)
Bibtex_BibtexEntry_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
Bibtex_BibtexEntry.attributes={Bibtex_BibtexEntry_Volume, Bibtex_BibtexEntry_publicationFilePath, Bibtex_BibtexEntry_Text, Bibtex_BibtexEntry_Year, Bibtex_BibtexEntry_Title, Bibtex_BibtexEntry_Journal, Bibtex_BibtexEntry_Author, Bibtex_BibtexEntry_Pages}
Bibtex_BibtexEntry.methods={Bibtex_BibtexEntry_m_toString}

# Bibtex_Tag class attributes and methods
Bibtex_Tag_Name: Property = Property(name="Name", type=StringType)
Bibtex_Tag_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
Bibtex_Tag.attributes={Bibtex_Tag_Name}
Bibtex_Tag.methods={Bibtex_Tag_m_toString}

# Relationships
Tags0: BinaryAssociation = BinaryAssociation(
    name="Tags0",
    ends={
        Property(name="Bibtex_Tag", type=Bibtex_BibtexEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="Bibtex_BibtexEntry", type=Bibtex_Tag, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="Bibtex",
    types={Bibtex_BibtexEntry, Bibtex_Tag},
    associations={Tags0},
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