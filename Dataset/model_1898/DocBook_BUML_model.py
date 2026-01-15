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
DocBook_DocBook = Class(name="DocBook::DocBook")
Book = Class(name="Book")
DocBook_Book = Class(name="DocBook::Book")
Article = Class(name="Article")
DocBook_Article = Class(name="DocBook::Article")
TitledElement = Class(name="TitledElement")
Sect1 = Class(name="Sect1")
DocBook_Section = Class(name="DocBook::Section", is_abstract=True)
Para = Class(name="Para")
DocBook_Sect1 = Class(name="DocBook::Sect1")
Section = Class(name="Section")
Sect2 = Class(name="Sect2")
DocBook_Sect2 = Class(name="DocBook::Sect2")
DocBook_Para = Class(name="DocBook::Para")
DocBook_TitledElement = Class(name="DocBook::TitledElement", is_abstract=True)

# DocBook_DocBook class attributes and methods

# Book class attributes and methods

# DocBook_Book class attributes and methods

# Article class attributes and methods

# DocBook_Article class attributes and methods

# TitledElement class attributes and methods

# Sect1 class attributes and methods

# DocBook_Section class attributes and methods

# Para class attributes and methods

# DocBook_Sect1 class attributes and methods

# Section class attributes and methods

# Sect2 class attributes and methods

# DocBook_Sect2 class attributes and methods

# DocBook_Para class attributes and methods
DocBook_Para_content: Property = Property(name="content", type=StringType)
DocBook_Para.attributes={DocBook_Para_content}

# DocBook_TitledElement class attributes and methods
DocBook_TitledElement_title: Property = Property(name="title", type=StringType)
DocBook_TitledElement.attributes={DocBook_TitledElement_title}

# Relationships
books0: BinaryAssociation = BinaryAssociation(
    name="books0",
    ends={
        Property(name="Book", type=DocBook_DocBook, multiplicity=Multiplicity(1, 1)),
        Property(name="DocBook_DocBook", type=Book, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
articles1: BinaryAssociation = BinaryAssociation(
    name="articles1",
    ends={
        Property(name="Article", type=DocBook_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="DocBook_Book", type=Article, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
sections_12: BinaryAssociation = BinaryAssociation(
    name="sections_12",
    ends={
        Property(name="Sect1", type=DocBook_Article, multiplicity=Multiplicity(1, 1)),
        Property(name="DocBook_Article", type=Sect1, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
paras3: BinaryAssociation = BinaryAssociation(
    name="paras3",
    ends={
        Property(name="Para", type=DocBook_Section, multiplicity=Multiplicity(1, 1)),
        Property(name="DocBook_Section", type=Para, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
sections_24: BinaryAssociation = BinaryAssociation(
    name="sections_24",
    ends={
        Property(name="Sect2", type=DocBook_Sect1, multiplicity=Multiplicity(1, 1)),
        Property(name="DocBook_Sect1", type=Sect2, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)

# Generalizations
gen_DocBook_Article_TitledElement = Generalization(general=TitledElement, specific=DocBook_Article)
gen_DocBook_Section_TitledElement = Generalization(general=TitledElement, specific=DocBook_Section)
gen_DocBook_Sect1_Section = Generalization(general=Section, specific=DocBook_Sect1)
gen_DocBook_Sect2_Section = Generalization(general=Section, specific=DocBook_Sect2)

# Domain Model
domain_model = DomainModel(
    name="PrimitiveTypes",
    types={DocBook_DocBook, Book, DocBook_Book, Article, DocBook_Article, TitledElement, Sect1, DocBook_Section, Para, DocBook_Sect1, Section, Sect2, DocBook_Sect2, DocBook_Para, DocBook_TitledElement},
    associations={books0, articles1, sections_12, paras3, sections_24},
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