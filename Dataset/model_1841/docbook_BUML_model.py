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
docbook_Article = Class(name="docbook::Article")
docbook_TitledElement = Class(name="docbook::TitledElement", is_abstract=True)
TitledElement = Class(name="TitledElement")
docbook_DocBook = Class(name="docbook::DocBook")
docbook_Book = Class(name="docbook::Book")
Section = Class(name="Section")
docbook_Sect2 = Class(name="docbook::Sect2")
docbook_Sect1 = Class(name="docbook::Sect1")
docbook_Section = Class(name="docbook::Section", is_abstract=True)
docbook_Para = Class(name="docbook::Para")

# docbook_Article class attributes and methods

# docbook_TitledElement class attributes and methods
docbook_TitledElement_title: Property = Property(name="title", type=StringType)
docbook_TitledElement.attributes={docbook_TitledElement_title}

# TitledElement class attributes and methods

# docbook_DocBook class attributes and methods

# docbook_Book class attributes and methods

# Section class attributes and methods

# docbook_Sect2 class attributes and methods

# docbook_Sect1 class attributes and methods

# docbook_Section class attributes and methods

# docbook_Para class attributes and methods
docbook_Para_content: Property = Property(name="content", type=StringType)
docbook_Para.attributes={docbook_Para_content}

# Relationships
articles1: BinaryAssociation = BinaryAssociation(
    name="articles1",
    ends={
        Property(name="docbook_Article", type=docbook_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="docbook_Book2", type=docbook_Article, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
books0: BinaryAssociation = BinaryAssociation(
    name="books0",
    ends={
        Property(name="docbook_Book", type=docbook_DocBook, multiplicity=Multiplicity(1, 1)),
        Property(name="docbook_DocBook", type=docbook_Book, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
paras5: BinaryAssociation = BinaryAssociation(
    name="paras5",
    ends={
        Property(name="docbook_Section", type=docbook_Para, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="docbook_Para", type=docbook_Section, multiplicity=Multiplicity(1, 1))
    }
)
sections_26: BinaryAssociation = BinaryAssociation(
    name="sections_26",
    ends={
        Property(name="docbook_Sect2", type=docbook_Sect1, multiplicity=Multiplicity(1, 1)),
        Property(name="docbook_Sect17", type=docbook_Sect2, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sections_13: BinaryAssociation = BinaryAssociation(
    name="sections_13",
    ends={
        Property(name="docbook_Sect1", type=docbook_Article, multiplicity=Multiplicity(1, 1)),
        Property(name="docbook_Article4", type=docbook_Sect1, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_docbook_Article_TitledElement = Generalization(general=TitledElement, specific=docbook_Article)
gen_docbook_Sect1_Section = Generalization(general=Section, specific=docbook_Sect1)
gen_docbook_Sect2_Section = Generalization(general=Section, specific=docbook_Sect2)
gen_docbook_Section_TitledElement = Generalization(general=TitledElement, specific=docbook_Section)

# Domain Model
domain_model = DomainModel(
    name="docbook",
    types={docbook_Article, docbook_TitledElement, TitledElement, docbook_DocBook, docbook_Book, Section, docbook_Sect2, docbook_Sect1, docbook_Section, docbook_Para},
    associations={articles1, books0, paras5, sections_26, sections_13},
    generalizations={gen_docbook_Article_TitledElement, gen_docbook_Sect1_Section, gen_docbook_Sect2_Section, gen_docbook_Section_TitledElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)