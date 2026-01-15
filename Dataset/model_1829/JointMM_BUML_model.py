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
TrgDocBook = Class(name="TrgDocBook")
jointPackage_SrcBibTeXFile = Class(name="jointPackage::SrcBibTeXFile")
SrcBibTeXEntry = Class(name="SrcBibTeXEntry")
jointPackage_SrcArticle = Class(name="jointPackage::SrcArticle")
SrcAuthoredEntry = Class(name="SrcAuthoredEntry")
SrcDatedEntry = Class(name="SrcDatedEntry")
SrcTitledEntry = Class(name="SrcTitledEntry")
jointPackage_SrcTechReport = Class(name="jointPackage::SrcTechReport")
jointPackage_SrcUnpublished = Class(name="jointPackage::SrcUnpublished")
jointPackage_JointMM = Class(name="jointPackage::JointMM")
SrcMasterThesis = Class(name="SrcMasterThesis")
jointPackage_SrcBooklet = Class(name="jointPackage::SrcBooklet")
jointPackage_SrcBook = Class(name="jointPackage::SrcBook")
jointPackage_SrcInCollection = Class(name="jointPackage::SrcInCollection")
SrcBook = Class(name="SrcBook")
jointPackage_SrcInBook = Class(name="jointPackage::SrcInBook")
jointPackage_SrcPhDThesis = Class(name="jointPackage::SrcPhDThesis")
SrcThesisEntry = Class(name="SrcThesisEntry")
jointPackage_SrcMasterThesis = Class(name="jointPackage::SrcMasterThesis")
jointPackage_SrcAuthor = Class(name="jointPackage::SrcAuthor")
jointPackage_SrcManual = Class(name="jointPackage::SrcManual")
jointPackage_SrcProceedings = Class(name="jointPackage::SrcProceedings")
jointPackage_SrcInProceedings = Class(name="jointPackage::SrcInProceedings")
SrcProceedings = Class(name="SrcProceedings")
SrcBookTitledEntry = Class(name="SrcBookTitledEntry")
jointPackage_SrcTitledEntry = Class(name="jointPackage::SrcTitledEntry", is_abstract=True)
jointPackage_SrcBookTitledEntry = Class(name="jointPackage::SrcBookTitledEntry", is_abstract=True)
jointPackage_SrcMisc = Class(name="jointPackage::SrcMisc")
jointPackage_SrcThesisEntry = Class(name="jointPackage::SrcThesisEntry", is_abstract=True)
jointPackage_TrgDocBook = Class(name="jointPackage::TrgDocBook")
TrgBook = Class(name="TrgBook")
jointPackage_SrcBibTeXEntry = Class(name="jointPackage::SrcBibTeXEntry", is_abstract=True)
jointPackage_SrcAuthoredEntry = Class(name="jointPackage::SrcAuthoredEntry", is_abstract=True)
SrcAuthor = Class(name="SrcAuthor")
jointPackage_SrcDatedEntry = Class(name="jointPackage::SrcDatedEntry", is_abstract=True)
jointPackage_TrgSection = Class(name="jointPackage::TrgSection", is_abstract=True)
TrgPara = Class(name="TrgPara")
jointPackage_TrgSect1 = Class(name="jointPackage::TrgSect1")
TrgSection = Class(name="TrgSection")
TrgSect2 = Class(name="TrgSect2")
jointPackage_TrgSect2 = Class(name="jointPackage::TrgSect2")
jointPackage_TrgPara = Class(name="jointPackage::TrgPara")
jointPackage_TrgBook = Class(name="jointPackage::TrgBook")
TrgArticle = Class(name="TrgArticle")
jointPackage_TrgTitledElement = Class(name="jointPackage::TrgTitledElement", is_abstract=True)
jointPackage_TrgArticle = Class(name="jointPackage::TrgArticle")
TrgTitledElement = Class(name="TrgTitledElement")
TrgSect1 = Class(name="TrgSect1")

# TrgDocBook class attributes and methods

# jointPackage_SrcBibTeXFile class attributes and methods

# SrcBibTeXEntry class attributes and methods

