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
Datentyp: Enumeration = Enumeration(
    name="Datentyp",
    literals={
            EnumerationLiteral(name="Integer"),
			EnumerationLiteral(name="String"),
			EnumerationLiteral(name="Float"),
			EnumerationLiteral(name="Boolean"),
			EnumerationLiteral(name="Email"),
			EnumerationLiteral(name="Date"),
			EnumerationLiteral(name="Time")
    }
)

# Classes
swml_WebModel = Class(name="swml::WebModel")
swml_HypertextModel = Class(name="swml::HypertextModel")
swml_ContentModel = Class(name="swml::ContentModel")
swml_Enumeration = Class(name="swml::Enumeration")
swml_Entity = Class(name="swml::Entity")
swml_EnumTyp = Class(name="swml::EnumTyp")
swml_Attribute = Class(name="swml::Attribute")
swml_Reference = Class(name="swml::Reference")
swml_EntityPages = Class(name="swml::EntityPages")
swml_Literals = Class(name="swml::Literals")
swml_WebPage = Class(name="swml::WebPage", is_abstract=True)
swml_staticPage = Class(name="swml::staticPage")
swml_LinkKat2 = Class(name="swml::LinkKat2", is_abstract=True)
swml_LinkJoinNode = Class(name="swml::LinkJoinNode")
WebPage = Class(name="WebPage")
swml_LinkKat1 = Class(name="swml::LinkKat1", is_abstract=True)
swml_dynamicPage = Class(name="swml::dynamicPage", is_abstract=True)
dynamicPage = Class(name="dynamicPage")
swml_IndexPages = Class(name="swml::IndexPages")
swml_UpdatePage = Class(name="swml::UpdatePage")
EntityPages = Class(name="EntityPages")
swml_OK = Class(name="swml::OK")
swml_KO = Class(name="swml::KO")
swml_DeletePage = Class(name="swml::DeletePage")
swml_CreatePage = Class(name="swml::CreatePage")
swml_Links = Class(name="swml::Links", is_abstract=True)
swml_LinkParamater = Class(name="swml::LinkParamater")
swml_NonContextualLinks = Class(name="swml::NonContextualLinks")
LinkKat2 = Class(name="LinkKat2")
swml_ContextualLinks = Class(name="swml::ContextualLinks")
LinkKat1 = Class(name="LinkKat1")
Links = Class(name="Links")

# swml_WebModel class attributes and methods

# swml_HypertextModel class attributes and methods

# swml_ContentModel class attributes and methods

# swml_Enumeration class attributes and methods
swml_Enumeration_name: Property = Property(name="name", type=StringType)
swml_Enumeration.attributes={swml_Enumeration_name}

# swml_Entity class attributes and methods
swml_Entity_name: Property = Property(name="name", type=StringType)
swml_Entity.attributes={swml_Entity_name}

# swml_EnumTyp class attributes and methods
swml_EnumTyp_name: Property = Property(name="name", type=StringType)
swml_EnumTyp.attributes={swml_EnumTyp_name}

# swml_Attribute class attributes and methods
swml_Attribute_name: Property = Property(name="name", type=StringType)
swml_Attribute_Typ: Property = Property(name="Typ", type=StringType)
swml_Attribute.attributes={swml_Attribute_Typ, swml_Attribute_name}

# swml_Reference class attributes and methods
swml_Reference_rolename: Property = Property(name="rolename", type=StringType)
swml_Reference_lowerBound: Property = Property(name="lowerBound", type=IntegerType)
swml_Reference_upperBound: Property = Property(name="upperBound", type=IntegerType)
swml_Reference.attributes={swml_Reference_lowerBound, swml_Reference_upperBound, swml_Reference_rolename}

# swml_EntityPages class attributes and methods

# swml_Literals class attributes and methods
swml_Literals_name: Property = Property(name="name", type=StringType)
swml_Literals.attributes={swml_Literals_name}

