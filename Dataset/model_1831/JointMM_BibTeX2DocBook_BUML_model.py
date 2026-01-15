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
jointPackage_BibTeX2DocBook_JointMM = Class(name="jointPackage::BibTeX2DocBook::JointMM")
SrcMasterThesis = Class(name="SrcMasterThesis")
jointPackage_BibTeX2DocBook_SrcBibTeXFile = Class(name="jointPackage::BibTeX2DocBook::SrcBibTeXFile")
SrcBibTeXEntry = Class(name="SrcBibTeXEntry")
jointPackage_BibTeX2DocBook_SrcArticle = Class(name="jointPackage::BibTeX2DocBook::SrcArticle")
SrcAuthoredEntry = Class(name="SrcAuthoredEntry")
SrcDatedEntry = Class(name="SrcDatedEntry")
SrcTitledEntry = Class(name="SrcTitledEntry")
jointPackage_BibTeX2DocBook_SrcTechReport = Class(name="jointPackage::BibTeX2DocBook::SrcTechReport")
TrgDocBook = Class(name="TrgDocBook")
jointPackage_BibTeX2DocBook_SrcBooklet = Class(name="jointPackage::BibTeX2DocBook::SrcBooklet")
jointPackage_BibTeX2DocBook_SrcBook = Class(name="jointPackage::BibTeX2DocBook::SrcBook")
jointPackage_BibTeX2DocBook_SrcInCollection = Class(name="jointPackage::BibTeX2DocBook::SrcInCollection")
SrcBook = Class(name="SrcBook")
jointPackage_BibTeX2DocBook_SrcInBook = Class(name="jointPackage::BibTeX2DocBook::SrcInBook")
jointPackage_BibTeX2DocBook_SrcPhDThesis = Class(name="jointPackage::BibTeX2DocBook::SrcPhDThesis")
SrcThesisEntry = Class(name="SrcThesisEntry")
jointPackage_BibTeX2DocBook_SrcMasterThesis = Class(name="jointPackage::BibTeX2DocBook::SrcMasterThesis")
jointPackage_BibTeX2DocBook_SrcAuthor = Class(name="jointPackage::BibTeX2DocBook::SrcAuthor")
jointPackage_BibTeX2DocBook_SrcBibTeXEntry = Class(name="jointPackage::BibTeX2DocBook::SrcBibTeXEntry", is_abstract=True)
jointPackage_BibTeX2DocBook_SrcAuthoredEntry = Class(name="jointPackage::BibTeX2DocBook::SrcAuthoredEntry", is_abstract=True)
SrcAuthor = Class(name="SrcAuthor")
jointPackage_BibTeX2DocBook_SrcDatedEntry = Class(name="jointPackage::BibTeX2DocBook::SrcDatedEntry", is_abstract=True)
jointPackage_BibTeX2DocBook_SrcTitledEntry = Class(name="jointPackage::BibTeX2DocBook::SrcTitledEntry", is_abstract=True)
jointPackage_BibTeX2DocBook_SrcUnpublished = Class(name="jointPackage::BibTeX2DocBook::SrcUnpublished")
jointPackage_BibTeX2DocBook_SrcManual = Class(name="jointPackage::BibTeX2DocBook::SrcManual")
jointPackage_BibTeX2DocBook_SrcProceedings = Class(name="jointPackage::BibTeX2DocBook::SrcProceedings")
jointPackage_BibTeX2DocBook_SrcInProceedings = Class(name="jointPackage::BibTeX2DocBook::SrcInProceedings")
SrcProceedings = Class(name="SrcProceedings")
SrcBookTitledEntry = Class(name="SrcBookTitledEntry")
jointPackage_BibTeX2DocBook_SrcThesisEntry = Class(name="jointPackage::BibTeX2DocBook::SrcThesisEntry", is_abstract=True)
jointPackage_BibTeX2DocBook_TrgDocBook = Class(name="jointPackage::BibTeX2DocBook::TrgDocBook")
TrgBook = Class(name="TrgBook")
jointPackage_BibTeX2DocBook_TrgBook = Class(name="jointPackage::BibTeX2DocBook::TrgBook")
TrgArticle = Class(name="TrgArticle")
jointPackage_BibTeX2DocBook_TrgTitledElement = Class(name="jointPackage::BibTeX2DocBook::TrgTitledElement", is_abstract=True)
jointPackage_BibTeX2DocBook_TrgArticle = Class(name="jointPackage::BibTeX2DocBook::TrgArticle")
TrgTitledElement = Class(name="TrgTitledElement")
jointPackage_BibTeX2DocBook_SrcBookTitledEntry = Class(name="jointPackage::BibTeX2DocBook::SrcBookTitledEntry", is_abstract=True)
jointPackage_BibTeX2DocBook_SrcMisc = Class(name="jointPackage::BibTeX2DocBook::SrcMisc")
TrgPara = Class(name="TrgPara")
jointPackage_BibTeX2DocBook_TrgSect1 = Class(name="jointPackage::BibTeX2DocBook::TrgSect1")
TrgSection = Class(name="TrgSection")
TrgSect2 = Class(name="TrgSect2")
jointPackage_BibTeX2DocBook_TrgSect2 = Class(name="jointPackage::BibTeX2DocBook::TrgSect2")
jointPackage_BibTeX2DocBook_TrgPara = Class(name="jointPackage::BibTeX2DocBook::TrgPara")
TrgSect1 = Class(name="TrgSect1")
jointPackage_BibTeX2DocBook_TrgSection = Class(name="jointPackage::BibTeX2DocBook::TrgSection", is_abstract=True)

