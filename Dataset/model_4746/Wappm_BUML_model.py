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
AppTypes: Enumeration = Enumeration(
    name="AppTypes",
    literals={
            EnumerationLiteral(name="String"),
			EnumerationLiteral(name="Integer"),
			EnumerationLiteral(name="Float"),
			EnumerationLiteral(name="Double"),
			EnumerationLiteral(name="Boolean")
    }
)

# Classes
wappm_WebModel = Class(name="wappm::WebModel")
wappm_HypertextLayer = Class(name="wappm::HypertextLayer")
wappm_ContentLayer = Class(name="wappm::ContentLayer")
wappm_Page = Class(name="wappm::Page")
wappm_Link = Class(name="wappm::Link")
wappm_StaticPage = Class(name="wappm::StaticPage")
Page = Class(name="Page")
wappm_DynamicPage = Class(name="wappm::DynamicPage")
wappm_WebClass = Class(name="wappm::WebClass")
wappm_DetailPage = Class(name="wappm::DetailPage")
DynamicPage = Class(name="DynamicPage")
wappm_IndexPage = Class(name="wappm::IndexPage")
wappm_Attribute = Class(name="wappm::Attribute")
wappm_Reference = Class(name="wappm::Reference")

# wappm_WebModel class attributes and methods
wappm_WebModel_name: Property = Property(name="name", type=StringType)
wappm_WebModel.attributes={wappm_WebModel_name}

# wappm_HypertextLayer class attributes and methods
wappm_HypertextLayer_hyperName: Property = Property(name="hyperName", type=StringType)
wappm_HypertextLayer.attributes={wappm_HypertextLayer_hyperName}

# wappm_ContentLayer class attributes and methods
wappm_ContentLayer_contentName: Property = Property(name="contentName", type=StringType)
wappm_ContentLayer.attributes={wappm_ContentLayer_contentName}

# wappm_Page class attributes and methods
wappm_Page_name: Property = Property(name="name", type=StringType)
wappm_Page_path: Property = Property(name="path", type=StringType)
wappm_Page.attributes={wappm_Page_name, wappm_Page_path}

# wappm_Link class attributes and methods

# wappm_StaticPage class attributes and methods

# Page class attributes and methods

# wappm_DynamicPage class attributes and methods

# wappm_WebClass class attributes and methods
wappm_WebClass_name: Property = Property(name="name", type=StringType)
wappm_WebClass.attributes={wappm_WebClass_name}

# wappm_DetailPage class attributes and methods

# DynamicPage class attributes and methods

# wappm_IndexPage class attributes and methods
wappm_IndexPage_size: Property = Property(name="size", type=IntegerType)
wappm_IndexPage.attributes={wappm_IndexPage_size}

# wappm_Attribute class attributes and methods
wappm_Attribute_name: Property = Property(name="name", type=StringType)
wappm_Attribute_type: Property = Property(name="type", type=StringType)
wappm_Attribute.attributes={wappm_Attribute_name, wappm_Attribute_type}

# wappm_Reference class attributes and methods
wappm_Reference_name: Property = Property(name="name", type=StringType)
wappm_Reference_lowBound: Property = Property(name="lowBound", type=IntegerType)
wappm_Reference_upBound: Property = Property(name="upBound", type=IntegerType)
wappm_Reference.attributes={wappm_Reference_name, wappm_Reference_upBound, wappm_Reference_lowBound}

# Relationships
hypertext0: BinaryAssociation = BinaryAssociation(
    name="hypertext0",
    ends={
        Property(name="wappm_HypertextLayer", type=wappm_WebModel, multiplicity=Multiplicity(1, 1)),
        Property(name="wappm_WebModel", type=wappm_HypertextLayer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
content1: BinaryAssociation = BinaryAssociation(
    name="content1",
    ends={
        Property(name="wappm_ContentLayer", type=wappm_WebModel, multiplicity=Multiplicity(1, 1)),
        Property(name="wappm_WebModel2", type=wappm_ContentLayer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pages3: BinaryAssociation = BinaryAssociation(
    name="pages3",
    ends={
        Property(name="wappm_Page", type=wappm_HypertextLayer, multiplicity=Multiplicity(1, 1)),
        Property(name="wappm_HypertextLayer4", type=wappm_Page, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
links5: BinaryAssociation = BinaryAssociation(
    name="links5",
    ends={
        Property(name="wappm_Link", type=wappm_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="wappm_Page6", type=wappm_Link, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
references16: BinaryAssociation = BinaryAssociation(
    name="references16",
    ends={
        Property(name="wappm_Reference", type=wappm_WebClass, multiplicity=Multiplicity(1, 1)),
        Property(name="wappm_WebClass17", type=wappm_Reference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
displayedClass7: BinaryAssociation = BinaryAssociation(
    name="displayedClass7",
    ends={
        Property(name="wappm_WebClass", type=wappm_DynamicPage, multiplicity=Multiplicity(1, 1)),
        Property(name="wappm_DynamicPage", type=wappm_WebClass, multiplicity=Multiplicity(0, 1))
    }
)
page8: BinaryAssociation = BinaryAssociation(
    name="page8",
    ends={
        Property(name="wappm_Page10", type=wappm_Link, multiplicity=Multiplicity(1, 1)),
        Property(name="wappm_Link9", type=wappm_Page, multiplicity=Multiplicity(0, 1))
    }
)
classes11: BinaryAssociation = BinaryAssociation(
    name="classes11",
    ends={
        Property(name="wappm_WebClass13", type=wappm_ContentLayer, multiplicity=Multiplicity(1, 1)),
        Property(name="wappm_ContentLayer12", type=wappm_WebClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes14: BinaryAssociation = BinaryAssociation(
    name="attributes14",
    ends={
        Property(name="wappm_Attribute", type=wappm_WebClass, multiplicity=Multiplicity(1, 1)),
        Property(name="wappm_WebClass15", type=wappm_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_wappm_StaticPage_Page = Generalization(general=Page, specific=wappm_StaticPage)
gen_wappm_DynamicPage_Page = Generalization(general=Page, specific=wappm_DynamicPage)
gen_wappm_DetailPage_DynamicPage = Generalization(general=DynamicPage, specific=wappm_DetailPage)
gen_wappm_IndexPage_DynamicPage = Generalization(general=DynamicPage, specific=wappm_IndexPage)

# Domain Model
domain_model = DomainModel(
    name="wappm",
    types={wappm_WebModel, wappm_HypertextLayer, wappm_ContentLayer, wappm_Page, wappm_Link, wappm_StaticPage, Page, wappm_DynamicPage, wappm_WebClass, wappm_DetailPage, DynamicPage, wappm_IndexPage, wappm_Attribute, wappm_Reference, AppTypes},
    associations={hypertext0, content1, pages3, links5, references16, displayedClass7, page8, classes11, attributes14},
    generalizations={gen_wappm_StaticPage_Page, gen_wappm_DynamicPage_Page, gen_wappm_DetailPage_DynamicPage, gen_wappm_IndexPage_DynamicPage},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)