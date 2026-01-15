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
DBLP_Journal = Class(name="DBLP::Journal")
DBLP_Record = Class(name="DBLP::Record", is_abstract=True)
DBLP_Author = Class(name="DBLP::Author")
DBLP_Article = Class(name="DBLP::Article")
Record = Class(name="Record")
DBLP_InCollection = Class(name="DBLP::InCollection")
DBLP_Book = Class(name="DBLP::Book")
DBLP_Publisher = Class(name="DBLP::Publisher")
DBLP_Editor = Class(name="DBLP::Editor")
DBLP_Organization = Class(name="DBLP::Organization")
DBLP_InProceedings = Class(name="DBLP::InProceedings")
DBLP_MastersThesis = Class(name="DBLP::MastersThesis")
DBLP_School = Class(name="DBLP::School")
DBLP_Proceedings = Class(name="DBLP::Proceedings")
DBLP_PhDThesis = Class(name="DBLP::PhDThesis")
DBLP_Www = Class(name="DBLP::Www")

# DBLP_Journal class attributes and methods
DBLP_Journal_name: Property = Property(name="name", type=StringType)
DBLP_Journal.attributes={DBLP_Journal_name}

# DBLP_Record class attributes and methods
DBLP_Record_ee: Property = Property(name="ee", type=StringType)
DBLP_Record_url: Property = Property(name="url", type=StringType)
DBLP_Record_key: Property = Property(name="key", type=StringType)
DBLP_Record_mdate: Property = Property(name="mdate", type=StringType)
DBLP_Record.attributes={DBLP_Record_key, DBLP_Record_ee, DBLP_Record_url, DBLP_Record_mdate}

# DBLP_Author class attributes and methods
DBLP_Author_name: Property = Property(name="name", type=StringType)
DBLP_Author.attributes={DBLP_Author_name}

# DBLP_Article class attributes and methods
DBLP_Article_title: Property = Property(name="title", type=StringType)
DBLP_Article_fromPage: Property = Property(name="fromPage", type=IntegerType)
DBLP_Article_toPage: Property = Property(name="toPage", type=IntegerType)
DBLP_Article_number: Property = Property(name="number", type=IntegerType)
DBLP_Article_volume: Property = Property(name="volume", type=StringType)
DBLP_Article_month: Property = Property(name="month", type=StringType)
DBLP_Article_year: Property = Property(name="year", type=IntegerType)
DBLP_Article.attributes={DBLP_Article_month, DBLP_Article_title, DBLP_Article_number, DBLP_Article_fromPage, DBLP_Article_year, DBLP_Article_volume, DBLP_Article_toPage}

# Record class attributes and methods

# DBLP_InCollection class attributes and methods
DBLP_InCollection_title: Property = Property(name="title", type=StringType)
DBLP_InCollection_bookTitle: Property = Property(name="bookTitle", type=StringType)
DBLP_InCollection_year: Property = Property(name="year", type=IntegerType)
DBLP_InCollection_fromPage: Property = Property(name="fromPage", type=IntegerType)
DBLP_InCollection_toPage: Property = Property(name="toPage", type=IntegerType)
DBLP_InCollection_month: Property = Property(name="month", type=StringType)
DBLP_InCollection.attributes={DBLP_InCollection_year, DBLP_InCollection_title, DBLP_InCollection_fromPage, DBLP_InCollection_month, DBLP_InCollection_toPage, DBLP_InCollection_bookTitle}

# DBLP_Book class attributes and methods
DBLP_Book_month: Property = Property(name="month", type=StringType)
DBLP_Book_volume: Property = Property(name="volume", type=IntegerType)
DBLP_Book_series: Property = Property(name="series", type=StringType)
DBLP_Book_edition: Property = Property(name="edition", type=IntegerType)
DBLP_Book_isbn: Property = Property(name="isbn", type=StringType)
DBLP_Book_title: Property = Property(name="title", type=StringType)
DBLP_Book_year: Property = Property(name="year", type=IntegerType)
DBLP_Book.attributes={DBLP_Book_title, DBLP_Book_isbn, DBLP_Book_edition, DBLP_Book_volume, DBLP_Book_month, DBLP_Book_series, DBLP_Book_year}

# DBLP_Publisher class attributes and methods
DBLP_Publisher_name: Property = Property(name="name", type=StringType)
DBLP_Publisher_address: Property = Property(name="address", type=StringType)
DBLP_Publisher.attributes={DBLP_Publisher_name, DBLP_Publisher_address}

# DBLP_Editor class attributes and methods
DBLP_Editor_name: Property = Property(name="name", type=StringType)
DBLP_Editor.attributes={DBLP_Editor_name}

# DBLP_Organization class attributes and methods
DBLP_Organization_name: Property = Property(name="name", type=StringType)
DBLP_Organization.attributes={DBLP_Organization_name}