# jointPackage_BibTeX2DocBook_JointMM class attributes and methods

# SrcMasterThesis class attributes and methods

# jointPackage_BibTeX2DocBook_SrcBibTeXFile class attributes and methods

# SrcBibTeXEntry class attributes and methods

# jointPackage_BibTeX2DocBook_SrcArticle class attributes and methods
jointPackage_BibTeX2DocBook_SrcArticle_journal: Property = Property(name="journal", type=StringType)
jointPackage_BibTeX2DocBook_SrcArticle.attributes={jointPackage_BibTeX2DocBook_SrcArticle_journal}

# SrcAuthoredEntry class attributes and methods

# SrcDatedEntry class attributes and methods

# SrcTitledEntry class attributes and methods

# jointPackage_BibTeX2DocBook_SrcTechReport class attributes and methods

# TrgDocBook class attributes and methods

# jointPackage_BibTeX2DocBook_SrcBooklet class attributes and methods

# jointPackage_BibTeX2DocBook_SrcBook class attributes and methods
jointPackage_BibTeX2DocBook_SrcBook_publisher: Property = Property(name="publisher", type=StringType)
jointPackage_BibTeX2DocBook_SrcBook.attributes={jointPackage_BibTeX2DocBook_SrcBook_publisher}

# jointPackage_BibTeX2DocBook_SrcInCollection class attributes and methods

# SrcBook class attributes and methods

# jointPackage_BibTeX2DocBook_SrcInBook class attributes and methods
jointPackage_BibTeX2DocBook_SrcInBook_chapter: Property = Property(name="chapter", type=IntegerType)
jointPackage_BibTeX2DocBook_SrcInBook.attributes={jointPackage_BibTeX2DocBook_SrcInBook_chapter}

# jointPackage_BibTeX2DocBook_SrcPhDThesis class attributes and methods

# SrcThesisEntry class attributes and methods

# jointPackage_BibTeX2DocBook_SrcMasterThesis class attributes and methods

# jointPackage_BibTeX2DocBook_SrcAuthor class attributes and methods
jointPackage_BibTeX2DocBook_SrcAuthor_author: Property = Property(name="author", type=StringType)
jointPackage_BibTeX2DocBook_SrcAuthor.attributes={jointPackage_BibTeX2DocBook_SrcAuthor_author}

