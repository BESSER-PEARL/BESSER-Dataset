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
sistedesMM_Person = Class(name="sistedesMM::Person")
sistedesMM_Article = Class(name="sistedesMM::Article")
Publication = Class(name="Publication")
sistedesMM_University = Class(name="sistedesMM::University")
sistedesMM_Publication = Class(name="sistedesMM::Publication", is_abstract=True)
sistedesMM_Edition = Class(name="sistedesMM::Edition")
sistedesMM_Editor = Class(name="sistedesMM::Editor")
sistedesMM_Journal = Class(name="sistedesMM::Journal")
sistedesMM_InProceedings = Class(name="sistedesMM::InProceedings")
sistedesMM_Publisher = Class(name="sistedesMM::Publisher")
sistedesMM_SistedesMember = Class(name="sistedesMM::SistedesMember")
Person = Class(name="Person")
sistedesMM_Book = Class(name="sistedesMM::Book")

# sistedesMM_Person class attributes and methods
sistedesMM_Person_name: Property = Property(name="name", type=StringType)
sistedesMM_Person_surname: Property = Property(name="surname", type=StringType)
sistedesMM_Person_email: Property = Property(name="email", type=StringType)
sistedesMM_Person_nationality: Property = Property(name="nationality", type=StringType)
sistedesMM_Person.attributes={sistedesMM_Person_email, sistedesMM_Person_surname, sistedesMM_Person_name, sistedesMM_Person_nationality}

# sistedesMM_Article class attributes and methods
sistedesMM_Article_title: Property = Property(name="title", type=StringType)
sistedesMM_Article_fromPage: Property = Property(name="fromPage", type=IntegerType)
sistedesMM_Article_toPage: Property = Property(name="toPage", type=IntegerType)
sistedesMM_Article_number: Property = Property(name="number", type=IntegerType)
sistedesMM_Article_volume: Property = Property(name="volume", type=StringType)
sistedesMM_Article_month: Property = Property(name="month", type=StringType)
sistedesMM_Article_year: Property = Property(name="year", type=IntegerType)
sistedesMM_Article.attributes={sistedesMM_Article_month, sistedesMM_Article_toPage, sistedesMM_Article_year, sistedesMM_Article_number, sistedesMM_Article_fromPage, sistedesMM_Article_volume, sistedesMM_Article_title}

# Publication class attributes and methods

# sistedesMM_University class attributes and methods
sistedesMM_University_name: Property = Property(name="name", type=StringType)
sistedesMM_University_city: Property = Property(name="city", type=StringType)
sistedesMM_University_provinceOrState: Property = Property(name="provinceOrState", type=StringType)
sistedesMM_University_country: Property = Property(name="country", type=StringType)
sistedesMM_University.attributes={sistedesMM_University_name, sistedesMM_University_country, sistedesMM_University_city, sistedesMM_University_provinceOrState}

# sistedesMM_Publication class attributes and methods

# sistedesMM_Edition class attributes and methods
sistedesMM_Edition_year: Property = Property(name="year", type=IntegerType)
sistedesMM_Edition_location: Property = Property(name="location", type=StringType)
sistedesMM_Edition.attributes={sistedesMM_Edition_location, sistedesMM_Edition_year}

# sistedesMM_Editor class attributes and methods
sistedesMM_Editor_name: Property = Property(name="name", type=StringType)
sistedesMM_Editor.attributes={sistedesMM_Editor_name}

# sistedesMM_Journal class attributes and methods
sistedesMM_Journal_name: Property = Property(name="name", type=StringType)
sistedesMM_Journal_jcrIndexed: Property = Property(name="jcrIndexed", type=BooleanType)
sistedesMM_Journal_acronym: Property = Property(name="acronym", type=StringType)
sistedesMM_Journal.attributes={sistedesMM_Journal_jcrIndexed, sistedesMM_Journal_name, sistedesMM_Journal_acronym}

# sistedesMM_InProceedings class attributes and methods
sistedesMM_InProceedings_title: Property = Property(name="title", type=StringType)
sistedesMM_InProceedings_bookTitle: Property = Property(name="bookTitle", type=StringType)
sistedesMM_InProceedings_year: Property = Property(name="year", type=IntegerType)
sistedesMM_InProceedings_fromPage: Property = Property(name="fromPage", type=StringType)
sistedesMM_InProceedings_toPage: Property = Property(name="toPage", type=StringType)
sistedesMM_InProceedings_month: Property = Property(name="month", type=StringType)
sistedesMM_InProceedings.attributes={sistedesMM_InProceedings_toPage, sistedesMM_InProceedings_bookTitle, sistedesMM_InProceedings_fromPage, sistedesMM_InProceedings_month, sistedesMM_InProceedings_year, sistedesMM_InProceedings_title}

# sistedesMM_Publisher class attributes and methods
sistedesMM_Publisher_name: Property = Property(name="name", type=StringType)
sistedesMM_Publisher_address: Property = Property(name="address", type=StringType)
sistedesMM_Publisher.attributes={sistedesMM_Publisher_address, sistedesMM_Publisher_name}

