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
wikigen_Container = Class(name="wikigen_Container")
wikigen_GenLatexDocument = Class(name="wikigen_GenLatexDocument")
wikigen_GenHtmlDocument = Class(name="wikigen_GenHtmlDocument")
wikigen_HtmlProfile = Class(name="wikigen_HtmlProfile", is_abstract=True)
wikigen_Document = Class(name="wikigen_Document")
wikigen_Article = Class(name="wikigen_Article")
HtmlProfile = Class(name="HtmlProfile")

# wikigen_Container class attributes and methods

# wikigen_GenLatexDocument class attributes and methods
wikigen_GenLatexDocument_filename: Property = Property(name="filename", type=StringType)
wikigen_GenLatexDocument_title: Property = Property(name="title", type=StringType)
wikigen_GenLatexDocument_authors: Property = Property(name="authors", type=StringType)
wikigen_GenLatexDocument.attributes={wikigen_GenLatexDocument_title, wikigen_GenLatexDocument_filename, wikigen_GenLatexDocument_authors}

# wikigen_GenHtmlDocument class attributes and methods
wikigen_GenHtmlDocument_filename: Property = Property(name="filename", type=StringType)
wikigen_GenHtmlDocument.attributes={wikigen_GenHtmlDocument_filename}

# wikigen_HtmlProfile class attributes and methods

# wikigen_Document class attributes and methods

# wikigen_Article class attributes and methods
wikigen_Article_nbColumns: Property = Property(name="nbColumns", type=IntegerType)
wikigen_Article_generateTOC: Property = Property(name="generateTOC", type=BooleanType)
wikigen_Article.attributes={wikigen_Article_nbColumns, wikigen_Article_generateTOC}

# HtmlProfile class attributes and methods

# Relationships
roots2: BinaryAssociation = BinaryAssociation(
    name="roots2",
    ends={
        Property(name="wikigen_Document", type=wikigen_GenHtmlDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="wikigen_GenHtmlDocument3", type=wikigen_Document, multiplicity=Multiplicity(0, 9999))
    }
)
roots0: BinaryAssociation = BinaryAssociation(
    name="roots0",
    ends={
        Property(name="wikigen_Container", type=wikigen_GenLatexDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="wikigen_GenLatexDocument", type=wikigen_Container, multiplicity=Multiplicity(0, 9999))
    }
)
style1: BinaryAssociation = BinaryAssociation(
    name="style1",
    ends={
        Property(name="wikigen_HtmlProfile", type=wikigen_GenHtmlDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="wikigen_GenHtmlDocument", type=wikigen_HtmlProfile, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_wikigen_Article_HtmlProfile = Generalization(general=HtmlProfile, specific=wikigen_Article)

# Domain Model
domain_model = DomainModel(
    name="wikigen",
    types={wikigen_Container, wikigen_GenLatexDocument, wikigen_GenHtmlDocument, wikigen_HtmlProfile, wikigen_Document, wikigen_Article, HtmlProfile},
    associations={roots2, roots0, style1},
    generalizations={gen_wikigen_Article_HtmlProfile},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)