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

# Enumerations
SWMLTypes: Enumeration = Enumeration(
    name="SWMLTypes",
    literals={
            EnumerationLiteral(name="Boolean"),
			EnumerationLiteral(name="String"),
			EnumerationLiteral(name="Integer"),
			EnumerationLiteral(name="Float"),
			EnumerationLiteral(name="Email")
    }
)

# Classes
swml_WebModel = Class(name="swml::WebModel")
swml_HypertextLayer = Class(name="swml::HypertextLayer")
swml_Attribute = Class(name="swml::Attribute")
swml_Link = Class(name="swml::Link", is_abstract=True)
swml_IndexPage = Class(name="swml::IndexPage")
DynamicPage = Class(name="DynamicPage")
swml_ContentLayer = Class(name="swml::ContentLayer")
swml_Page = Class(name="swml::Page", is_abstract=True)
swml_Class = Class(name="swml::Class")
swml_DetailsPage = Class(name="swml::DetailsPage")
swml_DynamicPage = Class(name="swml::DynamicPage", is_abstract=True)
Page = Class(name="Page")
swml_StaticPage = Class(name="swml::StaticPage")
swml_NCLink = Class(name="swml::NCLink")
Link = Class(name="Link")
swml_CLink = Class(name="swml::CLink")

# swml_WebModel class attributes and methods
swml_WebModel_name: Property = Property(name="name", type=StringType)
swml_WebModel.attributes={swml_WebModel_name}

# swml_HypertextLayer class attributes and methods

# swml_Attribute class attributes and methods
swml_Attribute_name: Property = Property(name="name", type=StringType)
swml_Attribute_type: Property = Property(name="type", type=StringType)
swml_Attribute.attributes={swml_Attribute_name, swml_Attribute_type}

# swml_Link class attributes and methods

# swml_IndexPage class attributes and methods
swml_IndexPage_size: Property = Property(name="size", type=IntegerType)
swml_IndexPage.attributes={swml_IndexPage_size}

# DynamicPage class attributes and methods

# swml_ContentLayer class attributes and methods

# swml_Page class attributes and methods
swml_Page_name: Property = Property(name="name", type=StringType)
swml_Page.attributes={swml_Page_name}

# swml_Class class attributes and methods
swml_Class_name: Property = Property(name="name", type=StringType)
swml_Class.attributes={swml_Class_name}

# swml_DetailsPage class attributes and methods

# swml_DynamicPage class attributes and methods

# Page class attributes and methods

# swml_StaticPage class attributes and methods

# swml_NCLink class attributes and methods

# Link class attributes and methods

# swml_CLink class attributes and methods

# Relationships
hypertext0: BinaryAssociation = BinaryAssociation(
    name="hypertext0",
    ends={
        Property(name="swml_HypertextLayer", type=swml_WebModel, multiplicity=Multiplicity(1, 1)),
        Property(name="swml_WebModel", type=swml_HypertextLayer, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
attributes10: BinaryAssociation = BinaryAssociation(
    name="attributes10",
    ends={
        Property(name="swml_Attribute", type=swml_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="swml_Class11", type=swml_Attribute, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
representativeAttribute12: BinaryAssociation = BinaryAssociation(
    name="representativeAttribute12",
    ends={
        Property(name="swml_Attribute14", type=swml_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="swml_Class13", type=swml_Attribute, multiplicity=Multiplicity(1, 1))
    }
)
links15: BinaryAssociation = BinaryAssociation(
    name="links15",
    ends={
        Property(name="swml_Link", type=swml_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="swml_Page16", type=swml_Link, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
content1: BinaryAssociation = BinaryAssociation(
    name="content1",
    ends={
        Property(name="swml_ContentLayer", type=swml_WebModel, multiplicity=Multiplicity(1, 1)),
        Property(name="swml_WebModel2", type=swml_ContentLayer, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
pages3: BinaryAssociation = BinaryAssociation(
    name="pages3",
    ends={
        Property(name="swml_Page", type=swml_HypertextLayer, multiplicity=Multiplicity(1, 1)),
        Property(name="swml_HypertextLayer4", type=swml_Page, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
homePage5: BinaryAssociation = BinaryAssociation(
    name="homePage5",
    ends={
        Property(name="swml_Page7", type=swml_HypertextLayer, multiplicity=Multiplicity(1, 1)),
        Property(name="swml_HypertextLayer6", type=swml_Page, multiplicity=Multiplicity(1, 1))
    }
)
classes8: BinaryAssociation = BinaryAssociation(
    name="classes8",
    ends={
        Property(name="swml_Class", type=swml_ContentLayer, multiplicity=Multiplicity(1, 1)),
        Property(name="swml_ContentLayer9", type=swml_Class, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
displayedClass17: BinaryAssociation = BinaryAssociation(
    name="displayedClass17",
    ends={
        Property(name="swml_Class18", type=swml_DynamicPage, multiplicity=Multiplicity(1, 1)),
        Property(name="swml_DynamicPage", type=swml_Class, multiplicity=Multiplicity(1, 1))
    }
)
target19: BinaryAssociation = BinaryAssociation(
    name="target19",
    ends={
        Property(name="swml_Page21", type=swml_Link, multiplicity=Multiplicity(1, 1)),
        Property(name="swml_Link20", type=swml_Page, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_swml_IndexPage_DynamicPage = Generalization(general=DynamicPage, specific=swml_IndexPage)
gen_swml_DetailsPage_DynamicPage = Generalization(general=DynamicPage, specific=swml_DetailsPage)
gen_swml_DynamicPage_Page = Generalization(general=Page, specific=swml_DynamicPage)
gen_swml_StaticPage_Page = Generalization(general=Page, specific=swml_StaticPage)
gen_swml_NCLink_Link = Generalization(general=Link, specific=swml_NCLink)
gen_swml_CLink_Link = Generalization(general=Link, specific=swml_CLink)

# Domain Model
domain_model = DomainModel(
    name="swml",
    types={swml_WebModel, swml_HypertextLayer, swml_Attribute, swml_Link, swml_IndexPage, DynamicPage, swml_ContentLayer, swml_Page, swml_Class, swml_DetailsPage, swml_DynamicPage, Page, swml_StaticPage, swml_NCLink, Link, swml_CLink, SWMLTypes},
    associations={hypertext0, attributes10, representativeAttribute12, links15, content1, pages3, homePage5, classes8, displayedClass17, target19},
    generalizations={gen_swml_IndexPage_DynamicPage, gen_swml_DetailsPage_DynamicPage, gen_swml_DynamicPage_Page, gen_swml_StaticPage_Page, gen_swml_NCLink_Link, gen_swml_CLink_Link},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)