# jointPackage_BibTeX2DocBook_SrcBibTeXEntry class attributes and methods
jointPackage_BibTeX2DocBook_SrcBibTeXEntry_id: Property = Property(name="id", type=StringType)
jointPackage_BibTeX2DocBook_SrcBibTeXEntry.attributes={jointPackage_BibTeX2DocBook_SrcBibTeXEntry_id}

# jointPackage_BibTeX2DocBook_SrcAuthoredEntry class attributes and methods

# SrcAuthor class attributes and methods

# jointPackage_BibTeX2DocBook_SrcDatedEntry class attributes and methods
jointPackage_BibTeX2DocBook_SrcDatedEntry_year: Property = Property(name="year", type=StringType)
jointPackage_BibTeX2DocBook_SrcDatedEntry.attributes={jointPackage_BibTeX2DocBook_SrcDatedEntry_year}

# jointPackage_BibTeX2DocBook_SrcTitledEntry class attributes and methods
jointPackage_BibTeX2DocBook_SrcTitledEntry_title: Property = Property(name="title", type=StringType)
jointPackage_BibTeX2DocBook_SrcTitledEntry.attributes={jointPackage_BibTeX2DocBook_SrcTitledEntry_title}

# jointPackage_BibTeX2DocBook_SrcUnpublished class attributes and methods
jointPackage_BibTeX2DocBook_SrcUnpublished_note: Property = Property(name="note", type=StringType)
jointPackage_BibTeX2DocBook_SrcUnpublished.attributes={jointPackage_BibTeX2DocBook_SrcUnpublished_note}

# jointPackage_BibTeX2DocBook_SrcManual class attributes and methods

# jointPackage_BibTeX2DocBook_SrcProceedings class attributes and methods

# jointPackage_BibTeX2DocBook_SrcInProceedings class attributes and methods

# SrcProceedings class attributes and methods

# SrcBookTitledEntry class attributes and methods

# jointPackage_BibTeX2DocBook_SrcThesisEntry class attributes and methods
jointPackage_BibTeX2DocBook_SrcThesisEntry_school: Property = Property(name="school", type=StringType)
jointPackage_BibTeX2DocBook_SrcThesisEntry.attributes={jointPackage_BibTeX2DocBook_SrcThesisEntry_school}

# jointPackage_BibTeX2DocBook_TrgDocBook class attributes and methods

# TrgBook class attributes and methods

# jointPackage_BibTeX2DocBook_TrgBook class attributes and methods

# TrgArticle class attributes and methods

# jointPackage_BibTeX2DocBook_TrgTitledElement class attributes and methods
jointPackage_BibTeX2DocBook_TrgTitledElement_title: Property = Property(name="title", type=StringType)
jointPackage_BibTeX2DocBook_TrgTitledElement.attributes={jointPackage_BibTeX2DocBook_TrgTitledElement_title}

# jointPackage_BibTeX2DocBook_TrgArticle class attributes and methods

# TrgTitledElement class attributes and methods

# jointPackage_BibTeX2DocBook_SrcBookTitledEntry class attributes and methods
jointPackage_BibTeX2DocBook_SrcBookTitledEntry_booktitle: Property = Property(name="booktitle", type=StringType)
jointPackage_BibTeX2DocBook_SrcBookTitledEntry.attributes={jointPackage_BibTeX2DocBook_SrcBookTitledEntry_booktitle}

# jointPackage_BibTeX2DocBook_SrcMisc class attributes and methods

# TrgPara class attributes and methods

# jointPackage_BibTeX2DocBook_TrgSect1 class attributes and methods

# TrgSection class attributes and methods

# TrgSect2 class attributes and methods

# jointPackage_BibTeX2DocBook_TrgSect2 class attributes and methods

# jointPackage_BibTeX2DocBook_TrgPara class attributes and methods
jointPackage_BibTeX2DocBook_TrgPara_content: Property = Property(name="content", type=StringType)
jointPackage_BibTeX2DocBook_TrgPara.attributes={jointPackage_BibTeX2DocBook_TrgPara_content}

# TrgSect1 class attributes and methods

# jointPackage_BibTeX2DocBook_TrgSection class attributes and methods

