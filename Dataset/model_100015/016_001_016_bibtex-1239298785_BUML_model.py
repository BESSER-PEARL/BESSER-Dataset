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
bibtex_Model = Class(name="bibtex_Model")
bibtex_Document = Class(name="bibtex_Document")

# bibtex_Model class attributes and methods

# bibtex_Document class attributes and methods
bibtex_Document_type: Property = Property(name="type", type=StringType)
bibtex_Document_file: Property = Property(name="file", type=StringType)
bibtex_Document_cites: Property = Property(name="cites", type=IntegerType)
bibtex_Document_authors: Property = Property(name="authors", type=StringType)
bibtex_Document_abstract: Property = Property(name="abstract", type=StringType)
bibtex_Document_year: Property = Property(name="year", type=StringType)
bibtex_Document_month: Property = Property(name="month", type=StringType)
bibtex_Document_title: Property = Property(name="title", type=StringType)
bibtex_Document_key: Property = Property(name="key", type=StringType)
bibtex_Document_doi: Property = Property(name="doi", type=StringType)
bibtex_Document_url: Property = Property(name="url", type=StringType)
bibtex_Document_unparsedAuthors: Property = Property(name="unparsedAuthors", type=StringType)
bibtex_Document.attributes={bibtex_Document_abstract, bibtex_Document_doi, bibtex_Document_url, bibtex_Document_authors, bibtex_Document_unparsedAuthors, bibtex_Document_key, bibtex_Document_year, bibtex_Document_cites, bibtex_Document_file, bibtex_Document_title, bibtex_Document_type, bibtex_Document_month}

# Relationships
taxonomy0: BinaryAssociation = BinaryAssociation(
    name="taxonomy0",
    ends={
        Property(name="bibtex_Model", type=bibtex_Document, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_Document", type=bibtex_Model, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="bibtex",
    types={bibtex_Model, bibtex_Document},
    associations={taxonomy0},
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