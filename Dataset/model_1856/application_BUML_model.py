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
application_ApplicationGroup = Class(name="application::ApplicationGroup")
application_Application = Class(name="application::Application")
application_ApplicationRecipes = Class(name="application::ApplicationRecipes")
application_ApplicationMappers = Class(name="application::ApplicationMappers")
application_ApplicationUILayer = Class(name="application::ApplicationUILayer")
application_ApplicationInfrastructureLayers = Class(name="application::ApplicationInfrastructureLayers")
application_ApplicationStyleLibraries = Class(name="application::ApplicationStyleLibraries")
application_ApplicationRealms = Class(name="application::ApplicationRealms")
application_ApplicationMessageLibraries = Class(name="application::ApplicationMessageLibraries")
application_Language = Class(name="application::Language")
application_ApplicationInfrastructureLayer = Class(name="application::ApplicationInfrastructureLayer")
application_EnterpriseInfrastructure = Class(name="application::EnterpriseInfrastructure")
application_ApplicationMessageLibrary = Class(name="application::ApplicationMessageLibrary")
application_ApplicationLanguages = Class(name="application::ApplicationLanguages")
application_ApplicationStyle = Class(name="application::ApplicationStyle")
application_MessageLibrary = Class(name="application::MessageLibrary")
application_ApplicationRealm = Class(name="application::ApplicationRealm")
application_Roles = Class(name="application::Roles")
application_StyleLibrary = Class(name="application::StyleLibrary")
application_ApplicationUIPackage = Class(name="application::ApplicationUIPackage")
application_Form = Class(name="application::Form")
application_ApplicationRecipe = Class(name="application::ApplicationRecipe")
application_Recipes = Class(name="application::Recipes")
application_ApplicationMapper = Class(name="application::ApplicationMapper")
application_MappingLayer = Class(name="application::MappingLayer")
application_Mappers = Class(name="application::Mappers")

# application_ApplicationGroup class attributes and methods
application_ApplicationGroup_uid: Property = Property(name="uid", type=StringType)
application_ApplicationGroup_name: Property = Property(name="name", type=StringType)
application_ApplicationGroup.attributes={application_ApplicationGroup_uid, application_ApplicationGroup_name}

# application_Application class attributes and methods
application_Application_uid: Property = Property(name="uid", type=StringType)
application_Application_name: Property = Property(name="name", type=StringType)
application_Application.attributes={application_Application_uid, application_Application_name}

# application_ApplicationRecipes class attributes and methods
application_ApplicationRecipes_name: Property = Property(name="name", type=StringType)
application_ApplicationRecipes_uid: Property = Property(name="uid", type=StringType)
application_ApplicationRecipes.attributes={application_ApplicationRecipes_uid, application_ApplicationRecipes_name}

# application_ApplicationMappers class attributes and methods
application_ApplicationMappers_uid: Property = Property(name="uid", type=StringType)
application_ApplicationMappers_name: Property = Property(name="name", type=StringType)
application_ApplicationMappers.attributes={application_ApplicationMappers_uid, application_ApplicationMappers_name}

# application_ApplicationUILayer class attributes and methods
application_ApplicationUILayer_uid: Property = Property(name="uid", type=StringType)
application_ApplicationUILayer_name: Property = Property(name="name", type=StringType)
application_ApplicationUILayer.attributes={application_ApplicationUILayer_uid, application_ApplicationUILayer_name}

# application_ApplicationInfrastructureLayers class attributes and methods
application_ApplicationInfrastructureLayers_uid: Property = Property(name="uid", type=StringType)
application_ApplicationInfrastructureLayers_name: Property = Property(name="name", type=StringType)
application_ApplicationInfrastructureLayers.attributes={application_ApplicationInfrastructureLayers_name, application_ApplicationInfrastructureLayers_uid}

# application_ApplicationStyleLibraries class attributes and methods
application_ApplicationStyleLibraries_uid: Property = Property(name="uid", type=StringType)
application_ApplicationStyleLibraries_name: Property = Property(name="name", type=StringType)
application_ApplicationStyleLibraries.attributes={application_ApplicationStyleLibraries_uid, application_ApplicationStyleLibraries_name}

