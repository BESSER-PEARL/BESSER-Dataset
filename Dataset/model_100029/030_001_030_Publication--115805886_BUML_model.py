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
publication_Article = Class(name="publication_Article")
BiblioReference = Class(name="BiblioReference")
publication_BiblioReference = Class(name="publication_BiblioReference")
SimpleCitation = Class(name="SimpleCitation")
publication_SimpleOntologyTerm = Class(name="publication_SimpleOntologyTerm")
publication_LegalEntity = Class(name="publication_LegalEntity")
publication_OrderedLegalEntitySet = Class(name="publication_OrderedLegalEntitySet")
publication_Content = Class(name="publication_Content")
publication_Indexing = Class(name="publication_Indexing")
publication_BiblioReferenceSet = Class(name="publication_BiblioReferenceSet")
SimpleIdentifier = Class(name="SimpleIdentifier")
SimpleFeature = Class(name="SimpleFeature")
publication_SimpleCitation = Class(name="publication_SimpleCitation")
publication_Book = Class(name="publication_Book")
publication_BookArticle = Class(name="publication_BookArticle")
Article = Class(name="Article")
publication_Contact = Class(name="publication_Contact")
publication_Ontology = Class(name="publication_Ontology")
publication_Journal = Class(name="publication_Journal")
publication_JournalArticle = Class(name="publication_JournalArticle")
publication_JournalIssue = Class(name="publication_JournalIssue")
Journal = Class(name="Journal")
publication_TechnicalReport = Class(name="publication_TechnicalReport")
publication_Thesis = Class(name="publication_Thesis")
publication_Organization = Class(name="publication_Organization")
publication_Multimedia = Class(name="publication_Multimedia")
publication_Proceeding = Class(name="publication_Proceeding")
publication_Protocol = Class(name="publication_Protocol")
publication_SimpleFeature = Class(name="publication_SimpleFeature")
publication_WebResource = Class(name="publication_WebResource")

# publication_Article class attributes and methods
publication_Article_lastPage: Property = Property(name="lastPage", type=StringType)
publication_Article_firstPage: Property = Property(name="firstPage", type=StringType)
publication_Article.attributes={publication_Article_firstPage, publication_Article_lastPage}

# BiblioReference class attributes and methods

# publication_BiblioReference class attributes and methods

# SimpleCitation class attributes and methods

# publication_SimpleOntologyTerm class attributes and methods

# publication_LegalEntity class attributes and methods

# publication_OrderedLegalEntitySet class attributes and methods

# publication_Content class attributes and methods
publication_Content_body: Property = Property(name="body", type=StringType)
publication_Content.attributes={publication_Content_body}

# publication_Indexing class attributes and methods
publication_Indexing_keywords: Property = Property(name="keywords", type=StringType)
publication_Indexing.attributes={publication_Indexing_keywords}

# publication_BiblioReferenceSet class attributes and methods

# SimpleIdentifier class attributes and methods

# SimpleFeature class attributes and methods

# publication_SimpleCitation class attributes and methods
publication_SimpleCitation_source: Property = Property(name="source", type=StringType)
publication_SimpleCitation_authorList: Property = Property(name="authorList", type=StringType)
publication_SimpleCitation_date: Property = Property(name="date", type=DateType)
publication_SimpleCitation.attributes={publication_SimpleCitation_date, publication_SimpleCitation_source, publication_SimpleCitation_authorList}

# publication_Book class attributes and methods
publication_Book_iSBN: Property = Property(name="iSBN", type=StringType)
publication_Book_volume: Property = Property(name="volume", type=StringType)
publication_Book_edition: Property = Property(name="edition", type=StringType)
publication_Book_series: Property = Property(name="series", type=StringType)
publication_Book.attributes={publication_Book_iSBN, publication_Book_edition, publication_Book_series, publication_Book_volume}

# publication_BookArticle class attributes and methods
publication_BookArticle_section: Property = Property(name="section", type=StringType)
publication_BookArticle.attributes={publication_BookArticle_section}

# Article class attributes and methods

# publication_Contact class attributes and methods

# publication_Ontology class attributes and methods

