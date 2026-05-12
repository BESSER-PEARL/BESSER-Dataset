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
LaTeX_ValuedElement = Class(name="LaTeX_ValuedElement", is_abstract=True)
LaTeX_Type = Class(name="LaTeX_Type")
ValuedElement = Class(name="ValuedElement")
LaTeX_Date = Class(name="LaTeX_Date")
LaTeX_Author = Class(name="LaTeX_Author")
Name = Class(name="Name")
LaTeX_Adress = Class(name="LaTeX_Adress")
LaTeX_Organisation = Class(name="LaTeX_Organisation")
LaTeX_Title = Class(name="LaTeX_Title")
LaTeX_Name = Class(name="LaTeX_Name")
Author = Class(name="Author")
Organisation = Class(name="Organisation")
LaTeX_Phone = Class(name="LaTeX_Phone")
LaTeX_Fax = Class(name="LaTeX_Fax")
LaTeX_EMail = Class(name="LaTeX_EMail")
LaTeX_Heading = Class(name="LaTeX_Heading")
Phone = Class(name="Phone")
Fax = Class(name="Fax")
EMail = Class(name="EMail")
Adress = Class(name="Adress")
LaTeX_Abstract = Class(name="LaTeX_Abstract")
Heading = Class(name="Heading")
LaTeX_SectionBody = Class(name="LaTeX_SectionBody")
Corps = Class(name="Corps")
Section = Class(name="Section")
LaTeX_Corps = Class(name="LaTeX_Corps", is_abstract=True)
SectionBody = Class(name="SectionBody")
LaTeX_Value = Class(name="LaTeX_Value")
LaTeX_Cite = Class(name="LaTeX_Cite")
LaTeX_Path = Class(name="LaTeX_Path")
LaTeX_Keywords = Class(name="LaTeX_Keywords")
LaTeX_Figure = Class(name="LaTeX_Figure")
Path = Class(name="Path")
Label = Class(name="Label")
Title = Class(name="Title")
LaTeX_Item = Class(name="LaTeX_Item")
Items = Class(name="Items")
Enumerate = Class(name="Enumerate")
LaTeX_Label = Class(name="LaTeX_Label")
Item = Class(name="Item")
LaTeX_Enumerate = Class(name="LaTeX_Enumerate")
LaTeX_Section = Class(name="LaTeX_Section")
LaTeX_Description = Class(name="LaTeX_Description")
Date = Class(name="Date")
LaTeX_Items = Class(name="LaTeX_Items")
Description = Class(name="Description")
Bibliography = Class(name="Bibliography")
LaTeX_Bibliography = Class(name="LaTeX_Bibliography")
Citation = Class(name="Citation")
DocumentBody = Class(name="DocumentBody")
LaTeX_DocumentBody = Class(name="LaTeX_DocumentBody")
LaTeX_Citation = Class(name="LaTeX_Citation")
Document = Class(name="Document")
LaTeX_Document = Class(name="LaTeX_Document")
Type = Class(name="Type")
Keywords = Class(name="Keywords")
Abstract = Class(name="Abstract")

# LaTeX_ValuedElement class attributes and methods
LaTeX_ValuedElement_value: Property = Property(name="value", type=StringType)
LaTeX_ValuedElement.attributes={LaTeX_ValuedElement_value}

# LaTeX_Type class attributes and methods

# ValuedElement class attributes and methods

# LaTeX_Date class attributes and methods

# LaTeX_Author class attributes and methods

# Name class attributes and methods

# LaTeX_Adress class attributes and methods

# LaTeX_Organisation class attributes and methods

# LaTeX_Title class attributes and methods

# LaTeX_Name class attributes and methods

# Author class attributes and methods

# Organisation class attributes and methods

# LaTeX_Phone class attributes and methods

# LaTeX_Fax class attributes and methods

# LaTeX_EMail class attributes and methods

# LaTeX_Heading class attributes and methods

# Phone class attributes and methods

# Fax class attributes and methods

# EMail class attributes and methods

# Adress class attributes and methods

# LaTeX_Abstract class attributes and methods

# Heading class attributes and methods

# LaTeX_SectionBody class attributes and methods

# Corps class attributes and methods

# Section class attributes and methods

# LaTeX_Corps class attributes and methods