# DBLP_InProceedings class attributes and methods
DBLP_InProceedings_bootitle: Property = Property(name="bootitle", type=StringType)
DBLP_InProceedings_year: Property = Property(name="year", type=IntegerType)
DBLP_InProceedings_fromPage: Property = Property(name="fromPage", type=IntegerType)
DBLP_InProceedings_toPage: Property = Property(name="toPage", type=IntegerType)
DBLP_InProceedings_month: Property = Property(name="month", type=StringType)
DBLP_InProceedings_title: Property = Property(name="title", type=StringType)
DBLP_InProceedings.attributes={DBLP_InProceedings_fromPage, DBLP_InProceedings_month, DBLP_InProceedings_bootitle, DBLP_InProceedings_title, DBLP_InProceedings_toPage, DBLP_InProceedings_year}

# DBLP_MastersThesis class attributes and methods
DBLP_MastersThesis_title: Property = Property(name="title", type=StringType)
DBLP_MastersThesis_year: Property = Property(name="year", type=IntegerType)
DBLP_MastersThesis_month: Property = Property(name="month", type=StringType)
DBLP_MastersThesis.attributes={DBLP_MastersThesis_month, DBLP_MastersThesis_year, DBLP_MastersThesis_title}

# DBLP_School class attributes and methods
DBLP_School_name: Property = Property(name="name", type=StringType)
DBLP_School_address: Property = Property(name="address", type=StringType)
DBLP_School.attributes={DBLP_School_address, DBLP_School_name}

# DBLP_Proceedings class attributes and methods
DBLP_Proceedings_month: Property = Property(name="month", type=StringType)
DBLP_Proceedings_title: Property = Property(name="title", type=StringType)
DBLP_Proceedings_year: Property = Property(name="year", type=IntegerType)
DBLP_Proceedings_isbn: Property = Property(name="isbn", type=StringType)
DBLP_Proceedings.attributes={DBLP_Proceedings_title, DBLP_Proceedings_isbn, DBLP_Proceedings_month, DBLP_Proceedings_year}

# DBLP_PhDThesis class attributes and methods
DBLP_PhDThesis_title: Property = Property(name="title", type=StringType)
DBLP_PhDThesis_year: Property = Property(name="year", type=IntegerType)
DBLP_PhDThesis_month: Property = Property(name="month", type=StringType)
DBLP_PhDThesis.attributes={DBLP_PhDThesis_year, DBLP_PhDThesis_title, DBLP_PhDThesis_month}

# DBLP_Www class attributes and methods
DBLP_Www_title: Property = Property(name="title", type=StringType)
DBLP_Www_year: Property = Property(name="year", type=IntegerType)
DBLP_Www_month: Property = Property(name="month", type=StringType)
DBLP_Www.attributes={DBLP_Www_month, DBLP_Www_year, DBLP_Www_title}