# jointPackage_SrcArticle class attributes and methods
jointPackage_SrcArticle_journal: Property = Property(name="journal", type=StringType)
jointPackage_SrcArticle.attributes={jointPackage_SrcArticle_journal}

# SrcAuthoredEntry class attributes and methods

# SrcDatedEntry class attributes and methods

# SrcTitledEntry class attributes and methods

# jointPackage_SrcTechReport class attributes and methods

# jointPackage_SrcUnpublished class attributes and methods
jointPackage_SrcUnpublished_note: Property = Property(name="note", type=StringType)
jointPackage_SrcUnpublished.attributes={jointPackage_SrcUnpublished_note}

# jointPackage_JointMM class attributes and methods

# SrcMasterThesis class attributes and methods

# jointPackage_SrcBooklet class attributes and methods

# jointPackage_SrcBook class attributes and methods
jointPackage_SrcBook_publisher: Property = Property(name="publisher", type=StringType)
jointPackage_SrcBook.attributes={jointPackage_SrcBook_publisher}

# jointPackage_SrcInCollection class attributes and methods

# SrcBook class attributes and methods

# jointPackage_SrcInBook class attributes and methods
jointPackage_SrcInBook_chapter: Property = Property(name="chapter", type=IntegerType)
jointPackage_SrcInBook.attributes={jointPackage_SrcInBook_chapter}

# jointPackage_SrcPhDThesis class attributes and methods

# SrcThesisEntry class attributes and methods

# jointPackage_SrcMasterThesis class attributes and methods

# jointPackage_SrcAuthor class attributes and methods
jointPackage_SrcAuthor_author: Property = Property(name="author", type=StringType)
jointPackage_SrcAuthor.attributes={jointPackage_SrcAuthor_author}

# jointPackage_SrcManual class attributes and methods

# jointPackage_SrcProceedings class attributes and methods

# jointPackage_SrcInProceedings class attributes and methods

# SrcProceedings class attributes and methods

# SrcBookTitledEntry class attributes and methods

# jointPackage_SrcTitledEntry class attributes and methods
jointPackage_SrcTitledEntry_title: Property = Property(name="title", type=StringType)
jointPackage_SrcTitledEntry.attributes={jointPackage_SrcTitledEntry_title}

# jointPackage_SrcBookTitledEntry class attributes and methods
jointPackage_SrcBookTitledEntry_booktitle: Property = Property(name="booktitle", type=StringType)
jointPackage_SrcBookTitledEntry.attributes={jointPackage_SrcBookTitledEntry_booktitle}

# jointPackage_SrcMisc class attributes and methods

# jointPackage_SrcThesisEntry class attributes and methods
jointPackage_SrcThesisEntry_school: Property = Property(name="school", type=StringType)
jointPackage_SrcThesisEntry.attributes={jointPackage_SrcThesisEntry_school}

# jointPackage_TrgDocBook class attributes and methods

# TrgBook class attributes and methods

# jointPackage_SrcBibTeXEntry class attributes and methods
jointPackage_SrcBibTeXEntry_id: Property = Property(name="id", type=StringType)
jointPackage_SrcBibTeXEntry.attributes={jointPackage_SrcBibTeXEntry_id}

# jointPackage_SrcAuthoredEntry class attributes and methods

# SrcAuthor class attributes and methods

# jointPackage_SrcDatedEntry class attributes and methods
jointPackage_SrcDatedEntry_year: Property = Property(name="year", type=StringType)
jointPackage_SrcDatedEntry.attributes={jointPackage_SrcDatedEntry_year}

# jointPackage_TrgSection class attributes and methods

# TrgPara class attributes and methods

# jointPackage_TrgSect1 class attributes and methods

# TrgSection class attributes and methods

# TrgSect2 class attributes and methods

# jointPackage_TrgSect2 class attributes and methods

# jointPackage_TrgPara class attributes and methods
jointPackage_TrgPara_content: Property = Property(name="content", type=StringType)
jointPackage_TrgPara.attributes={jointPackage_TrgPara_content}

# jointPackage_TrgBook class attributes and methods

# TrgArticle class attributes and methods