# sistedesMM_SistedesMember class attributes and methods

# Person class attributes and methods

# sistedesMM_Book class attributes and methods
sistedesMM_Book_title: Property = Property(name="title", type=StringType)
sistedesMM_Book_year: Property = Property(name="year", type=IntegerType)
sistedesMM_Book_month: Property = Property(name="month", type=StringType)
sistedesMM_Book_volume: Property = Property(name="volume", type=StringType)
sistedesMM_Book_series: Property = Property(name="series", type=StringType)
sistedesMM_Book_edition: Property = Property(name="edition", type=IntegerType)
sistedesMM_Book_isbn: Property = Property(name="isbn", type=StringType)
sistedesMM_Book.attributes={sistedesMM_Book_isbn, sistedesMM_Book_year, sistedesMM_Book_edition, sistedesMM_Book_month, sistedesMM_Book_volume, sistedesMM_Book_series, sistedesMM_Book_title}

# Relationships
authors2: BinaryAssociation = BinaryAssociation(
    name="authors2",
    ends={
        Property(name="Person", type=sistedesMM_Publication, multiplicity=Multiplicity(1, 1)),
        Property(name="publications", type=sistedesMM_Person, multiplicity=Multiplicity(1, 9999))
    }
)
university0: BinaryAssociation = BinaryAssociation(
    name="university0",
    ends={
        Property(name="sistedesMM_University", type=sistedesMM_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="sistedesMM_Person", type=sistedesMM_University, multiplicity=Multiplicity(1, 9999))
    }
)
publications1: BinaryAssociation = BinaryAssociation(
    name="publications1",
    ends={
        Property(name="Publication", type=sistedesMM_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="authors", type=sistedesMM_Publication, multiplicity=Multiplicity(0, 9999))
    }
)
publisher4: BinaryAssociation = BinaryAssociation(
    name="publisher4",
    ends={
        Property(name="sistedesMM_Publisher", type=sistedesMM_InProceedings, multiplicity=Multiplicity(1, 1)),
        Property(name="sistedesMM_InProceedings", type=sistedesMM_Publisher, multiplicity=Multiplicity(0, 1))
    }
)
editors5: BinaryAssociation = BinaryAssociation(
    name="editors5",
    ends={
        Property(name="sistedesMM_Editor", type=sistedesMM_InProceedings, multiplicity=Multiplicity(1, 1)),
        Property(name="sistedesMM_InProceedings6", type=sistedesMM_Editor, multiplicity=Multiplicity(0, 9999))
    }
)
journal3: BinaryAssociation = BinaryAssociation(
    name="journal3",
    ends={
        Property(name="Journal", type=sistedesMM_Article, multiplicity=Multiplicity(1, 1)),
        Property(name="articles", type=sistedesMM_Journal, multiplicity=Multiplicity(0, 1))
    }
)
attendedTo10: BinaryAssociation = BinaryAssociation(
    name="attendedTo10",
    ends={
        Property(name="sistedesMM_Edition", type=sistedesMM_SistedesMember, multiplicity=Multiplicity(1, 1)),
        Property(name="sistedesMM_SistedesMember", type=sistedesMM_Edition, multiplicity=Multiplicity(0, 9999))
    }
)
articles7: BinaryAssociation = BinaryAssociation(
    name="articles7",
    ends={
        Property(name="Article", type=sistedesMM_Journal, multiplicity=Multiplicity(1, 1)),
        Property(name="journal", type=sistedesMM_Article, multiplicity=Multiplicity(0, 1))
    }
)
publisher8: BinaryAssociation = BinaryAssociation(
    name="publisher8",
    ends={
        Property(name="sistedesMM_Publisher9", type=sistedesMM_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="sistedesMM_Book", type=sistedesMM_Publisher, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_sistedesMM_Article_Publication = Generalization(general=Publication, specific=sistedesMM_Article)
gen_sistedesMM_InProceedings_Publication = Generalization(general=Publication, specific=sistedesMM_InProceedings)
gen_sistedesMM_SistedesMember_Person = Generalization(general=Person, specific=sistedesMM_SistedesMember)
gen_sistedesMM_Book_Publication = Generalization(general=Publication, specific=sistedesMM_Book)

# Domain Model
domain_model = DomainModel(
    name="sistedesMM",
    types={sistedesMM_Person, sistedesMM_Article, Publication, sistedesMM_University, sistedesMM_Publication, sistedesMM_Edition, sistedesMM_Editor, sistedesMM_Journal, sistedesMM_InProceedings, sistedesMM_Publisher, sistedesMM_SistedesMember, Person, sistedesMM_Book},
    associations={authors2, university0, publications1, publisher4, editors5, journal3, attendedTo10, articles7, publisher8},
    generalizations={gen_sistedesMM_Article_Publication, gen_sistedesMM_InProceedings_Publication, gen_sistedesMM_SistedesMember_Person, gen_sistedesMM_Book_Publication},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)