# swml_WebPage class attributes and methods
swml_WebPage_name: Property = Property(name="name", type=StringType)
swml_WebPage.attributes={swml_WebPage_name}

# swml_staticPage class attributes and methods

# swml_LinkKat2 class attributes and methods

# swml_LinkJoinNode class attributes and methods

# WebPage class attributes and methods

# swml_LinkKat1 class attributes and methods

# swml_dynamicPage class attributes and methods

# dynamicPage class attributes and methods

# swml_IndexPages class attributes and methods

# swml_UpdatePage class attributes and methods

# EntityPages class attributes and methods

# swml_OK class attributes and methods

# swml_KO class attributes and methods

# swml_DeletePage class attributes and methods

# swml_CreatePage class attributes and methods

# swml_Links class attributes and methods
swml_Links_Name: Property = Property(name="Name", type=StringType)
swml_Links.attributes={swml_Links_Name}

# swml_LinkParamater class attributes and methods
swml_LinkParamater_Parameter: Property = Property(name="Parameter", type=StringType)
swml_LinkParamater.attributes={swml_LinkParamater_Parameter}

# swml_NonContextualLinks class attributes and methods

# LinkKat2 class attributes and methods

# swml_ContextualLinks class attributes and methods

# LinkKat1 class attributes and methods

# Links class attributes and methods