# jointPackage_TrgTitledElement class attributes and methods
jointPackage_TrgTitledElement_title: Property = Property(name="title", type=StringType)
jointPackage_TrgTitledElement.attributes={jointPackage_TrgTitledElement_title}

# jointPackage_TrgArticle class attributes and methods

# TrgTitledElement class attributes and methods

# TrgSect1 class attributes and methods

# Relationships
targetRoot1: BinaryAssociation = BinaryAssociation(
    name="targetRoot1",
    ends={
        Property(name="TrgDocBook", type=jointPackage_JointMM, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_JointMM2", type=TrgDocBook, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
entries3: BinaryAssociation = BinaryAssociation(
    name="entries3",
    ends={
        Property(name="SrcBibTeXEntry", type=jointPackage_SrcBibTeXFile, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_SrcBibTeXFile", type=SrcBibTeXEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sourceRoot0: BinaryAssociation = BinaryAssociation(
    name="sourceRoot0",
    ends={
        Property(name="SrcMasterThesis", type=jointPackage_JointMM, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_JointMM", type=SrcMasterThesis, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
books5: BinaryAssociation = BinaryAssociation(
    name="books5",
    ends={
        Property(name="TrgBook", type=jointPackage_TrgDocBook, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_TrgDocBook", type=TrgBook, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
authors4: BinaryAssociation = BinaryAssociation(
    name="authors4",
    ends={
        Property(name="SrcAuthor", type=jointPackage_SrcAuthoredEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_SrcAuthoredEntry", type=SrcAuthor, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
sections_17: BinaryAssociation = BinaryAssociation(
    name="sections_17",
    ends={
        Property(name="TrgSect1", type=jointPackage_TrgArticle, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_TrgArticle", type=TrgSect1, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
paras8: BinaryAssociation = BinaryAssociation(
    name="paras8",
    ends={
        Property(name="#", type=jointPackage_TrgSection, multiplicity=Multiplicity(1, 1)),
        Property(name="0", type=TrgPara, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
sections_29: BinaryAssociation = BinaryAssociation(
    name="sections_29",
    ends={
        Property(name="TrgSect2", type=jointPackage_TrgSect1, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_TrgSect1", type=TrgSect2, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
section10: BinaryAssociation = BinaryAssociation(
    name="section10",
    ends={
        Property(name="#12", type=jointPackage_TrgPara, multiplicity=Multiplicity(1, 1)),
        Property(name="011", type=TrgSection, multiplicity=Multiplicity(1, 1))
    }
)
articles6: BinaryAssociation = BinaryAssociation(
    name="articles6",
    ends={
        Property(name="TrgArticle", type=jointPackage_TrgBook, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_TrgBook", type=TrgArticle, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)

# Generalizations
gen_jointPackage_SrcArticle_SrcAuthoredEntry = Generalization(general=SrcAuthoredEntry, specific=jointPackage_SrcArticle)
gen_jointPackage_SrcArticle_SrcDatedEntry = Generalization(general=SrcDatedEntry, specific=jointPackage_SrcArticle)
gen_jointPackage_SrcArticle_SrcTitledEntry = Generalization(general=SrcTitledEntry, specific=jointPackage_SrcArticle)
gen_jointPackage_SrcTechReport_SrcAuthoredEntry = Generalization(general=SrcAuthoredEntry, specific=jointPackage_SrcTechReport)
gen_jointPackage_SrcTechReport_SrcDatedEntry = Generalization(general=SrcDatedEntry, specific=jointPackage_SrcTechReport)
gen_jointPackage_SrcTechReport_SrcTitledEntry = Generalization(general=SrcTitledEntry, specific=jointPackage_SrcTechReport)
gen_jointPackage_SrcUnpublished_SrcAuthoredEntry = Generalization(general=SrcAuthoredEntry, specific=jointPackage_SrcUnpublished)
gen_jointPackage_SrcBooklet_SrcDatedEntry = Generalization(general=SrcDatedEntry, specific=jointPackage_SrcBooklet)
gen_jointPackage_SrcBook_SrcAuthoredEntry = Generalization(general=SrcAuthoredEntry, specific=jointPackage_SrcBook)
gen_jointPackage_SrcBook_SrcDatedEntry = Generalization(general=SrcDatedEntry, specific=jointPackage_SrcBook)
gen_jointPackage_SrcBook_SrcTitledEntry = Generalization(general=SrcTitledEntry, specific=jointPackage_SrcBook)
gen_jointPackage_SrcInCollection_SrcBook = Generalization(general=SrcBook, specific=jointPackage_SrcInCollection)
gen_jointPackage_SrcInCollection_SrcBookTitledEntry = Generalization(general=SrcBookTitledEntry, specific=jointPackage_SrcInCollection)
gen_jointPackage_SrcInBook_SrcBook = Generalization(general=SrcBook, specific=jointPackage_SrcInBook)
gen_jointPackage_SrcPhDThesis_SrcThesisEntry = Generalization(general=SrcThesisEntry, specific=jointPackage_SrcPhDThesis)
gen_jointPackage_SrcMasterThesis_SrcThesisEntry = Generalization(general=SrcThesisEntry, specific=jointPackage_SrcMasterThesis)
gen_jointPackage_SrcUnpublished_SrcTitledEntry = Generalization(general=SrcTitledEntry, specific=jointPackage_SrcUnpublished)
gen_jointPackage_SrcManual_SrcTitledEntry = Generalization(general=SrcTitledEntry, specific=jointPackage_SrcManual)
gen_jointPackage_SrcProceedings_SrcDatedEntry = Generalization(general=SrcDatedEntry, specific=jointPackage_SrcProceedings)
gen_jointPackage_SrcProceedings_SrcTitledEntry = Generalization(general=SrcTitledEntry, specific=jointPackage_SrcProceedings)
gen_jointPackage_SrcInProceedings_SrcProceedings = Generalization(general=SrcProceedings, specific=jointPackage_SrcInProceedings)
gen_jointPackage_SrcInProceedings_SrcAuthoredEntry = Generalization(general=SrcAuthoredEntry, specific=jointPackage_SrcInProceedings)
gen_jointPackage_SrcInProceedings_SrcBookTitledEntry = Generalization(general=SrcBookTitledEntry, specific=jointPackage_SrcInProceedings)
gen_jointPackage_SrcTitledEntry_SrcBibTeXEntry = Generalization(general=SrcBibTeXEntry, specific=jointPackage_SrcTitledEntry)
gen_jointPackage_SrcBookTitledEntry_SrcBibTeXEntry = Generalization(general=SrcBibTeXEntry, specific=jointPackage_SrcBookTitledEntry)
gen_jointPackage_SrcMisc_SrcBibTeXEntry = Generalization(general=SrcBibTeXEntry, specific=jointPackage_SrcMisc)
gen_jointPackage_SrcThesisEntry_SrcAuthoredEntry = Generalization(general=SrcAuthoredEntry, specific=jointPackage_SrcThesisEntry)
gen_jointPackage_SrcThesisEntry_SrcDatedEntry = Generalization(general=SrcDatedEntry, specific=jointPackage_SrcThesisEntry)
gen_jointPackage_SrcThesisEntry_SrcTitledEntry = Generalization(general=SrcTitledEntry, specific=jointPackage_SrcThesisEntry)
gen_jointPackage_SrcAuthoredEntry_SrcBibTeXEntry = Generalization(general=SrcBibTeXEntry, specific=jointPackage_SrcAuthoredEntry)
gen_jointPackage_SrcDatedEntry_SrcBibTeXEntry = Generalization(general=SrcBibTeXEntry, specific=jointPackage_SrcDatedEntry)
gen_jointPackage_TrgSection_TrgTitledElement = Generalization(general=TrgTitledElement, specific=jointPackage_TrgSection)
gen_jointPackage_TrgSect1_TrgSection = Generalization(general=TrgSection, specific=jointPackage_TrgSect1)
gen_jointPackage_TrgSect2_TrgSection = Generalization(general=TrgSection, specific=jointPackage_TrgSect2)
gen_jointPackage_TrgArticle_TrgTitledElement = Generalization(general=TrgTitledElement, specific=jointPackage_TrgArticle)

# Domain Model
domain_model = DomainModel(
    name="jointPackage",
    types={TrgDocBook, jointPackage_SrcBibTeXFile, SrcBibTeXEntry, jointPackage_SrcArticle, SrcAuthoredEntry, SrcDatedEntry, SrcTitledEntry, jointPackage_SrcTechReport, jointPackage_SrcUnpublished, jointPackage_JointMM, SrcMasterThesis, jointPackage_SrcBooklet, jointPackage_SrcBook, jointPackage_SrcInCollection, SrcBook, jointPackage_SrcInBook, jointPackage_SrcPhDThesis, SrcThesisEntry, jointPackage_SrcMasterThesis, jointPackage_SrcAuthor, jointPackage_SrcManual, jointPackage_SrcProceedings, jointPackage_SrcInProceedings, SrcProceedings, SrcBookTitledEntry, jointPackage_SrcTitledEntry, jointPackage_SrcBookTitledEntry, jointPackage_SrcMisc, jointPackage_SrcThesisEntry, jointPackage_TrgDocBook, TrgBook, jointPackage_SrcBibTeXEntry, jointPackage_SrcAuthoredEntry, SrcAuthor, jointPackage_SrcDatedEntry, jointPackage_TrgSection, TrgPara, jointPackage_TrgSect1, TrgSection, TrgSect2, jointPackage_TrgSect2, jointPackage_TrgPara, jointPackage_TrgBook, TrgArticle, jointPackage_TrgTitledElement, jointPackage_TrgArticle, TrgTitledElement, TrgSect1},
    associations={targetRoot1, entries3, sourceRoot0, books5, authors4, sections_17, paras8, sections_29, section10, articles6},
    generalizations={gen_jointPackage_SrcArticle_SrcAuthoredEntry, gen_jointPackage_SrcArticle_SrcDatedEntry, gen_jointPackage_SrcArticle_SrcTitledEntry, gen_jointPackage_SrcTechReport_SrcAuthoredEntry, gen_jointPackage_SrcTechReport_SrcDatedEntry, gen_jointPackage_SrcTechReport_SrcTitledEntry, gen_jointPackage_SrcUnpublished_SrcAuthoredEntry, gen_jointPackage_SrcBooklet_SrcDatedEntry, gen_jointPackage_SrcBook_SrcAuthoredEntry, gen_jointPackage_SrcBook_SrcDatedEntry, gen_jointPackage_SrcBook_SrcTitledEntry, gen_jointPackage_SrcInCollection_SrcBook, gen_jointPackage_SrcInCollection_SrcBookTitledEntry, gen_jointPackage_SrcInBook_SrcBook, gen_jointPackage_SrcPhDThesis_SrcThesisEntry, gen_jointPackage_SrcMasterThesis_SrcThesisEntry, gen_jointPackage_SrcUnpublished_SrcTitledEntry, gen_jointPackage_SrcManual_SrcTitledEntry, gen_jointPackage_SrcProceedings_SrcDatedEntry, gen_jointPackage_SrcProceedings_SrcTitledEntry, gen_jointPackage_SrcInProceedings_SrcProceedings, gen_jointPackage_SrcInProceedings_SrcAuthoredEntry, gen_jointPackage_SrcInProceedings_SrcBookTitledEntry, gen_jointPackage_SrcTitledEntry_SrcBibTeXEntry, gen_jointPackage_SrcBookTitledEntry_SrcBibTeXEntry, gen_jointPackage_SrcMisc_SrcBibTeXEntry, gen_jointPackage_SrcThesisEntry_SrcAuthoredEntry, gen_jointPackage_SrcThesisEntry_SrcDatedEntry, gen_jointPackage_SrcThesisEntry_SrcTitledEntry, gen_jointPackage_SrcAuthoredEntry_SrcBibTeXEntry, gen_jointPackage_SrcDatedEntry_SrcBibTeXEntry, gen_jointPackage_TrgSection_TrgTitledElement, gen_jointPackage_TrgSect1_TrgSection, gen_jointPackage_TrgSect2_TrgSection, gen_jointPackage_TrgArticle_TrgTitledElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)