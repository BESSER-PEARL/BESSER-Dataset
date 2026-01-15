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
DataType: Enumeration = Enumeration(
    name="DataType",
    literals={
            EnumerationLiteral(name="String"),
			EnumerationLiteral(name="Float"),
			EnumerationLiteral(name="Integer"),
			EnumerationLiteral(name="Boolean")
    }
)

# Classes
WebPage = Class(name="WebPage")
swml_Link = Class(name="swml::Link")
swml_DynamicPage = Class(name="swml::DynamicPage")
swml_Icon = Class(name="swml::Icon")
swml_WebApplication = Class(name="swml::WebApplication")
swml_Entity = Class(name="swml::Entity")
swml_StaticPage = Class(name="swml::StaticPage")
swml_Attribute = Class(name="swml::Attribute")
swml_Relationship = Class(name="swml::Relationship")
swml_WebPage = Class(name="swml::WebPage")
swml_EntityPage = Class(name="swml::EntityPage")
DynamicPage = Class(name="DynamicPage")
swml_IndexPage = Class(name="swml::IndexPage")

# WebPage class attributes and methods

# swml_Link class attributes and methods
swml_Link_href: Property = Property(name="href", type=StringType)
swml_Link.attributes={swml_Link_href}

# swml_DynamicPage class attributes and methods

# swml_Icon class attributes and methods
swml_Icon_image: Property = Property(name="image", type=StringType)
swml_Icon.attributes={swml_Icon_image}

# swml_WebApplication class attributes and methods
swml_WebApplication_name: Property = Property(name="name", type=StringType)
swml_WebApplication.attributes={swml_WebApplication_name}

# swml_Entity class attributes and methods
swml_Entity_name: Property = Property(name="name", type=StringType)
swml_Entity.attributes={swml_Entity_name}

# swml_StaticPage class attributes and methods

# swml_Attribute class attributes and methods
swml_Attribute_name: Property = Property(name="name", type=StringType)
swml_Attribute_dataType: Property = Property(name="dataType", type=StringType)
swml_Attribute.attributes={swml_Attribute_dataType, swml_Attribute_name}

# swml_Relationship class attributes and methods
swml_Relationship_role: Property = Property(name="role", type=StringType)
swml_Relationship_lowerBound: Property = Property(name="lowerBound", type=IntegerType)
swml_Relationship_upperBound: Property = Property(name="upperBound", type=IntegerType)
swml_Relationship.attributes={swml_Relationship_role, swml_Relationship_lowerBound, swml_Relationship_upperBound}

# swml_WebPage class attributes and methods
swml_WebPage_relativeUrl: Property = Property(name="relativeUrl", type=StringType)
swml_WebPage_title: Property = Property(name="title", type=StringType)
swml_WebPage.attributes={swml_WebPage_title, swml_WebPage_relativeUrl}

# swml_EntityPage class attributes and methods

# DynamicPage class attributes and methods

# swml_IndexPage class attributes and methods

# Relationships
links13: BinaryAssociation = BinaryAssociation(
    name="links13",
    ends={
        Property(name="swml_Link", type=swml_StaticPage, multiplicity=Multiplicity(1, 1)),
        Property(name="swml_StaticPage14", type=swml_Link, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entities0: BinaryAssociation = BinaryAssociation(
    name="entities0",
    ends={
        Property(name="swml_Entity", type=swml_WebApplication, multiplicity=Multiplicity(1, 1)),
        Property(name="swml_WebApplication", type=swml_Entity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
homePage1: BinaryAssociation = BinaryAssociation(
    name="homePage1",
    ends={
        Property(name="swml_StaticPage", type=swml_WebApplication, multiplicity=Multiplicity(1, 1)),
        Property(name="swml_WebApplication2", type=swml_StaticPage, multiplicity=Multiplicity(1, 1))
    }
)
attributes3: BinaryAssociation = BinaryAssociation(
    name="attributes3",
    ends={
        Property(name="swml_Attribute", type=swml_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="swml_Entity4", type=swml_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
id5: BinaryAssociation = BinaryAssociation(
    name="id5",
    ends={
        Property(name="swml_Attribute7", type=swml_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="swml_Entity6", type=swml_Attribute, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
relationships8: BinaryAssociation = BinaryAssociation(
    name="relationships8",
    ends={
        Property(name="swml_Relationship", type=swml_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="swml_Entity9", type=swml_Relationship, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referencedEntity10: BinaryAssociation = BinaryAssociation(
    name="referencedEntity10",
    ends={
        Property(name="swml_Entity12", type=swml_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="swml_Relationship11", type=swml_Entity, multiplicity=Multiplicity(1, 1))
    }
)
icon15: BinaryAssociation = BinaryAssociation(
    name="icon15",
    ends={
        Property(name="swml_Icon", type=swml_DynamicPage, multiplicity=Multiplicity(1, 1)),
        Property(name="swml_DynamicPage", type=swml_Icon, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type16: BinaryAssociation = BinaryAssociation(
    name="type16",
    ends={
        Property(name="swml_Entity18", type=swml_DynamicPage, multiplicity=Multiplicity(1, 1)),
        Property(name="swml_DynamicPage17", type=swml_Entity, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_swml_StaticPage_WebPage = Generalization(general=WebPage, specific=swml_StaticPage)
gen_swml_DynamicPage_WebPage = Generalization(general=WebPage, specific=swml_DynamicPage)
gen_swml_EntityPage_DynamicPage = Generalization(general=DynamicPage, specific=swml_EntityPage)
gen_swml_IndexPage_DynamicPage = Generalization(general=DynamicPage, specific=swml_IndexPage)

# Domain Model
domain_model = DomainModel(
    name="swml",
    types={WebPage, swml_Link, swml_DynamicPage, swml_Icon, swml_WebApplication, swml_Entity, swml_StaticPage, swml_Attribute, swml_Relationship, swml_WebPage, swml_EntityPage, DynamicPage, swml_IndexPage, DataType},
    associations={links13, entities0, homePage1, attributes3, id5, relationships8, referencedEntity10, icon15, type16},
    generalizations={gen_swml_StaticPage_WebPage, gen_swml_DynamicPage_WebPage, gen_swml_EntityPage_DynamicPage, gen_swml_IndexPage_DynamicPage},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)