# SectionBody class attributes and methods

# LaTeX_Value class attributes and methods

# LaTeX_Cite class attributes and methods

# LaTeX_Path class attributes and methods

# LaTeX_Keywords class attributes and methods

# LaTeX_Figure class attributes and methods

# Path class attributes and methods

# Label class attributes and methods

# Title class attributes and methods

# LaTeX_Item class attributes and methods

# Items class attributes and methods

# Enumerate class attributes and methods

# LaTeX_Label class attributes and methods

# Item class attributes and methods

# LaTeX_Enumerate class attributes and methods

# LaTeX_Section class attributes and methods

# LaTeX_Description class attributes and methods

# Date class attributes and methods

# LaTeX_Items class attributes and methods

# Description class attributes and methods

# Bibliography class attributes and methods

# LaTeX_Bibliography class attributes and methods

# Citation class attributes and methods

# DocumentBody class attributes and methods

# LaTeX_DocumentBody class attributes and methods

# LaTeX_Citation class attributes and methods

# Document class attributes and methods

# LaTeX_Document class attributes and methods

# Type class attributes and methods

# Keywords class attributes and methods

# Abstract class attributes and methods

# Relationships
organisation1: BinaryAssociation = BinaryAssociation(
    name="organisation1",
    ends={
        Property(name="Organisation", type=LaTeX_Name, multiplicity=Multiplicity(1, 1)),
        Property(name="names2", type=Organisation, multiplicity=Multiplicity(0, 1))
    }
)
names3: BinaryAssociation = BinaryAssociation(
    name="names3",
    ends={
        Property(name="Name", type=LaTeX_Author, multiplicity=Multiplicity(1, 1)),
        Property(name="author", type=Name, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
author0: BinaryAssociation = BinaryAssociation(
    name="author0",
    ends={
        Property(name="Author", type=LaTeX_Name, multiplicity=Multiplicity(1, 1)),
        Property(name="names", type=Author, multiplicity=Multiplicity(0, 1))
    }
)
organisations8: BinaryAssociation = BinaryAssociation(
    name="organisations8",
    ends={
        Property(name="Organisation9", type=LaTeX_Heading, multiplicity=Multiplicity(1, 1)),
        Property(name="heading", type=Organisation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
phone10: BinaryAssociation = BinaryAssociation(
    name="phone10",
    ends={
        Property(name="Phone", type=LaTeX_Heading, multiplicity=Multiplicity(1, 1)),
        Property(name="LaTeX_Heading", type=Phone, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
names4: BinaryAssociation = BinaryAssociation(
    name="names4",
    ends={
        Property(name="Name5", type=LaTeX_Organisation, multiplicity=Multiplicity(1, 1)),
        Property(name="organisation", type=Name, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
fax11: BinaryAssociation = BinaryAssociation(
    name="fax11",
    ends={
        Property(name="Fax", type=LaTeX_Heading, multiplicity=Multiplicity(1, 1)),
        Property(name="LaTeX_Heading12", type=Fax, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
email13: BinaryAssociation = BinaryAssociation(
    name="email13",
    ends={
        Property(name="EMail", type=LaTeX_Heading, multiplicity=Multiplicity(1, 1)),
        Property(name="LaTeX_Heading14", type=EMail, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
adress6: BinaryAssociation = BinaryAssociation(
    name="adress6",
    ends={
        Property(name="Adress", type=LaTeX_Organisation, multiplicity=Multiplicity(1, 1)),
        Property(name="LaTeX_Organisation", type=Adress, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
heading7: BinaryAssociation = BinaryAssociation(
    name="heading7",
    ends={
        Property(name="Heading", type=LaTeX_Organisation, multiplicity=Multiplicity(1, 1)),
        Property(name="organisations", type=Heading, multiplicity=Multiplicity(1, 1))
    }
)
corps15: BinaryAssociation = BinaryAssociation(
    name="corps15",
    ends={
        Property(name="Corps", type=LaTeX_SectionBody, multiplicity=Multiplicity(1, 1)),
        Property(name="sectionbody", type=Corps, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
section16: BinaryAssociation = BinaryAssociation(
    name="section16",
    ends={
        Property(name="Section", type=LaTeX_SectionBody, multiplicity=Multiplicity(1, 1)),
        Property(name="sectionBody", type=Section, multiplicity=Multiplicity(1, 1))
    }
)
sectionbody17: BinaryAssociation = BinaryAssociation(
    name="sectionbody17",
    ends={
        Property(name="SectionBody", type=LaTeX_Corps, multiplicity=Multiplicity(1, 1)),
        Property(name="corps", type=SectionBody, multiplicity=Multiplicity(1, 1))
    }
)
path18: BinaryAssociation = BinaryAssociation(
    name="path18",
    ends={
        Property(name="Path", type=LaTeX_Figure, multiplicity=Multiplicity(1, 1)),
        Property(name="LaTeX_Figure", type=Path, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
label19: BinaryAssociation = BinaryAssociation(
    name="label19",
    ends={
        Property(name="Label", type=LaTeX_Figure, multiplicity=Multiplicity(1, 1)),
        Property(name="LaTeX_Figure20", type=Label, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
title21: BinaryAssociation = BinaryAssociation(
    name="title21",
    ends={
        Property(name="Title", type=LaTeX_Figure, multiplicity=Multiplicity(1, 1)),
        Property(name="LaTeX_Figure22", type=Title, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
itemscontainer23: BinaryAssociation = BinaryAssociation(
    name="itemscontainer23",
    ends={
        Property(name="Items", type=LaTeX_Item, multiplicity=Multiplicity(1, 1)),
        Property(name="item", type=Items, multiplicity=Multiplicity(0, 1))
    }
)
enumeratecontainer24: BinaryAssociation = BinaryAssociation(
    name="enumeratecontainer24",
    ends={
        Property(name="Enumerate", type=LaTeX_Item, multiplicity=Multiplicity(1, 1)),
        Property(name="item25", type=Enumerate, multiplicity=Multiplicity(0, 1))
    }
)
item26: BinaryAssociation = BinaryAssociation(
    name="item26",
    ends={
        Property(name="Item", type=LaTeX_Items, multiplicity=Multiplicity(1, 1)),
        Property(name="itemscontainer", type=Item, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
item27: BinaryAssociation = BinaryAssociation(
    name="item27",
    ends={
        Property(name="Item28", type=LaTeX_Enumerate, multiplicity=Multiplicity(1, 1)),
        Property(name="enumeratecontainer", type=Item, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
title29: BinaryAssociation = BinaryAssociation(
    name="title29",
    ends={
        Property(name="Title30", type=LaTeX_Section, multiplicity=Multiplicity(1, 1)),
        Property(name="LaTeX_Section", type=Title, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
sectionBody31: BinaryAssociation = BinaryAssociation(
    name="sectionBody31",
    ends={
        Property(name="SectionBody32", type=LaTeX_Section, multiplicity=Multiplicity(1, 1)),
        Property(name="section", type=SectionBody, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
date33: BinaryAssociation = BinaryAssociation(
    name="date33",
    ends={
        Property(name="Date", type=LaTeX_Description, multiplicity=Multiplicity(1, 1)),
        Property(name="LaTeX_Description", type=Date, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
label34: BinaryAssociation = BinaryAssociation(
    name="label34",
    ends={
        Property(name="Label35", type=LaTeX_Citation, multiplicity=Multiplicity(1, 1)),
        Property(name="LaTeX_Citation", type=Label, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
author36: BinaryAssociation = BinaryAssociation(
    name="author36",
    ends={
        Property(name="Author38", type=LaTeX_Citation, multiplicity=Multiplicity(1, 1)),
        Property(name="LaTeX_Citation37", type=Author, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
description39: BinaryAssociation = BinaryAssociation(
    name="description39",
    ends={
        Property(name="Description", type=LaTeX_Citation, multiplicity=Multiplicity(1, 1)),
        Property(name="LaTeX_Citation40", type=Description, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
bibliography41: BinaryAssociation = BinaryAssociation(
    name="bibliography41",
    ends={
        Property(name="Bibliography", type=LaTeX_Citation, multiplicity=Multiplicity(1, 1)),
        Property(name="citations", type=Bibliography, multiplicity=Multiplicity(1, 1))
    }
)
citations42: BinaryAssociation = BinaryAssociation(
    name="citations42",
    ends={
        Property(name="Citation", type=LaTeX_Bibliography, multiplicity=Multiplicity(1, 1)),
        Property(name="bibliography", type=Citation, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
documentbody43: BinaryAssociation = BinaryAssociation(
    name="documentbody43",
    ends={
        Property(name="DocumentBody", type=LaTeX_Bibliography, multiplicity=Multiplicity(1, 1)),
        Property(name="bibliography44", type=DocumentBody, multiplicity=Multiplicity(1, 1))
    }
)
bibliography47: BinaryAssociation = BinaryAssociation(
    name="bibliography47",
    ends={
        Property(name="Bibliography48", type=LaTeX_DocumentBody, multiplicity=Multiplicity(1, 1)),
        Property(name="documentbody", type=Bibliography, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
document49: BinaryAssociation = BinaryAssociation(
    name="document49",
    ends={
        Property(name="Document", type=LaTeX_DocumentBody, multiplicity=Multiplicity(1, 1)),
        Property(name="documentbody50", type=Document, multiplicity=Multiplicity(1, 1))
    }
)
type51: BinaryAssociation = BinaryAssociation(
    name="type51",
    ends={
        Property(name="Type", type=LaTeX_Document, multiplicity=Multiplicity(1, 1)),
        Property(name="LaTeX_Document", type=Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
title52: BinaryAssociation = BinaryAssociation(
    name="title52",
    ends={
        Property(name="Title54", type=LaTeX_Document, multiplicity=Multiplicity(1, 1)),
        Property(name="LaTeX_Document53", type=Title, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
author55: BinaryAssociation = BinaryAssociation(
    name="author55",
    ends={
        Property(name="Author57", type=LaTeX_Document, multiplicity=Multiplicity(1, 1)),
        Property(name="LaTeX_Document56", type=Author, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
date58: BinaryAssociation = BinaryAssociation(
    name="date58",
    ends={
        Property(name="Date60", type=LaTeX_Document, multiplicity=Multiplicity(1, 1)),
        Property(name="LaTeX_Document59", type=Date, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
heading61: BinaryAssociation = BinaryAssociation(
    name="heading61",
    ends={
        Property(name="Heading63", type=LaTeX_Document, multiplicity=Multiplicity(1, 1)),
        Property(name="LaTeX_Document62", type=Heading, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sections45: BinaryAssociation = BinaryAssociation(
    name="sections45",
    ends={
        Property(name="Section46", type=LaTeX_DocumentBody, multiplicity=Multiplicity(1, 1)),
        Property(name="LaTeX_DocumentBody", type=Section, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
keywords66: BinaryAssociation = BinaryAssociation(
    name="keywords66",
    ends={
        Property(name="Keywords", type=LaTeX_Document, multiplicity=Multiplicity(1, 1)),
        Property(name="LaTeX_Document67", type=Keywords, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
documentbody68: BinaryAssociation = BinaryAssociation(
    name="documentbody68",
    ends={
        Property(name="DocumentBody69", type=LaTeX_Document, multiplicity=Multiplicity(1, 1)),
        Property(name="document", type=DocumentBody, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
abstract64: BinaryAssociation = BinaryAssociation(
    name="abstract64",
    ends={
        Property(name="Abstract", type=LaTeX_Document, multiplicity=Multiplicity(1, 1)),
        Property(name="LaTeX_Document65", type=Abstract, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_LaTeX_Type_ValuedElement = Generalization(general=ValuedElement, specific=LaTeX_Type)
gen_LaTeX_Date_ValuedElement = Generalization(general=ValuedElement, specific=LaTeX_Date)
gen_LaTeX_Adress_ValuedElement = Generalization(general=ValuedElement, specific=LaTeX_Adress)
gen_LaTeX_Title_ValuedElement = Generalization(general=ValuedElement, specific=LaTeX_Title)
gen_LaTeX_Name_ValuedElement = Generalization(general=ValuedElement, specific=LaTeX_Name)
gen_LaTeX_Phone_ValuedElement = Generalization(general=ValuedElement, specific=LaTeX_Phone)
gen_LaTeX_Fax_ValuedElement = Generalization(general=ValuedElement, specific=LaTeX_Fax)
gen_LaTeX_EMail_ValuedElement = Generalization(general=ValuedElement, specific=LaTeX_EMail)
gen_LaTeX_Value_Corps = Generalization(general=Corps, specific=LaTeX_Value)
gen_LaTeX_Value_ValuedElement = Generalization(general=ValuedElement, specific=LaTeX_Value)
gen_LaTeX_Cite_Corps = Generalization(general=Corps, specific=LaTeX_Cite)
gen_LaTeX_Cite_ValuedElement = Generalization(general=ValuedElement, specific=LaTeX_Cite)
gen_LaTeX_Path_ValuedElement = Generalization(general=ValuedElement, specific=LaTeX_Path)
gen_LaTeX_Abstract_ValuedElement = Generalization(general=ValuedElement, specific=LaTeX_Abstract)
gen_LaTeX_Keywords_ValuedElement = Generalization(general=ValuedElement, specific=LaTeX_Keywords)
gen_LaTeX_Figure_Corps = Generalization(general=Corps, specific=LaTeX_Figure)
gen_LaTeX_Item_ValuedElement = Generalization(general=ValuedElement, specific=LaTeX_Item)
gen_LaTeX_Label_ValuedElement = Generalization(general=ValuedElement, specific=LaTeX_Label)
gen_LaTeX_Enumerate_Corps = Generalization(general=Corps, specific=LaTeX_Enumerate)
gen_LaTeX_Section_Corps = Generalization(general=Corps, specific=LaTeX_Section)
gen_LaTeX_Description_ValuedElement = Generalization(general=ValuedElement, specific=LaTeX_Description)
gen_LaTeX_Items_Corps = Generalization(general=Corps, specific=LaTeX_Items)

# Domain Model
domain_model = DomainModel(
    name="PrimitiveTypes",
    types={LaTeX_ValuedElement, LaTeX_Type, ValuedElement, LaTeX_Date, LaTeX_Author, Name, LaTeX_Adress, LaTeX_Organisation, LaTeX_Title, LaTeX_Name, Author, Organisation, LaTeX_Phone, LaTeX_Fax, LaTeX_EMail, LaTeX_Heading, Phone, Fax, EMail, Adress, LaTeX_Abstract, Heading, LaTeX_SectionBody, Corps, Section, LaTeX_Corps, SectionBody, LaTeX_Value, LaTeX_Cite, LaTeX_Path, LaTeX_Keywords, LaTeX_Figure, Path, Label, Title, LaTeX_Item, Items, Enumerate, LaTeX_Label, Item, LaTeX_Enumerate, LaTeX_Section, LaTeX_Description, Date, LaTeX_Items, Description, Bibliography, LaTeX_Bibliography, Citation, DocumentBody, LaTeX_DocumentBody, LaTeX_Citation, Document, LaTeX_Document, Type, Keywords, Abstract},
    associations={organisation1, names3, author0, organisations8, phone10, names4, fax11, email13, adress6, heading7, corps15, section16, sectionbody17, path18, label19, title21, itemscontainer23, enumeratecontainer24, item26, item27, title29, sectionBody31, date33, label34, author36, description39, bibliography41, citations42, documentbody43, bibliography47, document49, type51, title52, author55, date58, heading61, sections45, keywords66, documentbody68, abstract64},
    generalizations={gen_LaTeX_Type_ValuedElement, gen_LaTeX_Date_ValuedElement, gen_LaTeX_Adress_ValuedElement, gen_LaTeX_Title_ValuedElement, gen_LaTeX_Name_ValuedElement, gen_LaTeX_Phone_ValuedElement, gen_LaTeX_Fax_ValuedElement, gen_LaTeX_EMail_ValuedElement, gen_LaTeX_Value_Corps, gen_LaTeX_Value_ValuedElement, gen_LaTeX_Cite_Corps, gen_LaTeX_Cite_ValuedElement, gen_LaTeX_Path_ValuedElement, gen_LaTeX_Abstract_ValuedElement, gen_LaTeX_Keywords_ValuedElement, gen_LaTeX_Figure_Corps, gen_LaTeX_Item_ValuedElement, gen_LaTeX_Label_ValuedElement, gen_LaTeX_Enumerate_Corps, gen_LaTeX_Section_Corps, gen_LaTeX_Description_ValuedElement, gen_LaTeX_Items_Corps},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)