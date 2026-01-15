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
swml_v2_Link = Class(name="swml::v2::Link")
swml_v2_WebModel = Class(name="swml::v2::WebModel")
swml_v2_NavigationLayer = Class(name="swml::v2::NavigationLayer")
swml_v2_ContentLayer = Class(name="swml::v2::ContentLayer")
swml_v2_Page = Class(name="swml::v2::Page", is_abstract=True)
swml_v2_Class = Class(name="swml::v2::Class")
swml_v2_Attribute = Class(name="swml::v2::Attribute")
swml_v2_IndexPage = Class(name="swml::v2::IndexPage")
DynamicPage = Class(name="DynamicPage")
swml_v2_DetailsPage = Class(name="swml::v2::DetailsPage")
swml_v2_DynamicPage = Class(name="swml::v2::DynamicPage", is_abstract=True)
Page = Class(name="Page")
swml_v2_StaticPage = Class(name="swml::v2::StaticPage")
swml_v2_NCLink = Class(name="swml::v2::NCLink")
Link = Class(name="Link")
swml_v2_CLink = Class(name="swml::v2::CLink")

# swml_v2_Link class attributes and methods

# swml_v2_WebModel class attributes and methods
swml_v2_WebModel_name: Property = Property(name="name", type=StringType)
swml_v2_WebModel.attributes={swml_v2_WebModel_name}

# swml_v2_NavigationLayer class attributes and methods

# swml_v2_ContentLayer class attributes and methods

# swml_v2_Page class attributes and methods
swml_v2_Page_name: Property = Property(name="name", type=StringType)
swml_v2_Page.attributes={swml_v2_Page_name}

# swml_v2_Class class attributes and methods
swml_v2_Class_name: Property = Property(name="name", type=StringType)
swml_v2_Class.attributes={swml_v2_Class_name}

# swml_v2_Attribute class attributes and methods
swml_v2_Attribute_name: Property = Property(name="name", type=StringType)
swml_v2_Attribute_type: Property = Property(name="type", type=StringType)
swml_v2_Attribute.attributes={swml_v2_Attribute_type, swml_v2_Attribute_name}

# swml_v2_IndexPage class attributes and methods
swml_v2_IndexPage_size: Property = Property(name="size", type=IntegerType)
swml_v2_IndexPage.attributes={swml_v2_IndexPage_size}

# DynamicPage class attributes and methods

# swml_v2_DetailsPage class attributes and methods

# swml_v2_DynamicPage class attributes and methods

# Page class attributes and methods

# swml_v2_StaticPage class attributes and methods

# swml_v2_NCLink class attributes and methods

# Link class attributes and methods

# swml_v2_CLink class attributes and methods

# Relationships
links15: BinaryAssociation = BinaryAssociation(
    name="links15",
    ends={
        Property(name="swml_v2_Link", type=swml_v2_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="swml_v2_Page16", type=swml_v2_Link, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hypertext0: BinaryAssociation = BinaryAssociation(
    name="hypertext0",
    ends={
        Property(name="swml_v2_NavigationLayer", type=swml_v2_WebModel, multiplicity=Multiplicity(1, 1)),
        Property(name="swml_v2_WebModel", type=swml_v2_NavigationLayer, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
content1: BinaryAssociation = BinaryAssociation(
    name="content1",
    ends={
        Property(name="swml_v2_ContentLayer", type=swml_v2_WebModel, multiplicity=Multiplicity(1, 1)),
        Property(name="swml_v2_WebModel2", type=swml_v2_ContentLayer, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
pages3: BinaryAssociation = BinaryAssociation(
    name="pages3",
    ends={
        Property(name="swml_v2_Page", type=swml_v2_NavigationLayer, multiplicity=Multiplicity(1, 1)),
        Property(name="swml_v2_NavigationLayer4", type=swml_v2_Page, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
homePage5: BinaryAssociation = BinaryAssociation(
    name="homePage5",
    ends={
        Property(name="swml_v2_Page7", type=swml_v2_NavigationLayer, multiplicity=Multiplicity(1, 1)),
        Property(name="swml_v2_NavigationLayer6", type=swml_v2_Page, multiplicity=Multiplicity(1, 1))
    }
)
classes8: BinaryAssociation = BinaryAssociation(
    name="classes8",
    ends={
        Property(name="swml_v2_Class", type=swml_v2_ContentLayer, multiplicity=Multiplicity(1, 1)),
        Property(name="swml_v2_ContentLayer9", type=swml_v2_Class, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
attributes10: BinaryAssociation = BinaryAssociation(
    name="attributes10",
    ends={
        Property(name="swml_v2_Attribute", type=swml_v2_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="swml_v2_Class11", type=swml_v2_Attribute, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
representativeAttribute12: BinaryAssociation = BinaryAssociation(
    name="representativeAttribute12",
    ends={
        Property(name="swml_v2_Attribute14", type=swml_v2_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="swml_v2_Class13", type=swml_v2_Attribute, multiplicity=Multiplicity(1, 1))
    }
)
displayedClass17: BinaryAssociation = BinaryAssociation(
    name="displayedClass17",
    ends={
        Property(name="swml_v2_Class18", type=swml_v2_DynamicPage, multiplicity=Multiplicity(1, 1)),
        Property(name="swml_v2_DynamicPage", type=swml_v2_Class, multiplicity=Multiplicity(1, 1))
    }
)
target19: BinaryAssociation = BinaryAssociation(
    name="target19",
    ends={
        Property(name="swml_v2_Page21", type=swml_v2_Link, multiplicity=Multiplicity(1, 1)),
        Property(name="swml_v2_Link20", type=swml_v2_Page, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_swml_v2_IndexPage_DynamicPage = Generalization(general=DynamicPage, specific=swml_v2_IndexPage)
gen_swml_v2_DetailsPage_DynamicPage = Generalization(general=DynamicPage, specific=swml_v2_DetailsPage)
gen_swml_v2_DynamicPage_Page = Generalization(general=Page, specific=swml_v2_DynamicPage)
gen_swml_v2_StaticPage_Page = Generalization(general=Page, specific=swml_v2_StaticPage)
gen_swml_v2_NCLink_Link = Generalization(general=Link, specific=swml_v2_NCLink)
gen_swml_v2_CLink_Link = Generalization(general=Link, specific=swml_v2_CLink)

# Domain Model
domain_model = DomainModel(
    name="swml_v2",
    types={swml_v2_Link, swml_v2_WebModel, swml_v2_NavigationLayer, swml_v2_ContentLayer, swml_v2_Page, swml_v2_Class, swml_v2_Attribute, swml_v2_IndexPage, DynamicPage, swml_v2_DetailsPage, swml_v2_DynamicPage, Page, swml_v2_StaticPage, swml_v2_NCLink, Link, swml_v2_CLink, SWMLTypes},
    associations={links15, hypertext0, content1, pages3, homePage5, classes8, attributes10, representativeAttribute12, displayedClass17, target19},
    generalizations={gen_swml_v2_IndexPage_DynamicPage, gen_swml_v2_DetailsPage_DynamicPage, gen_swml_v2_DynamicPage_Page, gen_swml_v2_StaticPage_Page, gen_swml_v2_NCLink_Link, gen_swml_v2_CLink_Link},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)