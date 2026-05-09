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
publicationExample_Researcher = Class(name="publicationExample_Researcher")
Human = Class(name="Human")
publicationExample_Publication = Class(name="publicationExample_Publication", is_abstract=True)
publicationExample_Humanity = Class(name="publicationExample_Humanity")
publicationExample_Human = Class(name="publicationExample_Human")
publicationExample_JournalArticle = Class(name="publicationExample_JournalArticle")
Publication = Class(name="Publication")
publicationExample_Paper = Class(name="publicationExample_Paper")
publicationExample_WorkshopPaper = Class(name="publicationExample_WorkshopPaper")
Paper = Class(name="Paper")
publicationExample_ConferencePaper = Class(name="publicationExample_ConferencePaper")
publicationExample_Books = Class(name="publicationExample_Books")
publicationExample_Thesis = Class(name="publicationExample_Thesis")
publicationExample_Other = Class(name="publicationExample_Other")
publicationExample_Editorship = Class(name="publicationExample_Editorship")

# publicationExample_Researcher class attributes and methods

# Human class attributes and methods

# publicationExample_Publication class attributes and methods

# publicationExample_Humanity class attributes and methods

# publicationExample_Human class attributes and methods

# publicationExample_JournalArticle class attributes and methods

# Publication class attributes and methods

# publicationExample_Paper class attributes and methods

# publicationExample_WorkshopPaper class attributes and methods

# Paper class attributes and methods

# publicationExample_ConferencePaper class attributes and methods

# publicationExample_Books class attributes and methods

# publicationExample_Thesis class attributes and methods

# publicationExample_Other class attributes and methods

# publicationExample_Editorship class attributes and methods

# Relationships
contributedTo0: BinaryAssociation = BinaryAssociation(
    name="contributedTo0",
    ends={
        Property(name="publicationExample_Publication", type=publicationExample_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="publicationExample_Researcher", type=publicationExample_Publication, multiplicity=Multiplicity(0, 9999))
    }
)
humans1: BinaryAssociation = BinaryAssociation(
    name="humans1",
    ends={
        Property(name="publicationExample_Human", type=publicationExample_Humanity, multiplicity=Multiplicity(1, 1)),
        Property(name="publicationExample_Humanity", type=publicationExample_Human, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
publications2: BinaryAssociation = BinaryAssociation(
    name="publications2",
    ends={
        Property(name="publicationExample_Publication4", type=publicationExample_Humanity, multiplicity=Multiplicity(1, 1)),
        Property(name="publicationExample_Humanity3", type=publicationExample_Publication, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_publicationExample_Researcher_Human = Generalization(general=Human, specific=publicationExample_Researcher)
gen_publicationExample_JournalArticle_Publication = Generalization(general=Publication, specific=publicationExample_JournalArticle)
gen_publicationExample_Paper_Publication = Generalization(general=Publication, specific=publicationExample_Paper)
gen_publicationExample_WorkshopPaper_Paper = Generalization(general=Paper, specific=publicationExample_WorkshopPaper)
gen_publicationExample_ConferencePaper_Paper = Generalization(general=Paper, specific=publicationExample_ConferencePaper)
gen_publicationExample_Books_Publication = Generalization(general=Publication, specific=publicationExample_Books)
gen_publicationExample_Thesis_Publication = Generalization(general=Publication, specific=publicationExample_Thesis)
gen_publicationExample_Other_Publication = Generalization(general=Publication, specific=publicationExample_Other)
gen_publicationExample_Editorship_Publication = Generalization(general=Publication, specific=publicationExample_Editorship)

# Domain Model
domain_model = DomainModel(
    name="publicationExample",
    types={publicationExample_Researcher, Human, publicationExample_Publication, publicationExample_Humanity, publicationExample_Human, publicationExample_JournalArticle, Publication, publicationExample_Paper, publicationExample_WorkshopPaper, Paper, publicationExample_ConferencePaper, publicationExample_Books, publicationExample_Thesis, publicationExample_Other, publicationExample_Editorship},
    associations={contributedTo0, humans1, publications2},
    generalizations={gen_publicationExample_Researcher_Human, gen_publicationExample_JournalArticle_Publication, gen_publicationExample_Paper_Publication, gen_publicationExample_WorkshopPaper_Paper, gen_publicationExample_ConferencePaper_Paper, gen_publicationExample_Books_Publication, gen_publicationExample_Thesis_Publication, gen_publicationExample_Other_Publication, gen_publicationExample_Editorship_Publication},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)