# Relationships
hypertextmodels0: BinaryAssociation = BinaryAssociation(
    name="hypertextmodels0",
    ends={
        Property(name="swml_HypertextModel", type=swml_WebModel, multiplicity=Multiplicity(1, 1)),
        Property(name="swml_WebModel", type=swml_HypertextModel, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
contentmodels1: BinaryAssociation = BinaryAssociation(
    name="contentmodels1",
    ends={
        Property(name="swml_ContentModel", type=swml_WebModel, multiplicity=Multiplicity(1, 1)),
        Property(name="swml_WebModel2", type=swml_ContentModel, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
Enumerations3: BinaryAssociation = BinaryAssociation(
    name="Enumerations3",
    ends={
        Property(name="swml_Enumeration", type=swml_ContentModel, multiplicity=Multiplicity(1, 1)),
        Property(name="swml_ContentModel4", type=swml_Enumeration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Entities5: BinaryAssociation = BinaryAssociation(
    name="Entities5",
    ends={
        Property(name="swml_Entity", type=swml_ContentModel, multiplicity=Multiplicity(1, 1)),
        Property(name="swml_ContentModel6", type=swml_Entity, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
EnumAttribute7: BinaryAssociation = BinaryAssociation(
    name="EnumAttribute7",
    ends={
        Property(name="swml_EnumTyp", type=swml_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="swml_Entity8", type=swml_EnumTyp, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Attributes9: BinaryAssociation = BinaryAssociation(
    name="Attributes9",
    ends={
        Property(name="swml_Attribute", type=swml_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="swml_Entity10", type=swml_Attribute, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
References11: BinaryAssociation = BinaryAssociation(
    name="References11",
    ends={
        Property(name="swml_Reference", type=swml_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="swml_Entity12", type=swml_Reference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Child14: BinaryAssociation = BinaryAssociation(
    name="Child14",
    ends={
        Property(name="swml_Entity15", type=swml_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="swml_Entity13", type=swml_Entity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Enums16: BinaryAssociation = BinaryAssociation(
    name="Enums16",
    ends={
        Property(name="swml_Enumeration18", type=swml_EnumTyp, multiplicity=Multiplicity(1, 1)),
        Property(name="swml_EnumTyp17", type=swml_Enumeration, multiplicity=Multiplicity(1, 1))
    }
)
Opposite20: BinaryAssociation = BinaryAssociation(
    name="Opposite20",
    ends={
        Property(name="swml_Reference21", type=swml_Reference, multiplicity=Multiplicity(1, 1)),
        Property(name="swml_Reference19", type=swml_Reference, multiplicity=Multiplicity(0, 1))
    }
)
RefTo22: BinaryAssociation = BinaryAssociation(
    name="RefTo22",
    ends={
        Property(name="swml_Entity24", type=swml_Reference, multiplicity=Multiplicity(1, 1)),
        Property(name="swml_Reference23", type=swml_Entity, multiplicity=Multiplicity(1, 1))
    }
)
ownedLiteral25: BinaryAssociation = BinaryAssociation(
    name="ownedLiteral25",
    ends={
        Property(name="swml_Literals", type=swml_Enumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="swml_Enumeration26", type=swml_Literals, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
WebPages27: BinaryAssociation = BinaryAssociation(
    name="WebPages27",
    ends={
        Property(name="swml_WebPage", type=swml_HypertextModel, multiplicity=Multiplicity(1, 1)),
        Property(name="swml_HypertextModel28", type=swml_WebPage, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
homepage29: BinaryAssociation = BinaryAssociation(
    name="homepage29",
    ends={
        Property(name="swml_staticPage", type=swml_HypertextModel, multiplicity=Multiplicity(1, 1)),
        Property(name="swml_HypertextModel30", type=swml_staticPage, multiplicity=Multiplicity(1, 1))
    }
)
Link31: BinaryAssociation = BinaryAssociation(
    name="Link31",
    ends={
        Property(name="swml_LinkKat2", type=swml_WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="swml_WebPage32", type=swml_LinkKat2, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Links33: BinaryAssociation = BinaryAssociation(
    name="Links33",
    ends={
        Property(name="swml_LinkKat1", type=swml_LinkJoinNode, multiplicity=Multiplicity(1, 1)),
        Property(name="swml_LinkJoinNode", type=swml_LinkKat1, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
EntityType34: BinaryAssociation = BinaryAssociation(
    name="EntityType34",
    ends={
        Property(name="swml_Entity35", type=swml_dynamicPage, multiplicity=Multiplicity(1, 1)),
        Property(name="swml_dynamicPage", type=swml_Entity, multiplicity=Multiplicity(1, 1))
    }
)
InnerPage36: BinaryAssociation = BinaryAssociation(
    name="InnerPage36",
    ends={
        Property(name="swml_dynamicPage37", type=swml_EntityPages, multiplicity=Multiplicity(1, 1)),
        Property(name="swml_EntityPages", type=swml_dynamicPage, multiplicity=Multiplicity(0, 9999))
    }
)
OKLink38: BinaryAssociation = BinaryAssociation(
    name="OKLink38",
    ends={
        Property(name="swml_OK", type=swml_UpdatePage, multiplicity=Multiplicity(1, 1)),
        Property(name="swml_UpdatePage", type=swml_OK, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
KOLink39: BinaryAssociation = BinaryAssociation(
    name="KOLink39",
    ends={
        Property(name="swml_KO", type=swml_UpdatePage, multiplicity=Multiplicity(1, 1)),
        Property(name="swml_UpdatePage40", type=swml_KO, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
OKLink41: BinaryAssociation = BinaryAssociation(
    name="OKLink41",
    ends={
        Property(name="swml_OK42", type=swml_DeletePage, multiplicity=Multiplicity(1, 1)),
        Property(name="swml_DeletePage", type=swml_OK, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
KOLink43: BinaryAssociation = BinaryAssociation(
    name="KOLink43",
    ends={
        Property(name="swml_KO45", type=swml_DeletePage, multiplicity=Multiplicity(1, 1)),
        Property(name="swml_DeletePage44", type=swml_KO, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
OKLink46: BinaryAssociation = BinaryAssociation(
    name="OKLink46",
    ends={
        Property(name="swml_OK47", type=swml_CreatePage, multiplicity=Multiplicity(1, 1)),
        Property(name="swml_CreatePage", type=swml_OK, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
KOLink48: BinaryAssociation = BinaryAssociation(
    name="KOLink48",
    ends={
        Property(name="swml_KO50", type=swml_CreatePage, multiplicity=Multiplicity(1, 1)),
        Property(name="swml_CreatePage49", type=swml_KO, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
Link51: BinaryAssociation = BinaryAssociation(
    name="Link51",
    ends={
        Property(name="swml_LinkParamater", type=swml_Links, multiplicity=Multiplicity(1, 1)),
        Property(name="swml_Links", type=swml_LinkParamater, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
TargetPage52: BinaryAssociation = BinaryAssociation(
    name="TargetPage52",
    ends={
        Property(name="swml_WebPage54", type=swml_Links, multiplicity=Multiplicity(1, 1)),
        Property(name="swml_Links53", type=swml_WebPage, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_swml_LinkJoinNode_WebPage = Generalization(general=WebPage, specific=swml_LinkJoinNode)
gen_swml_staticPage_WebPage = Generalization(general=WebPage, specific=swml_staticPage)
gen_swml_dynamicPage_WebPage = Generalization(general=WebPage, specific=swml_dynamicPage)
gen_swml_EntityPages_dynamicPage = Generalization(general=dynamicPage, specific=swml_EntityPages)
gen_swml_IndexPages_dynamicPage = Generalization(general=dynamicPage, specific=swml_IndexPages)
gen_swml_UpdatePage_EntityPages = Generalization(general=EntityPages, specific=swml_UpdatePage)
gen_swml_DeletePage_EntityPages = Generalization(general=EntityPages, specific=swml_DeletePage)
gen_swml_CreatePage_EntityPages = Generalization(general=EntityPages, specific=swml_CreatePage)
gen_swml_NonContextualLinks_LinkKat2 = Generalization(general=LinkKat2, specific=swml_NonContextualLinks)
gen_swml_ContextualLinks_LinkKat2 = Generalization(general=LinkKat2, specific=swml_ContextualLinks)
gen_swml_OK_LinkKat1 = Generalization(general=LinkKat1, specific=swml_OK)
gen_swml_KO_LinkKat1 = Generalization(general=LinkKat1, specific=swml_KO)
gen_swml_LinkKat1_Links = Generalization(general=Links, specific=swml_LinkKat1)
gen_swml_LinkKat2_Links = Generalization(general=Links, specific=swml_LinkKat2)

# Domain Model
domain_model = DomainModel(
    name="swml",
    types={swml_WebModel, swml_HypertextModel, swml_ContentModel, swml_Enumeration, swml_Entity, swml_EnumTyp, swml_Attribute, swml_Reference, swml_EntityPages, swml_Literals, swml_WebPage, swml_staticPage, swml_LinkKat2, swml_LinkJoinNode, WebPage, swml_LinkKat1, swml_dynamicPage, dynamicPage, swml_IndexPages, swml_UpdatePage, EntityPages, swml_OK, swml_KO, swml_DeletePage, swml_CreatePage, swml_Links, swml_LinkParamater, swml_NonContextualLinks, LinkKat2, swml_ContextualLinks, LinkKat1, Links, Datentyp},
    associations={hypertextmodels0, contentmodels1, Enumerations3, Entities5, EnumAttribute7, Attributes9, References11, Child14, Enums16, Opposite20, RefTo22, ownedLiteral25, WebPages27, homepage29, Link31, Links33, EntityType34, InnerPage36, OKLink38, KOLink39, OKLink41, KOLink43, OKLink46, KOLink48, Link51, TargetPage52},
    generalizations={gen_swml_LinkJoinNode_WebPage, gen_swml_staticPage_WebPage, gen_swml_dynamicPage_WebPage, gen_swml_EntityPages_dynamicPage, gen_swml_IndexPages_dynamicPage, gen_swml_UpdatePage_EntityPages, gen_swml_DeletePage_EntityPages, gen_swml_CreatePage_EntityPages, gen_swml_NonContextualLinks_LinkKat2, gen_swml_ContextualLinks_LinkKat2, gen_swml_OK_LinkKat1, gen_swml_KO_LinkKat1, gen_swml_LinkKat1_Links, gen_swml_LinkKat2_Links},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)