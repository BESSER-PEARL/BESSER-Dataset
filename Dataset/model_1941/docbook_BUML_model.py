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
docbook_Author = Class(name="docbook::Author")
docbook_Book = Class(name="docbook::Book")
XMLElement = Class(name="XMLElement")
docbook_Bookinfo = Class(name="docbook::Bookinfo")
docbook_Chapter = Class(name="docbook::Chapter")
docbook_Section = Class(name="docbook::Section")
docbook_Subtitle = Class(name="docbook::Subtitle")
TitledElement = Class(name="TitledElement")
docbook_SectionMixedContent = Class(name="docbook::SectionMixedContent", is_abstract=True)
docbook_Title = Class(name="docbook::Title")
docbook_TitledElement = Class(name="docbook::TitledElement", is_abstract=True)
docbook_ParaMixedContent = Class(name="docbook::ParaMixedContent", is_abstract=True)
docbook_Para = Class(name="docbook::Para")
SectionMixedContent = Class(name="SectionMixedContent")
docbook_XMLElement = Class(name="docbook::XMLElement", is_abstract=True)
docbook_Emphasis = Class(name="docbook::Emphasis")
docbook_Ulink = Class(name="docbook::Ulink")
docbook_Link = Class(name="docbook::Link")
docbook_ProgramListing = Class(name="docbook::ProgramListing")
Para = Class(name="Para")
docbook_SimpleText = Class(name="docbook::SimpleText")
ParaMixedContent = Class(name="ParaMixedContent")
docbook_Figure = Class(name="docbook::Figure")
docbook_MediaObject = Class(name="docbook::MediaObject")
docbook_Tip = Class(name="docbook::Tip")
docbook_Warning = Class(name="docbook::Warning")
docbook_ImageObject = Class(name="docbook::ImageObject")
docbook_ImageData = Class(name="docbook::ImageData")

# docbook_Author class attributes and methods
docbook_Author_honorific: Property = Property(name="honorific", type=StringType)
docbook_Author_firstname: Property = Property(name="firstname", type=StringType)
docbook_Author_surname: Property = Property(name="surname", type=StringType)
docbook_Author_authorblug: Property = Property(name="authorblug", type=StringType)
docbook_Author.attributes={docbook_Author_honorific, docbook_Author_authorblug, docbook_Author_firstname, docbook_Author_surname}

# docbook_Book class attributes and methods

# XMLElement class attributes and methods

# docbook_Bookinfo class attributes and methods
docbook_Bookinfo_date: Property = Property(name="date", type=StringType)
docbook_Bookinfo_pubdate: Property = Property(name="pubdate", type=StringType)
docbook_Bookinfo.attributes={docbook_Bookinfo_pubdate, docbook_Bookinfo_date}

# docbook_Chapter class attributes and methods

# docbook_Section class attributes and methods

# docbook_Subtitle class attributes and methods

# TitledElement class attributes and methods

# docbook_SectionMixedContent class attributes and methods

# docbook_Title class attributes and methods

# docbook_TitledElement class attributes and methods

# docbook_ParaMixedContent class attributes and methods

# docbook_Para class attributes and methods

# SectionMixedContent class attributes and methods

# docbook_XMLElement class attributes and methods
docbook_XMLElement_id: Property = Property(name="id", type=StringType)
docbook_XMLElement.attributes={docbook_XMLElement_id}

# docbook_Emphasis class attributes and methods

# docbook_Ulink class attributes and methods

# docbook_Link class attributes and methods

# docbook_ProgramListing class attributes and methods

# Para class attributes and methods

# docbook_SimpleText class attributes and methods
docbook_SimpleText_data: Property = Property(name="data", type=StringType)
docbook_SimpleText.attributes={docbook_SimpleText_data}

# ParaMixedContent class attributes and methods

# docbook_Figure class attributes and methods

# docbook_MediaObject class attributes and methods

# docbook_Tip class attributes and methods

# docbook_Warning class attributes and methods

# docbook_ImageObject class attributes and methods

# docbook_ImageData class attributes and methods
docbook_ImageData_fileref: Property = Property(name="fileref", type=StringType)
docbook_ImageData_width: Property = Property(name="width", type=StringType)
docbook_ImageData_depth: Property = Property(name="depth", type=StringType)
docbook_ImageData.attributes={docbook_ImageData_width, docbook_ImageData_depth, docbook_ImageData_fileref}

