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
solution_WebApplication = Class(name="solution::WebApplication")
solution_Entity = Class(name="solution::Entity")
solution_WebPage = Class(name="solution::WebPage", is_abstract=True)
solution_StaticPage = Class(name="solution::StaticPage")
solution_Attribute = Class(name="solution::Attribute")
solution_Relationship = Class(name="solution::Relationship")
solution_Link = Class(name="solution::Link", is_abstract=True)
solution_NonContextualLink = Class(name="solution::NonContextualLink")
WebPage = Class(name="WebPage")
solution_DynamicPage = Class(name="solution::DynamicPage", is_abstract=True)
solution_EntityPage = Class(name="solution::EntityPage")
DynamicPage = Class(name="DynamicPage")
solution_IndexPage = Class(name="solution::IndexPage")
solution_CreatePage = Class(name="solution::CreatePage")
EditablePage = Class(name="EditablePage")
solution_UpdatePage = Class(name="solution::UpdatePage")
solution_DeletePage = Class(name="solution::DeletePage")
Link = Class(name="Link")
solution_ContextualLink = Class(name="solution::ContextualLink")
solution_EditablePage = Class(name="solution::EditablePage", is_abstract=True)
EntityPage = Class(name="EntityPage")

# solution_WebApplication class attributes and methods
solution_WebApplication_name: Property = Property(name="name", type=StringType)
solution_WebApplication_m_creationDateBeforeGoLive: Method = Method(name="creationDateBeforeGoLive", parameters={}, type=BooleanType)
solution_WebApplication.attributes={solution_WebApplication_name}
solution_WebApplication.methods={solution_WebApplication_m_creationDateBeforeGoLive}

# solution_Entity class attributes and methods
solution_Entity_name: Property = Property(name="name", type=StringType)
solution_Entity.attributes={solution_Entity_name}

# solution_WebPage class attributes and methods
solution_WebPage_name: Property = Property(name="name", type=StringType)
solution_WebPage_relativeUrl: Property = Property(name="relativeUrl", type=StringType)
solution_WebPage.attributes={solution_WebPage_relativeUrl, solution_WebPage_name}

# solution_StaticPage class attributes and methods

# solution_Attribute class attributes and methods
solution_Attribute_name: Property = Property(name="name", type=StringType)
solution_Attribute_dataType: Property = Property(name="dataType", type=StringType)
solution_Attribute.attributes={solution_Attribute_name, solution_Attribute_dataType}

# solution_Relationship class attributes and methods
solution_Relationship_roleName: Property = Property(name="roleName", type=StringType)
solution_Relationship_lowerBound: Property = Property(name="lowerBound", type=IntegerType)
solution_Relationship_upperBound: Property = Property(name="upperBound", type=IntegerType)
solution_Relationship.attributes={solution_Relationship_lowerBound, solution_Relationship_roleName, solution_Relationship_upperBound}

# solution_Link class attributes and methods
solution_Link_name: Property = Property(name="name", type=StringType)
solution_Link.attributes={solution_Link_name}

# solution_NonContextualLink class attributes and methods

# WebPage class attributes and methods

# solution_DynamicPage class attributes and methods

# solution_EntityPage class attributes and methods

# DynamicPage class attributes and methods

# solution_IndexPage class attributes and methods

# solution_CreatePage class attributes and methods

# EditablePage class attributes and methods

# solution_UpdatePage class attributes and methods

# solution_DeletePage class attributes and methods

# Link class attributes and methods

# solution_ContextualLink class attributes and methods

# solution_EditablePage class attributes and methods

# EntityPage class attributes and methods