# application_ApplicationRealms class attributes and methods
application_ApplicationRealms_uid: Property = Property(name="uid", type=StringType)
application_ApplicationRealms_name: Property = Property(name="name", type=StringType)
application_ApplicationRealms.attributes={application_ApplicationRealms_uid, application_ApplicationRealms_name}

# application_ApplicationMessageLibraries class attributes and methods
application_ApplicationMessageLibraries_uid: Property = Property(name="uid", type=StringType)
application_ApplicationMessageLibraries_name: Property = Property(name="name", type=StringType)
application_ApplicationMessageLibraries.attributes={application_ApplicationMessageLibraries_uid, application_ApplicationMessageLibraries_name}

# application_Language class attributes and methods

# application_ApplicationInfrastructureLayer class attributes and methods
application_ApplicationInfrastructureLayer_uid: Property = Property(name="uid", type=StringType)
application_ApplicationInfrastructureLayer_name: Property = Property(name="name", type=StringType)
application_ApplicationInfrastructureLayer.attributes={application_ApplicationInfrastructureLayer_uid, application_ApplicationInfrastructureLayer_name}

# application_EnterpriseInfrastructure class attributes and methods

# application_ApplicationMessageLibrary class attributes and methods
application_ApplicationMessageLibrary_uid: Property = Property(name="uid", type=StringType)
application_ApplicationMessageLibrary_name: Property = Property(name="name", type=StringType)
application_ApplicationMessageLibrary.attributes={application_ApplicationMessageLibrary_name, application_ApplicationMessageLibrary_uid}

# application_ApplicationLanguages class attributes and methods
application_ApplicationLanguages_uid: Property = Property(name="uid", type=StringType)
application_ApplicationLanguages_name: Property = Property(name="name", type=StringType)
application_ApplicationLanguages.attributes={application_ApplicationLanguages_uid, application_ApplicationLanguages_name}

# application_ApplicationStyle class attributes and methods
application_ApplicationStyle_uid: Property = Property(name="uid", type=StringType)
application_ApplicationStyle_name: Property = Property(name="name", type=StringType)
application_ApplicationStyle.attributes={application_ApplicationStyle_name, application_ApplicationStyle_uid}

# application_MessageLibrary class attributes and methods

# application_ApplicationRealm class attributes and methods
application_ApplicationRealm_uid: Property = Property(name="uid", type=StringType)
application_ApplicationRealm_name: Property = Property(name="name", type=StringType)
application_ApplicationRealm.attributes={application_ApplicationRealm_uid, application_ApplicationRealm_name}

# application_Roles class attributes and methods

# application_StyleLibrary class attributes and methods

# application_ApplicationUIPackage class attributes and methods
application_ApplicationUIPackage_uid: Property = Property(name="uid", type=StringType)
application_ApplicationUIPackage_name: Property = Property(name="name", type=StringType)
application_ApplicationUIPackage.attributes={application_ApplicationUIPackage_name, application_ApplicationUIPackage_uid}

# application_Form class attributes and methods

# application_ApplicationRecipe class attributes and methods
application_ApplicationRecipe_uid: Property = Property(name="uid", type=StringType)
application_ApplicationRecipe_name: Property = Property(name="name", type=StringType)
application_ApplicationRecipe.attributes={application_ApplicationRecipe_uid, application_ApplicationRecipe_name}

# application_Recipes class attributes and methods

# application_ApplicationMapper class attributes and methods
application_ApplicationMapper_uid: Property = Property(name="uid", type=StringType)
application_ApplicationMapper_name: Property = Property(name="name", type=StringType)
application_ApplicationMapper.attributes={application_ApplicationMapper_name, application_ApplicationMapper_uid}

# application_MappingLayer class attributes and methods

# application_Mappers class attributes and methods