# Relationships
sourceRoot0: BinaryAssociation = BinaryAssociation(
    name="sourceRoot0",
    ends={
        Property(name="SrcMasterThesis", type=jointPackage_BibTeX2DocBook_JointMM, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_BibTeX2DocBook_JointMM", type=SrcMasterThesis, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
entries3: BinaryAssociation = BinaryAssociation(
    name="entries3",
    ends={
        Property(name="SrcBibTeXEntry", type=jointPackage_BibTeX2DocBook_SrcBibTeXFile, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_BibTeX2DocBook_SrcBibTeXFile", type=SrcBibTeXEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
targetRoot1: BinaryAssociation = BinaryAssociation(
    name="targetRoot1",
    ends={
        Property(name="TrgDocBook", type=jointPackage_BibTeX2DocBook_JointMM, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_BibTeX2DocBook_JointMM2", type=TrgDocBook, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
authors4: BinaryAssociation = BinaryAssociation(
    name="authors4",
    ends={
        Property(name="SrcAuthor", type=jointPackage_BibTeX2DocBook_SrcAuthoredEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_BibTeX2DocBook_SrcAuthoredEntry", type=SrcAuthor, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
books5: BinaryAssociation = BinaryAssociation(
    name="books5",
    ends={
        Property(name="TrgBook", type=jointPackage_BibTeX2DocBook_TrgDocBook, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_BibTeX2DocBook_TrgDocBook", type=TrgBook, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
articles6: BinaryAssociation = BinaryAssociation(
    name="articles6",
    ends={
        Property(name="TrgArticle", type=jointPackage_BibTeX2DocBook_TrgBook, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_BibTeX2DocBook_TrgBook", type=TrgArticle, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
paras8: BinaryAssociation = BinaryAssociation(
    name="paras8",
    ends={
        Property(name="#", type=jointPackage_BibTeX2DocBook_TrgSection, multiplicity=Multiplicity(1, 1)),
        Property(name="0", type=TrgPara, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
sections_29: BinaryAssociation = BinaryAssociation(
    name="sections_29",
    ends={
        Property(name="TrgSect2", type=jointPackage_BibTeX2DocBook_TrgSect1, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_BibTeX2DocBook_TrgSect1", type=TrgSect2, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
section10: BinaryAssociation = BinaryAssociation(
    name="section10",
    ends={
        Property(name="#12", type=jointPackage_BibTeX2DocBook_TrgPara, multiplicity=Multiplicity(1, 1)),
        Property(name="011", type=TrgSection, multiplicity=Multiplicity(1, 1))
    }
)
sections_17: BinaryAssociation = BinaryAssociation(
    name="sections_17",
    ends={
        Property(name="TrgSect1", type=jointPackage_BibTeX2DocBook_TrgArticle, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_BibTeX2DocBook_TrgArticle", type=TrgSect1, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)

# Generalizations
gen_jointPackage_BibTeX2DocBook_SrcArticle_SrcAuthoredEntry = Generalization(general=SrcAuthoredEntry, specific=jointPackage_BibTeX2DocBook_SrcArticle)
gen_jointPackage_BibTeX2DocBook_SrcArticle_SrcDatedEntry = Generalization(general=SrcDatedEntry, specific=jointPackage_BibTeX2DocBook_SrcArticle)
gen_jointPackage_BibTeX2DocBook_SrcArticle_SrcTitledEntry = Generalization(general=SrcTitledEntry, specific=jointPackage_BibTeX2DocBook_SrcArticle)
gen_jointPackage_BibTeX2DocBook_SrcTechReport_SrcAuthoredEntry = Generalization(general=SrcAuthoredEntry, specific=jointPackage_BibTeX2DocBook_SrcTechReport)
gen_jointPackage_BibTeX2DocBook_SrcTechReport_SrcDatedEntry = Generalization(general=SrcDatedEntry, specific=jointPackage_BibTeX2DocBook_SrcTechReport)
gen_jointPackage_BibTeX2DocBook_SrcTechReport_SrcTitledEntry = Generalization(general=SrcTitledEntry, specific=jointPackage_BibTeX2DocBook_SrcTechReport)
gen_jointPackage_BibTeX2DocBook_SrcBooklet_SrcDatedEntry = Generalization(general=SrcDatedEntry, specific=jointPackage_BibTeX2DocBook_SrcBooklet)
gen_jointPackage_BibTeX2DocBook_SrcBook_SrcAuthoredEntry = Generalization(general=SrcAuthoredEntry, specific=jointPackage_BibTeX2DocBook_SrcBook)
gen_jointPackage_BibTeX2DocBook_SrcBook_SrcDatedEntry = Generalization(general=SrcDatedEntry, specific=jointPackage_BibTeX2DocBook_SrcBook)
gen_jointPackage_BibTeX2DocBook_SrcBook_SrcTitledEntry = Generalization(general=SrcTitledEntry, specific=jointPackage_BibTeX2DocBook_SrcBook)
gen_jointPackage_BibTeX2DocBook_SrcInCollection_SrcBook = Generalization(general=SrcBook, specific=jointPackage_BibTeX2DocBook_SrcInCollection)
gen_jointPackage_BibTeX2DocBook_SrcInCollection_SrcBookTitledEntry = Generalization(general=SrcBookTitledEntry, specific=jointPackage_BibTeX2DocBook_SrcInCollection)
gen_jointPackage_BibTeX2DocBook_SrcInBook_SrcBook = Generalization(general=SrcBook, specific=jointPackage_BibTeX2DocBook_SrcInBook)
gen_jointPackage_BibTeX2DocBook_SrcPhDThesis_SrcThesisEntry = Generalization(general=SrcThesisEntry, specific=jointPackage_BibTeX2DocBook_SrcPhDThesis)
gen_jointPackage_BibTeX2DocBook_SrcMasterThesis_SrcThesisEntry = Generalization(general=SrcThesisEntry, specific=jointPackage_BibTeX2DocBook_SrcMasterThesis)
gen_jointPackage_BibTeX2DocBook_SrcAuthoredEntry_SrcBibTeXEntry = Generalization(general=SrcBibTeXEntry, specific=jointPackage_BibTeX2DocBook_SrcAuthoredEntry)
gen_jointPackage_BibTeX2DocBook_SrcDatedEntry_SrcBibTeXEntry = Generalization(general=SrcBibTeXEntry, specific=jointPackage_BibTeX2DocBook_SrcDatedEntry)
gen_jointPackage_BibTeX2DocBook_SrcTitledEntry_SrcBibTeXEntry = Generalization(general=SrcBibTeXEntry, specific=jointPackage_BibTeX2DocBook_SrcTitledEntry)
gen_jointPackage_BibTeX2DocBook_SrcUnpublished_SrcAuthoredEntry = Generalization(general=SrcAuthoredEntry, specific=jointPackage_BibTeX2DocBook_SrcUnpublished)
gen_jointPackage_BibTeX2DocBook_SrcUnpublished_SrcTitledEntry = Generalization(general=SrcTitledEntry, specific=jointPackage_BibTeX2DocBook_SrcUnpublished)
gen_jointPackage_BibTeX2DocBook_SrcManual_SrcTitledEntry = Generalization(general=SrcTitledEntry, specific=jointPackage_BibTeX2DocBook_SrcManual)
gen_jointPackage_BibTeX2DocBook_SrcProceedings_SrcDatedEntry = Generalization(general=SrcDatedEntry, specific=jointPackage_BibTeX2DocBook_SrcProceedings)
gen_jointPackage_BibTeX2DocBook_SrcProceedings_SrcTitledEntry = Generalization(general=SrcTitledEntry, specific=jointPackage_BibTeX2DocBook_SrcProceedings)
gen_jointPackage_BibTeX2DocBook_SrcInProceedings_SrcProceedings = Generalization(general=SrcProceedings, specific=jointPackage_BibTeX2DocBook_SrcInProceedings)
gen_jointPackage_BibTeX2DocBook_SrcInProceedings_SrcAuthoredEntry = Generalization(general=SrcAuthoredEntry, specific=jointPackage_BibTeX2DocBook_SrcInProceedings)
gen_jointPackage_BibTeX2DocBook_SrcInProceedings_SrcBookTitledEntry = Generalization(general=SrcBookTitledEntry, specific=jointPackage_BibTeX2DocBook_SrcInProceedings)
gen_jointPackage_BibTeX2DocBook_SrcThesisEntry_SrcAuthoredEntry = Generalization(general=SrcAuthoredEntry, specific=jointPackage_BibTeX2DocBook_SrcThesisEntry)
gen_jointPackage_BibTeX2DocBook_SrcThesisEntry_SrcDatedEntry = Generalization(general=SrcDatedEntry, specific=jointPackage_BibTeX2DocBook_SrcThesisEntry)
gen_jointPackage_BibTeX2DocBook_SrcThesisEntry_SrcTitledEntry = Generalization(general=SrcTitledEntry, specific=jointPackage_BibTeX2DocBook_SrcThesisEntry)
gen_jointPackage_BibTeX2DocBook_TrgArticle_TrgTitledElement = Generalization(general=TrgTitledElement, specific=jointPackage_BibTeX2DocBook_TrgArticle)
gen_jointPackage_BibTeX2DocBook_SrcBookTitledEntry_SrcBibTeXEntry = Generalization(general=SrcBibTeXEntry, specific=jointPackage_BibTeX2DocBook_SrcBookTitledEntry)
gen_jointPackage_BibTeX2DocBook_SrcMisc_SrcBibTeXEntry = Generalization(general=SrcBibTeXEntry, specific=jointPackage_BibTeX2DocBook_SrcMisc)
gen_jointPackage_BibTeX2DocBook_TrgSect1_TrgSection = Generalization(general=TrgSection, specific=jointPackage_BibTeX2DocBook_TrgSect1)
gen_jointPackage_BibTeX2DocBook_TrgSect2_TrgSection = Generalization(general=TrgSection, specific=jointPackage_BibTeX2DocBook_TrgSect2)
gen_jointPackage_BibTeX2DocBook_TrgSection_TrgTitledElement = Generalization(general=TrgTitledElement, specific=jointPackage_BibTeX2DocBook_TrgSection)

# Domain Model
domain_model = DomainModel(
    name="jointPackage_BibTeX2DocBook",
    types={jointPackage_BibTeX2DocBook_JointMM, SrcMasterThesis, jointPackage_BibTeX2DocBook_SrcBibTeXFile, SrcBibTeXEntry, jointPackage_BibTeX2DocBook_SrcArticle, SrcAuthoredEntry, SrcDatedEntry, SrcTitledEntry, jointPackage_BibTeX2DocBook_SrcTechReport, TrgDocBook, jointPackage_BibTeX2DocBook_SrcBooklet, jointPackage_BibTeX2DocBook_SrcBook, jointPackage_BibTeX2DocBook_SrcInCollection, SrcBook, jointPackage_BibTeX2DocBook_SrcInBook, jointPackage_BibTeX2DocBook_SrcPhDThesis, SrcThesisEntry, jointPackage_BibTeX2DocBook_SrcMasterThesis, jointPackage_BibTeX2DocBook_SrcAuthor, jointPackage_BibTeX2DocBook_SrcBibTeXEntry, jointPackage_BibTeX2DocBook_SrcAuthoredEntry, SrcAuthor, jointPackage_BibTeX2DocBook_SrcDatedEntry, jointPackage_BibTeX2DocBook_SrcTitledEntry, jointPackage_BibTeX2DocBook_SrcUnpublished, jointPackage_BibTeX2DocBook_SrcManual, jointPackage_BibTeX2DocBook_SrcProceedings, jointPackage_BibTeX2DocBook_SrcInProceedings, SrcProceedings, SrcBookTitledEntry, jointPackage_BibTeX2DocBook_SrcThesisEntry, jointPackage_BibTeX2DocBook_TrgDocBook, TrgBook, jointPackage_BibTeX2DocBook_TrgBook, TrgArticle, jointPackage_BibTeX2DocBook_TrgTitledElement, jointPackage_BibTeX2DocBook_TrgArticle, TrgTitledElement, jointPackage_BibTeX2DocBook_SrcBookTitledEntry, jointPackage_BibTeX2DocBook_SrcMisc, TrgPara, jointPackage_BibTeX2DocBook_TrgSect1, TrgSection, TrgSect2, jointPackage_BibTeX2DocBook_TrgSect2, jointPackage_BibTeX2DocBook_TrgPara, TrgSect1, jointPackage_BibTeX2DocBook_TrgSection},
    associations={sourceRoot0, entries3, targetRoot1, authors4, books5, articles6, paras8, sections_29, section10, sections_17},
    generalizations={gen_jointPackage_BibTeX2DocBook_SrcArticle_SrcAuthoredEntry, gen_jointPackage_BibTeX2DocBook_SrcArticle_SrcDatedEntry, gen_jointPackage_BibTeX2DocBook_SrcArticle_SrcTitledEntry, gen_jointPackage_BibTeX2DocBook_SrcTechReport_SrcAuthoredEntry, gen_jointPackage_BibTeX2DocBook_SrcTechReport_SrcDatedEntry, gen_jointPackage_BibTeX2DocBook_SrcTechReport_SrcTitledEntry, gen_jointPackage_BibTeX2DocBook_SrcBooklet_SrcDatedEntry, gen_jointPackage_BibTeX2DocBook_SrcBook_SrcAuthoredEntry, gen_jointPackage_BibTeX2DocBook_SrcBook_SrcDatedEntry, gen_jointPackage_BibTeX2DocBook_SrcBook_SrcTitledEntry, gen_jointPackage_BibTeX2DocBook_SrcInCollection_SrcBook, gen_jointPackage_BibTeX2DocBook_SrcInCollection_SrcBookTitledEntry, gen_jointPackage_BibTeX2DocBook_SrcInBook_SrcBook, gen_jointPackage_BibTeX2DocBook_SrcPhDThesis_SrcThesisEntry, gen_jointPackage_BibTeX2DocBook_SrcMasterThesis_SrcThesisEntry, gen_jointPackage_BibTeX2DocBook_SrcAuthoredEntry_SrcBibTeXEntry, gen_jointPackage_BibTeX2DocBook_SrcDatedEntry_SrcBibTeXEntry, gen_jointPackage_BibTeX2DocBook_SrcTitledEntry_SrcBibTeXEntry, gen_jointPackage_BibTeX2DocBook_SrcUnpublished_SrcAuthoredEntry, gen_jointPackage_BibTeX2DocBook_SrcUnpublished_SrcTitledEntry, gen_jointPackage_BibTeX2DocBook_SrcManual_SrcTitledEntry, gen_jointPackage_BibTeX2DocBook_SrcProceedings_SrcDatedEntry, gen_jointPackage_BibTeX2DocBook_SrcProceedings_SrcTitledEntry, gen_jointPackage_BibTeX2DocBook_SrcInProceedings_SrcProceedings, gen_jointPackage_BibTeX2DocBook_SrcInProceedings_SrcAuthoredEntry, gen_jointPackage_BibTeX2DocBook_SrcInProceedings_SrcBookTitledEntry, gen_jointPackage_BibTeX2DocBook_SrcThesisEntry_SrcAuthoredEntry, gen_jointPackage_BibTeX2DocBook_SrcThesisEntry_SrcDatedEntry, gen_jointPackage_BibTeX2DocBook_SrcThesisEntry_SrcTitledEntry, gen_jointPackage_BibTeX2DocBook_TrgArticle_TrgTitledElement, gen_jointPackage_BibTeX2DocBook_SrcBookTitledEntry_SrcBibTeXEntry, gen_jointPackage_BibTeX2DocBook_SrcMisc_SrcBibTeXEntry, gen_jointPackage_BibTeX2DocBook_TrgSect1_TrgSection, gen_jointPackage_BibTeX2DocBook_TrgSect2_TrgSection, gen_jointPackage_BibTeX2DocBook_TrgSection_TrgTitledElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)