# publication_Journal class attributes and methods
publication_Journal_iSSN: Property = Property(name="iSSN", type=StringType)
publication_Journal.attributes={publication_Journal_iSSN}

# publication_JournalArticle class attributes and methods

# publication_JournalIssue class attributes and methods
publication_JournalIssue_volume: Property = Property(name="volume", type=StringType)
publication_JournalIssue_issue: Property = Property(name="issue", type=StringType)
publication_JournalIssue_issueSupplement: Property = Property(name="issueSupplement", type=StringType)
publication_JournalIssue.attributes={publication_JournalIssue_issueSupplement, publication_JournalIssue_volume, publication_JournalIssue_issue}

# Journal class attributes and methods

# publication_TechnicalReport class attributes and methods

# publication_Thesis class attributes and methods

# publication_Organization class attributes and methods

# publication_Multimedia class attributes and methods

# publication_Proceeding class attributes and methods

# publication_Protocol class attributes and methods

# publication_SimpleFeature class attributes and methods

# publication_WebResource class attributes and methods
publication_WebResource_uRL: Property = Property(name="uRL", type=StringType)
publication_WebResource.attributes={publication_WebResource_uRL}

# Relationships
language0: BinaryAssociation = BinaryAssociation(
    name="language0",
    ends={
        Property(name="publication_SimpleOntologyTerm", type=publication_BiblioReference, multiplicity=Multiplicity(1, 1)),
        Property(name="publication_BiblioReference", type=publication_SimpleOntologyTerm, multiplicity=Multiplicity(0, 1))
    }
)
format1: BinaryAssociation = BinaryAssociation(
    name="format1",
    ends={
        Property(name="publication_SimpleOntologyTerm3", type=publication_BiblioReference, multiplicity=Multiplicity(1, 1)),
        Property(name="publication_BiblioReference2", type=publication_SimpleOntologyTerm, multiplicity=Multiplicity(0, 1))
    }
)
publisher4: BinaryAssociation = BinaryAssociation(
    name="publisher4",
    ends={
        Property(name="publication_LegalEntity", type=publication_BiblioReference, multiplicity=Multiplicity(1, 1)),
        Property(name="publication_BiblioReference5", type=publication_LegalEntity, multiplicity=Multiplicity(0, 1))
    }
)
authors6: BinaryAssociation = BinaryAssociation(
    name="authors6",
    ends={
        Property(name="publication_OrderedLegalEntitySet", type=publication_BiblioReference, multiplicity=Multiplicity(1, 1)),
        Property(name="publication_BiblioReference7", type=publication_OrderedLegalEntitySet, multiplicity=Multiplicity(0, 1))
    }
)
contributors8: BinaryAssociation = BinaryAssociation(
    name="contributors8",
    ends={
        Property(name="publication_OrderedLegalEntitySet10", type=publication_BiblioReference, multiplicity=Multiplicity(1, 1)),
        Property(name="publication_BiblioReference9", type=publication_OrderedLegalEntitySet, multiplicity=Multiplicity(0, 1))
    }
)
content11: BinaryAssociation = BinaryAssociation(
    name="content11",
    ends={
        Property(name="publication_Content", type=publication_BiblioReference, multiplicity=Multiplicity(1, 1)),
        Property(name="publication_BiblioReference12", type=publication_Content, multiplicity=Multiplicity(1, 1))
    }
)
indexings13: BinaryAssociation = BinaryAssociation(
    name="indexings13",
    ends={
        Property(name="Indexing", type=publication_BiblioReference, multiplicity=Multiplicity(1, 1)),
        Property(name="reference", type=publication_Indexing, multiplicity=Multiplicity(0, 9999))
    }
)
book18: BinaryAssociation = BinaryAssociation(
    name="book18",
    ends={
        Property(name="Book", type=publication_BookArticle, multiplicity=Multiplicity(1, 1)),
        Property(name="articles", type=publication_Book, multiplicity=Multiplicity(0, 9999))
    }
)
citations14: BinaryAssociation = BinaryAssociation(
    name="citations14",
    ends={
        Property(name="publication_SimpleCitation", type=publication_BiblioReferenceSet, multiplicity=Multiplicity(1, 1)),
        Property(name="publication_BiblioReferenceSet", type=publication_SimpleCitation, multiplicity=Multiplicity(0, 9999))
    }
)
editors15: BinaryAssociation = BinaryAssociation(
    name="editors15",
    ends={
        Property(name="publication_OrderedLegalEntitySet16", type=publication_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="publication_Book", type=publication_OrderedLegalEntitySet, multiplicity=Multiplicity(0, 1))
    }
)
articles17: BinaryAssociation = BinaryAssociation(
    name="articles17",
    ends={
        Property(name="BookArticle", type=publication_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="book", type=publication_BookArticle, multiplicity=Multiplicity(0, 9999))
    }
)
subjectHeadings28: BinaryAssociation = BinaryAssociation(
    name="subjectHeadings28",
    ends={
        Property(name="publication_SimpleOntologyTerm30", type=publication_Indexing, multiplicity=Multiplicity(1, 1)),
        Property(name="publication_Indexing29", type=publication_SimpleOntologyTerm, multiplicity=Multiplicity(0, 9999))
    }
)
classificationCodes31: BinaryAssociation = BinaryAssociation(
    name="classificationCodes31",
    ends={
        Property(name="publication_SimpleOntologyTerm33", type=publication_Indexing, multiplicity=Multiplicity(1, 1)),
        Property(name="publication_Indexing32", type=publication_SimpleOntologyTerm, multiplicity=Multiplicity(0, 9999))
    }
)
biblioReference19: BinaryAssociation = BinaryAssociation(
    name="biblioReference19",
    ends={
        Property(name="publication_BiblioReference21", type=publication_Content, multiplicity=Multiplicity(1, 1)),
        Property(name="publication_Content20", type=publication_BiblioReference, multiplicity=Multiplicity(1, 1))
    }
)
librarian22: BinaryAssociation = BinaryAssociation(
    name="librarian22",
    ends={
        Property(name="publication_Contact", type=publication_Indexing, multiplicity=Multiplicity(1, 1)),
        Property(name="publication_Indexing", type=publication_Contact, multiplicity=Multiplicity(0, 1))
    }
)
authority23: BinaryAssociation = BinaryAssociation(
    name="authority23",
    ends={
        Property(name="publication_LegalEntity25", type=publication_Indexing, multiplicity=Multiplicity(1, 1)),
        Property(name="publication_Indexing24", type=publication_LegalEntity, multiplicity=Multiplicity(0, 1))
    }
)
subjectHeadingOntology26: BinaryAssociation = BinaryAssociation(
    name="subjectHeadingOntology26",
    ends={
        Property(name="publication_Ontology", type=publication_Indexing, multiplicity=Multiplicity(1, 1)),
        Property(name="publication_Indexing27", type=publication_Ontology, multiplicity=Multiplicity(0, 1))
    }
)
articles39: BinaryAssociation = BinaryAssociation(
    name="articles39",
    ends={
        Property(name="JournalArticle", type=publication_JournalIssue, multiplicity=Multiplicity(1, 1)),
        Property(name="journalIssue", type=publication_JournalArticle, multiplicity=Multiplicity(0, 9999))
    }
)
reference34: BinaryAssociation = BinaryAssociation(
    name="reference34",
    ends={
        Property(name="BiblioReference", type=publication_Indexing, multiplicity=Multiplicity(1, 1)),
        Property(name="indexings", type=publication_BiblioReference, multiplicity=Multiplicity(1, 1))
    }
)
abbreviation35: BinaryAssociation = BinaryAssociation(
    name="abbreviation35",
    ends={
        Property(name="publication_SimpleOntologyTerm36", type=publication_Journal, multiplicity=Multiplicity(1, 1)),
        Property(name="publication_Journal", type=publication_SimpleOntologyTerm, multiplicity=Multiplicity(0, 1))
    }
)
journalIssue37: BinaryAssociation = BinaryAssociation(
    name="journalIssue37",
    ends={
        Property(name="JournalIssue", type=publication_JournalArticle, multiplicity=Multiplicity(1, 1)),
        Property(name="articles38", type=publication_JournalIssue, multiplicity=Multiplicity(1, 1))
    }
)
institution41: BinaryAssociation = BinaryAssociation(
    name="institution41",
    ends={
        Property(name="publication_Organization", type=publication_Thesis, multiplicity=Multiplicity(1, 1)),
        Property(name="publication_Thesis", type=publication_Organization, multiplicity=Multiplicity(1, 1))
    }
)
parameters40: BinaryAssociation = BinaryAssociation(
    name="parameters40",
    ends={
        Property(name="publication_SimpleFeature", type=publication_Protocol, multiplicity=Multiplicity(1, 1)),
        Property(name="publication_Protocol", type=publication_SimpleFeature, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_publication_Article_BiblioReference = Generalization(general=BiblioReference, specific=publication_Article)
gen_publication_BiblioReference_SimpleCitation = Generalization(general=SimpleCitation, specific=publication_BiblioReference)
gen_publication_BiblioReferenceSet_SimpleIdentifier = Generalization(general=SimpleIdentifier, specific=publication_BiblioReferenceSet)
gen_publication_Content_SimpleFeature = Generalization(general=SimpleFeature, specific=publication_Content)
gen_publication_Book_BiblioReference = Generalization(general=BiblioReference, specific=publication_Book)
gen_publication_BookArticle_Article = Generalization(general=Article, specific=publication_BookArticle)
gen_publication_Journal_BiblioReference = Generalization(general=BiblioReference, specific=publication_Journal)
gen_publication_JournalArticle_Article = Generalization(general=Article, specific=publication_JournalArticle)
gen_publication_JournalIssue_Journal = Generalization(general=Journal, specific=publication_JournalIssue)
gen_publication_TechnicalReport_BiblioReference = Generalization(general=BiblioReference, specific=publication_TechnicalReport)
gen_publication_Thesis_BiblioReference = Generalization(general=BiblioReference, specific=publication_Thesis)
gen_publication_Multimedia_BiblioReference = Generalization(general=BiblioReference, specific=publication_Multimedia)
gen_publication_Proceeding_BiblioReference = Generalization(general=BiblioReference, specific=publication_Proceeding)
gen_publication_Protocol_BiblioReference = Generalization(general=BiblioReference, specific=publication_Protocol)
gen_publication_SimpleCitation_SimpleFeature = Generalization(general=SimpleFeature, specific=publication_SimpleCitation)
gen_publication_WebResource_BiblioReference = Generalization(general=BiblioReference, specific=publication_WebResource)

# Domain Model
domain_model = DomainModel(
    name="publication",
    types={publication_Article, BiblioReference, publication_BiblioReference, SimpleCitation, publication_SimpleOntologyTerm, publication_LegalEntity, publication_OrderedLegalEntitySet, publication_Content, publication_Indexing, publication_BiblioReferenceSet, SimpleIdentifier, SimpleFeature, publication_SimpleCitation, publication_Book, publication_BookArticle, Article, publication_Contact, publication_Ontology, publication_Journal, publication_JournalArticle, publication_JournalIssue, Journal, publication_TechnicalReport, publication_Thesis, publication_Organization, publication_Multimedia, publication_Proceeding, publication_Protocol, publication_SimpleFeature, publication_WebResource},
    associations={language0, format1, publisher4, authors6, contributors8, content11, indexings13, book18, citations14, editors15, articles17, subjectHeadings28, classificationCodes31, biblioReference19, librarian22, authority23, subjectHeadingOntology26, articles39, reference34, abbreviation35, journalIssue37, institution41, parameters40},
    generalizations={gen_publication_Article_BiblioReference, gen_publication_BiblioReference_SimpleCitation, gen_publication_BiblioReferenceSet_SimpleIdentifier, gen_publication_Content_SimpleFeature, gen_publication_Book_BiblioReference, gen_publication_BookArticle_Article, gen_publication_Journal_BiblioReference, gen_publication_JournalArticle_Article, gen_publication_JournalIssue_Journal, gen_publication_TechnicalReport_BiblioReference, gen_publication_Thesis_BiblioReference, gen_publication_Multimedia_BiblioReference, gen_publication_Proceeding_BiblioReference, gen_publication_Protocol_BiblioReference, gen_publication_SimpleCitation_SimpleFeature, gen_publication_WebResource_BiblioReference},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)