# Relationships
applications0: BinaryAssociation = BinaryAssociation(
    name="applications0",
    ends={
        Property(name="application_Application", type=application_ApplicationGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="application_ApplicationGroup", type=application_Application, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
applicationRecipes1: BinaryAssociation = BinaryAssociation(
    name="applicationRecipes1",
    ends={
        Property(name="application_ApplicationRecipes", type=application_Application, multiplicity=Multiplicity(1, 1)),
        Property(name="application_Application2", type=application_ApplicationRecipes, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
applicationMappers3: BinaryAssociation = BinaryAssociation(
    name="applicationMappers3",
    ends={
        Property(name="application_ApplicationMappers", type=application_Application, multiplicity=Multiplicity(1, 1)),
        Property(name="application_Application4", type=application_ApplicationMappers, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
applicationUILayer5: BinaryAssociation = BinaryAssociation(
    name="applicationUILayer5",
    ends={
        Property(name="application_ApplicationUILayer", type=application_Application, multiplicity=Multiplicity(1, 1)),
        Property(name="application_Application6", type=application_ApplicationUILayer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
applicationInfrastructureLayer7: BinaryAssociation = BinaryAssociation(
    name="applicationInfrastructureLayer7",
    ends={
        Property(name="application_ApplicationInfrastructureLayers", type=application_Application, multiplicity=Multiplicity(1, 1)),
        Property(name="application_Application8", type=application_ApplicationInfrastructureLayers, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
applicationStyle9: BinaryAssociation = BinaryAssociation(
    name="applicationStyle9",
    ends={
        Property(name="application_ApplicationStyleLibraries", type=application_Application, multiplicity=Multiplicity(1, 1)),
        Property(name="application_Application10", type=application_ApplicationStyleLibraries, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
applicationRole11: BinaryAssociation = BinaryAssociation(
    name="applicationRole11",
    ends={
        Property(name="application_ApplicationRealms", type=application_Application, multiplicity=Multiplicity(1, 1)),
        Property(name="application_Application12", type=application_ApplicationRealms, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
applicationMessages13: BinaryAssociation = BinaryAssociation(
    name="applicationMessages13",
    ends={
        Property(name="application_ApplicationMessageLibraries", type=application_Application, multiplicity=Multiplicity(1, 1)),
        Property(name="application_Application14", type=application_ApplicationMessageLibraries, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
infarastructureLayers15: BinaryAssociation = BinaryAssociation(
    name="infarastructureLayers15",
    ends={
        Property(name="application_ApplicationInfrastructureLayer", type=application_ApplicationInfrastructureLayers, multiplicity=Multiplicity(1, 1)),
        Property(name="application_ApplicationInfrastructureLayers16", type=application_ApplicationInfrastructureLayer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
infarastructures17: BinaryAssociation = BinaryAssociation(
    name="infarastructures17",
    ends={
        Property(name="application_EnterpriseInfrastructure", type=application_ApplicationInfrastructureLayer, multiplicity=Multiplicity(1, 1)),
        Property(name="application_ApplicationInfrastructureLayer18", type=application_EnterpriseInfrastructure, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
messageLibraries19: BinaryAssociation = BinaryAssociation(
    name="messageLibraries19",
    ends={
        Property(name="application_ApplicationMessageLibrary", type=application_ApplicationMessageLibraries, multiplicity=Multiplicity(1, 1)),
        Property(name="application_ApplicationMessageLibraries20", type=application_ApplicationMessageLibrary, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
applicationLanguages21: BinaryAssociation = BinaryAssociation(
    name="applicationLanguages21",
    ends={
        Property(name="application_ApplicationLanguages", type=application_ApplicationMessageLibraries, multiplicity=Multiplicity(1, 1)),
        Property(name="application_ApplicationMessageLibraries22", type=application_ApplicationLanguages, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
languages23: BinaryAssociation = BinaryAssociation(
    name="languages23",
    ends={
        Property(name="application_Language", type=application_ApplicationLanguages, multiplicity=Multiplicity(1, 1)),
        Property(name="application_ApplicationLanguages24", type=application_Language, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
libraries25: BinaryAssociation = BinaryAssociation(
    name="libraries25",
    ends={
        Property(name="application_MessageLibrary", type=application_ApplicationMessageLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="application_ApplicationMessageLibrary26", type=application_MessageLibrary, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
realms27: BinaryAssociation = BinaryAssociation(
    name="realms27",
    ends={
        Property(name="application_ApplicationRealm", type=application_ApplicationRealms, multiplicity=Multiplicity(1, 1)),
        Property(name="application_ApplicationRealms28", type=application_ApplicationRealm, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
roles29: BinaryAssociation = BinaryAssociation(
    name="roles29",
    ends={
        Property(name="application_Roles", type=application_ApplicationRealm, multiplicity=Multiplicity(1, 1)),
        Property(name="application_ApplicationRealm30", type=application_Roles, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
styleLibraries31: BinaryAssociation = BinaryAssociation(
    name="styleLibraries31",
    ends={
        Property(name="application_ApplicationStyle", type=application_ApplicationStyleLibraries, multiplicity=Multiplicity(1, 1)),
        Property(name="application_ApplicationStyleLibraries32", type=application_ApplicationStyle, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
libraries33: BinaryAssociation = BinaryAssociation(
    name="libraries33",
    ends={
        Property(name="application_StyleLibrary", type=application_ApplicationStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="application_ApplicationStyle34", type=application_StyleLibrary, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
applicationUIPackages35: BinaryAssociation = BinaryAssociation(
    name="applicationUIPackages35",
    ends={
        Property(name="application_ApplicationUIPackage", type=application_ApplicationUILayer, multiplicity=Multiplicity(1, 1)),
        Property(name="application_ApplicationUILayer36", type=application_ApplicationUIPackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
forms37: BinaryAssociation = BinaryAssociation(
    name="forms37",
    ends={
        Property(name="application_Form", type=application_ApplicationUIPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="application_ApplicationUIPackage38", type=application_Form, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
recipes39: BinaryAssociation = BinaryAssociation(
    name="recipes39",
    ends={
        Property(name="application_ApplicationRecipe", type=application_ApplicationRecipes, multiplicity=Multiplicity(1, 1)),
        Property(name="application_ApplicationRecipes40", type=application_ApplicationRecipe, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
recipes41: BinaryAssociation = BinaryAssociation(
    name="recipes41",
    ends={
        Property(name="application_Recipes", type=application_ApplicationRecipe, multiplicity=Multiplicity(1, 1)),
        Property(name="application_ApplicationRecipe42", type=application_Recipes, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mappers43: BinaryAssociation = BinaryAssociation(
    name="mappers43",
    ends={
        Property(name="application_ApplicationMapper", type=application_ApplicationMappers, multiplicity=Multiplicity(1, 1)),
        Property(name="application_ApplicationMappers44", type=application_ApplicationMapper, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
appLayers45: BinaryAssociation = BinaryAssociation(
    name="appLayers45",
    ends={
        Property(name="application_MappingLayer", type=application_ApplicationMappers, multiplicity=Multiplicity(1, 1)),
        Property(name="application_ApplicationMappers46", type=application_MappingLayer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mapper47: BinaryAssociation = BinaryAssociation(
    name="mapper47",
    ends={
        Property(name="application_Mappers", type=application_ApplicationMapper, multiplicity=Multiplicity(1, 1)),
        Property(name="application_ApplicationMapper48", type=application_Mappers, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="application",
    types={application_ApplicationGroup, application_Application, application_ApplicationRecipes, application_ApplicationMappers, application_ApplicationUILayer, application_ApplicationInfrastructureLayers, application_ApplicationStyleLibraries, application_ApplicationRealms, application_ApplicationMessageLibraries, application_Language, application_ApplicationInfrastructureLayer, application_EnterpriseInfrastructure, application_ApplicationMessageLibrary, application_ApplicationLanguages, application_ApplicationStyle, application_MessageLibrary, application_ApplicationRealm, application_Roles, application_StyleLibrary, application_ApplicationUIPackage, application_Form, application_ApplicationRecipe, application_Recipes, application_ApplicationMapper, application_MappingLayer, application_Mappers},
    associations={applications0, applicationRecipes1, applicationMappers3, applicationUILayer5, applicationInfrastructureLayer7, applicationStyle9, applicationRole11, applicationMessages13, infarastructureLayers15, infarastructures17, messageLibraries19, applicationLanguages21, languages23, libraries25, realms27, roles29, styleLibraries31, libraries33, applicationUIPackages35, forms37, recipes39, recipes41, mappers43, appLayers45, mapper47},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)