# Relationships
entities0: BinaryAssociation = BinaryAssociation(
    name="entities0",
    ends={
        Property(name="solution_Entity", type=solution_WebApplication, multiplicity=Multiplicity(1, 1)),
        Property(name="solution_WebApplication", type=solution_Entity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
webpages1: BinaryAssociation = BinaryAssociation(
    name="webpages1",
    ends={
        Property(name="solution_WebPage", type=solution_WebApplication, multiplicity=Multiplicity(1, 1)),
        Property(name="solution_WebApplication2", type=solution_WebPage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
homePage3: BinaryAssociation = BinaryAssociation(
    name="homePage3",
    ends={
        Property(name="solution_StaticPage", type=solution_WebApplication, multiplicity=Multiplicity(1, 1)),
        Property(name="solution_WebApplication4", type=solution_StaticPage, multiplicity=Multiplicity(1, 1))
    }
)
attributes5: BinaryAssociation = BinaryAssociation(
    name="attributes5",
    ends={
        Property(name="solution_Attribute", type=solution_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="solution_Entity6", type=solution_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
id7: BinaryAssociation = BinaryAssociation(
    name="id7",
    ends={
        Property(name="solution_Attribute9", type=solution_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="solution_Entity8", type=solution_Attribute, multiplicity=Multiplicity(1, 1))
    }
)
relationships10: BinaryAssociation = BinaryAssociation(
    name="relationships10",
    ends={
        Property(name="Relationship", type=solution_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=solution_Relationship, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source11: BinaryAssociation = BinaryAssociation(
    name="source11",
    ends={
        Property(name="Entity", type=solution_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="relationships", type=solution_Entity, multiplicity=Multiplicity(1, 1))
    }
)
target12: BinaryAssociation = BinaryAssociation(
    name="target12",
    ends={
        Property(name="solution_Entity13", type=solution_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="solution_Relationship", type=solution_Entity, multiplicity=Multiplicity(1, 1))
    }
)
opposite15: BinaryAssociation = BinaryAssociation(
    name="opposite15",
    ends={
        Property(name="solution_Relationship16", type=solution_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="solution_Relationship14", type=solution_Relationship, multiplicity=Multiplicity(0, 1))
    }
)
links17: BinaryAssociation = BinaryAssociation(
    name="links17",
    ends={
        Property(name="solution_Link", type=solution_WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="solution_WebPage18", type=solution_Link, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
homeLink19: BinaryAssociation = BinaryAssociation(
    name="homeLink19",
    ends={
        Property(name="solution_NonContextualLink", type=solution_WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="solution_WebPage20", type=solution_NonContextualLink, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
entity21: BinaryAssociation = BinaryAssociation(
    name="entity21",
    ends={
        Property(name="solution_Entity22", type=solution_DynamicPage, multiplicity=Multiplicity(1, 1)),
        Property(name="solution_DynamicPage", type=solution_Entity, multiplicity=Multiplicity(1, 1))
    }
)
innerPages23: BinaryAssociation = BinaryAssociation(
    name="innerPages23",
    ends={
        Property(name="solution_DynamicPage24", type=solution_EntityPage, multiplicity=Multiplicity(1, 1)),
        Property(name="solution_EntityPage", type=solution_DynamicPage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target25: BinaryAssociation = BinaryAssociation(
    name="target25",
    ends={
        Property(name="solution_WebPage27", type=solution_Link, multiplicity=Multiplicity(1, 1)),
        Property(name="solution_Link26", type=solution_WebPage, multiplicity=Multiplicity(1, 1))
    }
)
information28: BinaryAssociation = BinaryAssociation(
    name="information28",
    ends={
        Property(name="solution_Entity29", type=solution_ContextualLink, multiplicity=Multiplicity(1, 1)),
        Property(name="solution_ContextualLink", type=solution_Entity, multiplicity=Multiplicity(1, 1))
    }
)
returnPage30: BinaryAssociation = BinaryAssociation(
    name="returnPage30",
    ends={
        Property(name="solution_EntityPage31", type=solution_EditablePage, multiplicity=Multiplicity(1, 1)),
        Property(name="solution_EditablePage", type=solution_EntityPage, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_solution_StaticPage_WebPage = Generalization(general=WebPage, specific=solution_StaticPage)
gen_solution_DynamicPage_WebPage = Generalization(general=WebPage, specific=solution_DynamicPage)
gen_solution_EntityPage_DynamicPage = Generalization(general=DynamicPage, specific=solution_EntityPage)
gen_solution_IndexPage_DynamicPage = Generalization(general=DynamicPage, specific=solution_IndexPage)
gen_solution_CreatePage_EditablePage = Generalization(general=EditablePage, specific=solution_CreatePage)
gen_solution_UpdatePage_EditablePage = Generalization(general=EditablePage, specific=solution_UpdatePage)
gen_solution_DeletePage_EditablePage = Generalization(general=EditablePage, specific=solution_DeletePage)
gen_solution_NonContextualLink_Link = Generalization(general=Link, specific=solution_NonContextualLink)
gen_solution_ContextualLink_Link = Generalization(general=Link, specific=solution_ContextualLink)
gen_solution_EditablePage_EntityPage = Generalization(general=EntityPage, specific=solution_EditablePage)

# Domain Model
domain_model = DomainModel(
    name="solution",
    types={solution_WebApplication, solution_Entity, solution_WebPage, solution_StaticPage, solution_Attribute, solution_Relationship, solution_Link, solution_NonContextualLink, WebPage, solution_DynamicPage, solution_EntityPage, DynamicPage, solution_IndexPage, solution_CreatePage, EditablePage, solution_UpdatePage, solution_DeletePage, Link, solution_ContextualLink, solution_EditablePage, EntityPage, DataType},
    associations={entities0, webpages1, homePage3, attributes5, id7, relationships10, source11, target12, opposite15, links17, homeLink19, entity21, innerPages23, target25, information28, returnPage30},
    generalizations={gen_solution_StaticPage_WebPage, gen_solution_DynamicPage_WebPage, gen_solution_EntityPage_DynamicPage, gen_solution_IndexPage_DynamicPage, gen_solution_CreatePage_EditablePage, gen_solution_UpdatePage_EditablePage, gen_solution_DeletePage_EditablePage, gen_solution_NonContextualLink_Link, gen_solution_ContextualLink_Link, gen_solution_EditablePage_EntityPage},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)