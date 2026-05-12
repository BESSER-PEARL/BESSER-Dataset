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
modulespecification_Module = Class(name="modulespecification_Module")

# modulespecification_Module class attributes and methods
modulespecification_Module_version: Property = Property(name="version", type=StringType)
modulespecification_Module_copyRightAuthorName: Property = Property(name="copyRightAuthorName", type=StringType)
modulespecification_Module_copyRightUrl: Property = Property(name="copyRightUrl", type=StringType)
modulespecification_Module_copyRightYear: Property = Property(name="copyRightYear", type=StringType)
modulespecification_Module_authorEmail: Property = Property(name="authorEmail", type=StringType)
modulespecification_Module_providerName: Property = Property(name="providerName", type=StringType)
modulespecification_Module_tychoVersion: Property = Property(name="tychoVersion", type=StringType)
modulespecification_Module_javaVersion: Property = Property(name="javaVersion", type=StringType)
modulespecification_Module_baseLocation: Property = Property(name="baseLocation", type=StringType)
modulespecification_Module_coreSuffix: Property = Property(name="coreSuffix", type=StringType)
modulespecification_Module_uiSuffix: Property = Property(name="uiSuffix", type=StringType)
modulespecification_Module_generateParent: Property = Property(name="generateParent", type=BooleanType)
modulespecification_Module_tychoParentName: Property = Property(name="tychoParentName", type=StringType)
modulespecification_Module_mavenGroupId: Property = Property(name="mavenGroupId", type=StringType)
modulespecification_Module_generateTests: Property = Property(name="generateTests", type=BooleanType)
modulespecification_Module_testsSuffix: Property = Property(name="testsSuffix", type=StringType)
modulespecification_Module_generateFeature: Property = Property(name="generateFeature", type=BooleanType)
modulespecification_Module_baseId: Property = Property(name="baseId", type=StringType)
modulespecification_Module_moduleName: Property = Property(name="moduleName", type=StringType)
modulespecification_Module_categoryName: Property = Property(name="categoryName", type=StringType)
modulespecification_Module_license: Property = Property(name="license", type=StringType)
modulespecification_Module_licenseUrl: Property = Property(name="licenseUrl", type=StringType)
modulespecification_Module_uie3Id: Property = Property(name="uie3Id", type=StringType)
modulespecification_Module_testsId: Property = Property(name="testsId", type=StringType)
modulespecification_Module_updateSiteId: Property = Property(name="updateSiteId", type=StringType)
modulespecification_Module_featureSuffix: Property = Property(name="featureSuffix", type=StringType)
modulespecification_Module_generateUpdatesite: Property = Property(name="generateUpdatesite", type=BooleanType)
modulespecification_Module_updateSiteSuffix: Property = Property(name="updateSiteSuffix", type=StringType)
modulespecification_Module_updateSiteUrl: Property = Property(name="updateSiteUrl", type=StringType)
modulespecification_Module_generateTarget: Property = Property(name="generateTarget", type=BooleanType)
modulespecification_Module_targetSuffix: Property = Property(name="targetSuffix", type=StringType)
modulespecification_Module_generateUiFragment: Property = Property(name="generateUiFragment", type=BooleanType)
modulespecification_Module_uie3Suffix: Property = Property(name="uie3Suffix", type=StringType)
modulespecification_Module_mavenVersionSuffix: Property = Property(name="mavenVersionSuffix", type=StringType)
modulespecification_Module_osgiVersionQualifier: Property = Property(name="osgiVersionQualifier", type=StringType)
modulespecification_Module_coreId: Property = Property(name="coreId", type=StringType)
modulespecification_Module_uiId: Property = Property(name="uiId", type=StringType)
modulespecification_Module_isLicenseEmpty: Property = Property(name="isLicenseEmpty", type=BooleanType)
modulespecification_Module_isLicenseUrlEmpty: Property = Property(name="isLicenseUrlEmpty", type=BooleanType)
modulespecification_Module_isUpdateSiteUrlEmpty: Property = Property(name="isUpdateSiteUrlEmpty", type=BooleanType)
modulespecification_Module_isAuthorEmailEmpty: Property = Property(name="isAuthorEmailEmpty", type=BooleanType)
modulespecification_Module_featureId: Property = Property(name="featureId", type=StringType)
modulespecification_Module_targetId: Property = Property(name="targetId", type=StringType)
modulespecification_Module_mavenVersion: Property = Property(name="mavenVersion", type=StringType)
modulespecification_Module_osgiVersion: Property = Property(name="osgiVersion", type=StringType)
modulespecification_Module_coreModuleName: Property = Property(name="coreModuleName", type=StringType)
modulespecification_Module_uiModuleName: Property = Property(name="uiModuleName", type=StringType)
modulespecification_Module.attributes={modulespecification_Module_copyRightYear, modulespecification_Module_targetId, modulespecification_Module_isUpdateSiteUrlEmpty, modulespecification_Module_generateParent, modulespecification_Module_mavenGroupId, modulespecification_Module_targetSuffix, modulespecification_Module_providerName, modulespecification_Module_tychoVersion, modulespecification_Module_isLicenseUrlEmpty, modulespecification_Module_coreSuffix, modulespecification_Module_copyRightUrl, modulespecification_Module_uie3Id, modulespecification_Module_testsId, modulespecification_Module_updateSiteSuffix, modulespecification_Module_testsSuffix, modulespecification_Module_categoryName, modulespecification_Module_generateTests, modulespecification_Module_coreModuleName, modulespecification_Module_moduleName, modulespecification_Module_license, modulespecification_Module_generateUpdatesite, modulespecification_Module_javaVersion, modulespecification_Module_featureSuffix, modulespecification_Module_updateSiteUrl, modulespecification_Module_generateTarget, modulespecification_Module_coreId, modulespecification_Module_mavenVersion, modulespecification_Module_isAuthorEmailEmpty, modulespecification_Module_generateFeature, modulespecification_Module_authorEmail, modulespecification_Module_featureId, modulespecification_Module_version, modulespecification_Module_baseLocation, modulespecification_Module_baseId, modulespecification_Module_generateUiFragment, modulespecification_Module_uiId, modulespecification_Module_copyRightAuthorName, modulespecification_Module_tychoParentName, modulespecification_Module_licenseUrl, modulespecification_Module_uiSuffix, modulespecification_Module_isLicenseEmpty, modulespecification_Module_uiModuleName, modulespecification_Module_updateSiteId, modulespecification_Module_osgiVersionQualifier, modulespecification_Module_uie3Suffix, modulespecification_Module_osgiVersion, modulespecification_Module_mavenVersionSuffix}

# Domain Model
domain_model = DomainModel(
    name="modulespecification",
    types={modulespecification_Module},
    associations={},
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