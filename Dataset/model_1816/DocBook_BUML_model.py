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
DocBook_Article = Class(name="DocBook::Article")
DocBook_TitledElement = Class(name="DocBook::TitledElement", is_abstract=True)
TitledElement = Class(name="TitledElement")
DocBook_Sect1 = Class(name="DocBook::Sect1")
DocBook_Section = Class(name="DocBook::Section", is_abstract=True)
DocBook_Para = Class(name="DocBook::Para")
Section = Class(name="Section")
DocBook_DocBook = Class(name="DocBook::DocBook")
DocBook_Book = Class(name="DocBook::Book")
DocBook_Sect2 = Class(name="DocBook::Sect2")

# DocBook_Article class attributes and methods

# DocBook_TitledElement class attributes and methods
DocBook_TitledElement_title: Property = Property(name="title", type=StringType)
DocBook_TitledElement.attributes={DocBook_TitledElement_title}

# TitledElement class attributes and methods

# DocBook_Sect1 class attributes and methods

# DocBook_Section class attributes and methods

# DocBook_Para class attributes and methods
DocBook_Para_content: Property = Property(name="content", type=StringType)
DocBook_Para.attributes={DocBook_Para_content}

# Section class attributes and methods

# DocBook_DocBook class attributes and methods

# DocBook_Book class attributes and methods

# DocBook_Sect2 class attributes and methods

# Relationships
articles1: BinaryAssociation = BinaryAssociation(
    name="articles1",
    ends={
        Property(name="DocBook_Article", type=DocBook_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="DocBook_Book2", type=DocBook_Article, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
sections_13: BinaryAssociation = BinaryAssociation(
    name="sections_13",
    ends={
        Property(name="DocBook_Sect1", type=DocBook_Article, multiplicity=Multiplicity(1, 1)),
        Property(name="DocBook_Article4", type=DocBook_Sect1, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
paras5: BinaryAssociation = BinaryAssociation(
    name="paras5",
    ends={
        Property(name="Para", type=DocBook_Section, multiplicity=Multiplicity(1, 1)),
        Property(name="section", type=DocBook_Para, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
books0: BinaryAssociation = BinaryAssociation(
    name="books0",
    ends={
        Property(name="DocBook_Book", type=DocBook_DocBook, multiplicity=Multiplicity(1, 1)),
        Property(name="DocBook_DocBook", type=DocBook_Book, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
section8: BinaryAssociation = BinaryAssociation(
    name="section8",
    ends={
        Property(name="Section", type=DocBook_Para, multiplicity=Multiplicity(1, 1)),
        Property(name="paras", type=DocBook_Section, multiplicity=Multiplicity(1, 1))
    }
)
sections_26: BinaryAssociation = BinaryAssociation(
    name="sections_26",
    ends={
        Property(name="DocBook_Sect2", type=DocBook_Sect1, multiplicity=Multiplicity(1, 1)),
        Property(name="DocBook_Sect17", type=DocBook_Sect2, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)

# Generalizations
gen_DocBook_Article_TitledElement = Generalization(general=TitledElement, specific=DocBook_Article)
gen_DocBook_Section_TitledElement = Generalization(general=TitledElement, specific=DocBook_Section)
gen_DocBook_Sect1_Section = Generalization(general=Section, specific=DocBook_Sect1)
gen_DocBook_Sect2_Section = Generalization(general=Section, specific=DocBook_Sect2)

# Domain Model
domain_model = DomainModel(
    name="DocBook",
    types={DocBook_Article, DocBook_TitledElement, TitledElement, DocBook_Sect1, DocBook_Section, DocBook_Para, Section, DocBook_DocBook, DocBook_Book, DocBook_Sect2},
    associations={articles1, sections_13, paras5, books0, section8, sections_26},
    generalizations={gen_DocBook_Article_TitledElement, gen_DocBook_Section_TitledElement, gen_DocBook_Sect1_Section, gen_DocBook_Sect2_Section},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)