# Relationships
journal1: BinaryAssociation = BinaryAssociation(
    name="journal1",
    ends={
        Property(name="Journal", type=DBLP_Article, multiplicity=Multiplicity(1, 1)),
        Property(name="articles", type=DBLP_Journal, multiplicity=Multiplicity(0, 1))
    }
)
authors0: BinaryAssociation = BinaryAssociation(
    name="authors0",
    ends={
        Property(name="Author", type=DBLP_Record, multiplicity=Multiplicity(1, 1)),
        Property(name="records", type=DBLP_Author, multiplicity=Multiplicity(0, 9999))
    }
)
records2: BinaryAssociation = BinaryAssociation(
    name="records2",
    ends={
        Property(name="Record", type=DBLP_Author, multiplicity=Multiplicity(1, 1)),
        Property(name="authors", type=DBLP_Record, multiplicity=Multiplicity(0, 9999))
    }
)
articles3: BinaryAssociation = BinaryAssociation(
    name="articles3",
    ends={
        Property(name="Article", type=DBLP_Journal, multiplicity=Multiplicity(1, 1)),
        Property(name="journal", type=DBLP_Article, multiplicity=Multiplicity(0, 9999))
    }
)
publisher4: BinaryAssociation = BinaryAssociation(
    name="publisher4",
    ends={
        Property(name="DBLP_Publisher", type=DBLP_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="DBLP_Book", type=DBLP_Publisher, multiplicity=Multiplicity(0, 1))
    }
)
editors11: BinaryAssociation = BinaryAssociation(
    name="editors11",
    ends={
        Property(name="DBLP_Editor12", type=DBLP_InProceedings, multiplicity=Multiplicity(1, 1)),
        Property(name="DBLP_InProceedings", type=DBLP_Editor, multiplicity=Multiplicity(0, 9999))
    }
)
editors5: BinaryAssociation = BinaryAssociation(
    name="editors5",
    ends={
        Property(name="DBLP_Editor", type=DBLP_InCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="DBLP_InCollection", type=DBLP_Editor, multiplicity=Multiplicity(0, 9999))
    }
)
sponsoredBy6: BinaryAssociation = BinaryAssociation(
    name="sponsoredBy6",
    ends={
        Property(name="DBLP_Organization", type=DBLP_InCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="DBLP_InCollection7", type=DBLP_Organization, multiplicity=Multiplicity(0, 1))
    }
)
publisher8: BinaryAssociation = BinaryAssociation(
    name="publisher8",
    ends={
        Property(name="DBLP_Publisher10", type=DBLP_InCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="DBLP_InCollection9", type=DBLP_Publisher, multiplicity=Multiplicity(0, 1))
    }
)
editors20: BinaryAssociation = BinaryAssociation(
    name="editors20",
    ends={
        Property(name="DBLP_Proceedings", type=DBLP_Editor, multiplicity=Multiplicity(0, 9999)),
        Property(name="DBLP_Editor21", type=DBLP_Proceedings, multiplicity=Multiplicity(1, 1))
    }
)
publisher22: BinaryAssociation = BinaryAssociation(
    name="publisher22",
    ends={
        Property(name="DBLP_Publisher24", type=DBLP_Proceedings, multiplicity=Multiplicity(1, 1)),
        Property(name="DBLP_Proceedings23", type=DBLP_Publisher, multiplicity=Multiplicity(0, 1))
    }
)
sponsoredBy25: BinaryAssociation = BinaryAssociation(
    name="sponsoredBy25",
    ends={
        Property(name="DBLP_Organization27", type=DBLP_Proceedings, multiplicity=Multiplicity(1, 1)),
        Property(name="DBLP_Proceedings26", type=DBLP_Organization, multiplicity=Multiplicity(0, 9999))
    }
)
organization13: BinaryAssociation = BinaryAssociation(
    name="organization13",
    ends={
        Property(name="DBLP_Organization15", type=DBLP_InProceedings, multiplicity=Multiplicity(1, 1)),
        Property(name="DBLP_InProceedings14", type=DBLP_Organization, multiplicity=Multiplicity(0, 1))
    }
)
publisher16: BinaryAssociation = BinaryAssociation(
    name="publisher16",
    ends={
        Property(name="DBLP_Publisher18", type=DBLP_InProceedings, multiplicity=Multiplicity(1, 1)),
        Property(name="DBLP_InProceedings17", type=DBLP_Publisher, multiplicity=Multiplicity(0, 1))
    }
)
school19: BinaryAssociation = BinaryAssociation(
    name="school19",
    ends={
        Property(name="DBLP_School", type=DBLP_MastersThesis, multiplicity=Multiplicity(1, 1)),
        Property(name="DBLP_MastersThesis", type=DBLP_School, multiplicity=Multiplicity(0, 1))
    }
)
school28: BinaryAssociation = BinaryAssociation(
    name="school28",
    ends={
        Property(name="DBLP_School29", type=DBLP_PhDThesis, multiplicity=Multiplicity(1, 1)),
        Property(name="DBLP_PhDThesis", type=DBLP_School, multiplicity=Multiplicity(0, 1))
    }
)
editors30: BinaryAssociation = BinaryAssociation(
    name="editors30",
    ends={
        Property(name="DBLP_Editor31", type=DBLP_Www, multiplicity=Multiplicity(1, 1)),
        Property(name="DBLP_Www", type=DBLP_Editor, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_DBLP_Article_Record = Generalization(general=Record, specific=DBLP_Article)
gen_DBLP_Book_Record = Generalization(general=Record, specific=DBLP_Book)
gen_DBLP_InCollection_Record = Generalization(general=Record, specific=DBLP_InCollection)
gen_DBLP_InProceedings_Record = Generalization(general=Record, specific=DBLP_InProceedings)
gen_DBLP_MastersThesis_Record = Generalization(general=Record, specific=DBLP_MastersThesis)
gen_DBLP_Proceedings_Record = Generalization(general=Record, specific=DBLP_Proceedings)
gen_DBLP_PhDThesis_Record = Generalization(general=Record, specific=DBLP_PhDThesis)
gen_DBLP_Www_Record = Generalization(general=Record, specific=DBLP_Www)

# Domain Model
domain_model = DomainModel(
    name="DBLP",
    types={DBLP_Journal, DBLP_Record, DBLP_Author, DBLP_Article, Record, DBLP_InCollection, DBLP_Book, DBLP_Publisher, DBLP_Editor, DBLP_Organization, DBLP_InProceedings, DBLP_MastersThesis, DBLP_School, DBLP_Proceedings, DBLP_PhDThesis, DBLP_Www},
    associations={journal1, authors0, records2, articles3, publisher4, editors11, editors5, sponsoredBy6, publisher8, editors20, publisher22, sponsoredBy25, organization13, publisher16, school19, school28, editors30},
    generalizations={gen_DBLP_Article_Record, gen_DBLP_Book_Record, gen_DBLP_InCollection_Record, gen_DBLP_InProceedings_Record, gen_DBLP_MastersThesis_Record, gen_DBLP_Proceedings_Record, gen_DBLP_PhDThesis_Record, gen_DBLP_Www_Record},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)