# Relationships
subtitle4: BinaryAssociation = BinaryAssociation(
    name="subtitle4",
    ends={
        Property(name="Subtitle", type=docbook_Bookinfo, multiplicity=Multiplicity(1, 1)),
        Property(name="bookinfo5", type=docbook_Subtitle, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
author6: BinaryAssociation = BinaryAssociation(
    name="author6",
    ends={
        Property(name="Author", type=docbook_Bookinfo, multiplicity=Multiplicity(1, 1)),
        Property(name="bookinfo7", type=docbook_Author, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bookinfo0: BinaryAssociation = BinaryAssociation(
    name="bookinfo0",
    ends={
        Property(name="Bookinfo", type=docbook_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="book", type=docbook_Bookinfo, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
chapter1: BinaryAssociation = BinaryAssociation(
    name="chapter1",
    ends={
        Property(name="Chapter", type=docbook_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="book2", type=docbook_Chapter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
book3: BinaryAssociation = BinaryAssociation(
    name="book3",
    ends={
        Property(name="Book", type=docbook_Bookinfo, multiplicity=Multiplicity(1, 1)),
        Property(name="bookinfo", type=docbook_Book, multiplicity=Multiplicity(0, 1))
    }
)
content20: BinaryAssociation = BinaryAssociation(
    name="content20",
    ends={
        Property(name="SectionMixedContent21", type=docbook_Section, multiplicity=Multiplicity(1, 1)),
        Property(name="section", type=docbook_SectionMixedContent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bookinfo8: BinaryAssociation = BinaryAssociation(
    name="bookinfo8",
    ends={
        Property(name="Bookinfo9", type=docbook_Author, multiplicity=Multiplicity(1, 1)),
        Property(name="author", type=docbook_Bookinfo, multiplicity=Multiplicity(0, 1))
    }
)
bookinfo10: BinaryAssociation = BinaryAssociation(
    name="bookinfo10",
    ends={
        Property(name="Bookinfo11", type=docbook_Subtitle, multiplicity=Multiplicity(1, 1)),
        Property(name="subtitle", type=docbook_Bookinfo, multiplicity=Multiplicity(0, 1))
    }
)
book12: BinaryAssociation = BinaryAssociation(
    name="book12",
    ends={
        Property(name="Book13", type=docbook_Chapter, multiplicity=Multiplicity(1, 1)),
        Property(name="chapter", type=docbook_Book, multiplicity=Multiplicity(0, 1))
    }
)
mixedContent14: BinaryAssociation = BinaryAssociation(
    name="mixedContent14",
    ends={
        Property(name="SectionMixedContent", type=docbook_Chapter, multiplicity=Multiplicity(1, 1)),
        Property(name="chapter15", type=docbook_SectionMixedContent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
titledElement16: BinaryAssociation = BinaryAssociation(
    name="titledElement16",
    ends={
        Property(name="TitledElement", type=docbook_Title, multiplicity=Multiplicity(1, 1)),
        Property(name="title", type=docbook_TitledElement, multiplicity=Multiplicity(0, 1))
    }
)
content17: BinaryAssociation = BinaryAssociation(
    name="content17",
    ends={
        Property(name="ParaMixedContent", type=docbook_Title, multiplicity=Multiplicity(1, 1)),
        Property(name="titleElement", type=docbook_ParaMixedContent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
content18: BinaryAssociation = BinaryAssociation(
    name="content18",
    ends={
        Property(name="ParaMixedContent19", type=docbook_Para, multiplicity=Multiplicity(1, 1)),
        Property(name="para", type=docbook_ParaMixedContent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
chapter22: BinaryAssociation = BinaryAssociation(
    name="chapter22",
    ends={
        Property(name="Chapter23", type=docbook_SectionMixedContent, multiplicity=Multiplicity(1, 1)),
        Property(name="mixedContent", type=docbook_Chapter, multiplicity=Multiplicity(0, 1))
    }
)
section24: BinaryAssociation = BinaryAssociation(
    name="section24",
    ends={
        Property(name="Section", type=docbook_SectionMixedContent, multiplicity=Multiplicity(1, 1)),
        Property(name="content", type=docbook_Section, multiplicity=Multiplicity(0, 1))
    }
)
title25: BinaryAssociation = BinaryAssociation(
    name="title25",
    ends={
        Property(name="Title", type=docbook_TitledElement, multiplicity=Multiplicity(1, 1)),
        Property(name="titledElement", type=docbook_Title, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
para26: BinaryAssociation = BinaryAssociation(
    name="para26",
    ends={
        Property(name="Para", type=docbook_ParaMixedContent, multiplicity=Multiplicity(1, 1)),
        Property(name="content27", type=docbook_Para, multiplicity=Multiplicity(0, 1))
    }
)
titleElement28: BinaryAssociation = BinaryAssociation(
    name="titleElement28",
    ends={
        Property(name="Title30", type=docbook_ParaMixedContent, multiplicity=Multiplicity(1, 1)),
        Property(name="content29", type=docbook_Title, multiplicity=Multiplicity(0, 1))
    }
)
emphasis31: BinaryAssociation = BinaryAssociation(
    name="emphasis31",
    ends={
        Property(name="Emphasis", type=docbook_ParaMixedContent, multiplicity=Multiplicity(1, 1)),
        Property(name="content32", type=docbook_Emphasis, multiplicity=Multiplicity(0, 1))
    }
)
ulink33: BinaryAssociation = BinaryAssociation(
    name="ulink33",
    ends={
        Property(name="Ulink", type=docbook_ParaMixedContent, multiplicity=Multiplicity(1, 1)),
        Property(name="content34", type=docbook_Ulink, multiplicity=Multiplicity(0, 1))
    }
)
link35: BinaryAssociation = BinaryAssociation(
    name="link35",
    ends={
        Property(name="Link", type=docbook_ParaMixedContent, multiplicity=Multiplicity(1, 1)),
        Property(name="content36", type=docbook_Link, multiplicity=Multiplicity(0, 1))
    }
)
content37: BinaryAssociation = BinaryAssociation(
    name="content37",
    ends={
        Property(name="MediaObject", type=docbook_Figure, multiplicity=Multiplicity(1, 1)),
        Property(name="figure", type=docbook_MediaObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
content38: BinaryAssociation = BinaryAssociation(
    name="content38",
    ends={
        Property(name="ParaMixedContent39", type=docbook_Emphasis, multiplicity=Multiplicity(1, 1)),
        Property(name="emphasis", type=docbook_ParaMixedContent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
content40: BinaryAssociation = BinaryAssociation(
    name="content40",
    ends={
        Property(name="ParaMixedContent41", type=docbook_Link, multiplicity=Multiplicity(1, 1)),
        Property(name="link", type=docbook_ParaMixedContent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
content42: BinaryAssociation = BinaryAssociation(
    name="content42",
    ends={
        Property(name="ParaMixedContent43", type=docbook_Ulink, multiplicity=Multiplicity(1, 1)),
        Property(name="ulink", type=docbook_ParaMixedContent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
figure44: BinaryAssociation = BinaryAssociation(
    name="figure44",
    ends={
        Property(name="Figure", type=docbook_MediaObject, multiplicity=Multiplicity(1, 1)),
        Property(name="content45", type=docbook_Figure, multiplicity=Multiplicity(0, 1))
    }
)
content46: BinaryAssociation = BinaryAssociation(
    name="content46",
    ends={
        Property(name="ImageObject", type=docbook_MediaObject, multiplicity=Multiplicity(1, 1)),
        Property(name="mediaObject", type=docbook_ImageObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mediaObject47: BinaryAssociation = BinaryAssociation(
    name="mediaObject47",
    ends={
        Property(name="MediaObject49", type=docbook_ImageObject, multiplicity=Multiplicity(1, 1)),
        Property(name="content48", type=docbook_MediaObject, multiplicity=Multiplicity(0, 1))
    }
)
content50: BinaryAssociation = BinaryAssociation(
    name="content50",
    ends={
        Property(name="ImageData", type=docbook_ImageObject, multiplicity=Multiplicity(1, 1)),
        Property(name="imageObject", type=docbook_ImageData, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
imageObject51: BinaryAssociation = BinaryAssociation(
    name="imageObject51",
    ends={
        Property(name="ImageObject53", type=docbook_ImageData, multiplicity=Multiplicity(1, 1)),
        Property(name="content52", type=docbook_ImageObject, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_docbook_Book_XMLElement = Generalization(general=XMLElement, specific=docbook_Book)
gen_docbook_Bookinfo_XMLElement = Generalization(general=XMLElement, specific=docbook_Bookinfo)
gen_docbook_Section_SectionMixedContent = Generalization(general=SectionMixedContent, specific=docbook_Section)
gen_docbook_Section_TitledElement = Generalization(general=TitledElement, specific=docbook_Section)
gen_docbook_Section_XMLElement = Generalization(general=XMLElement, specific=docbook_Section)
gen_docbook_Chapter_TitledElement = Generalization(general=TitledElement, specific=docbook_Chapter)
gen_docbook_Chapter_XMLElement = Generalization(general=XMLElement, specific=docbook_Chapter)
gen_docbook_Para_SectionMixedContent = Generalization(general=SectionMixedContent, specific=docbook_Para)
gen_docbook_ParaMixedContent_SectionMixedContent = Generalization(general=SectionMixedContent, specific=docbook_ParaMixedContent)
gen_docbook_ProgramListing_Para = Generalization(general=Para, specific=docbook_ProgramListing)
gen_docbook_SimpleText_ParaMixedContent = Generalization(general=ParaMixedContent, specific=docbook_SimpleText)
gen_docbook_Figure_TitledElement = Generalization(general=TitledElement, specific=docbook_Figure)
gen_docbook_Figure_ParaMixedContent = Generalization(general=ParaMixedContent, specific=docbook_Figure)
gen_docbook_Emphasis_ParaMixedContent = Generalization(general=ParaMixedContent, specific=docbook_Emphasis)
gen_docbook_Tip_Para = Generalization(general=Para, specific=docbook_Tip)
gen_docbook_Warning_Para = Generalization(general=Para, specific=docbook_Warning)
gen_docbook_Link_ParaMixedContent = Generalization(general=ParaMixedContent, specific=docbook_Link)
gen_docbook_Ulink_ParaMixedContent = Generalization(general=ParaMixedContent, specific=docbook_Ulink)

# Domain Model
domain_model = DomainModel(
    name="docbook",
    types={docbook_Author, docbook_Book, XMLElement, docbook_Bookinfo, docbook_Chapter, docbook_Section, docbook_Subtitle, TitledElement, docbook_SectionMixedContent, docbook_Title, docbook_TitledElement, docbook_ParaMixedContent, docbook_Para, SectionMixedContent, docbook_XMLElement, docbook_Emphasis, docbook_Ulink, docbook_Link, docbook_ProgramListing, Para, docbook_SimpleText, ParaMixedContent, docbook_Figure, docbook_MediaObject, docbook_Tip, docbook_Warning, docbook_ImageObject, docbook_ImageData},
    associations={subtitle4, author6, bookinfo0, chapter1, book3, content20, bookinfo8, bookinfo10, book12, mixedContent14, titledElement16, content17, content18, chapter22, section24, title25, para26, titleElement28, emphasis31, ulink33, link35, content37, content38, content40, content42, figure44, content46, mediaObject47, content50, imageObject51},
    generalizations={gen_docbook_Book_XMLElement, gen_docbook_Bookinfo_XMLElement, gen_docbook_Section_SectionMixedContent, gen_docbook_Section_TitledElement, gen_docbook_Section_XMLElement, gen_docbook_Chapter_TitledElement, gen_docbook_Chapter_XMLElement, gen_docbook_Para_SectionMixedContent, gen_docbook_ParaMixedContent_SectionMixedContent, gen_docbook_ProgramListing_Para, gen_docbook_SimpleText_ParaMixedContent, gen_docbook_Figure_TitledElement, gen_docbook_Figure_ParaMixedContent, gen_docbook_Emphasis_ParaMixedContent, gen_docbook_Tip_Para, gen_docbook_Warning_Para, gen_docbook_Link_ParaMixedContent, gen_docbook_Ulink_ParaMixedContent},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)