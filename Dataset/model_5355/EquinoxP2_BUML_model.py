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
p2_Copyright = Class(name="p2::Copyright")
p2_Description = Class(name="p2::Description")
p2_DiscoverySite = Class(name="p2::DiscoverySite")
p2_License = Class(name="p2::License")
p2_Vendor = Class(name="p2::Vendor")
p2_Feature = Class(name="p2::Feature")
Tool = Class(name="Tool")
p2_Plugin = Class(name="p2::Plugin")
FeatureMetadata = Class(name="FeatureMetadata")
Bundle = Class(name="Bundle")
p2_FeatureMetadata = Class(name="p2::FeatureMetadata", is_abstract=True)
LocatedElement = Class(name="LocatedElement")

# p2_Copyright class attributes and methods

# p2_Description class attributes and methods

# p2_DiscoverySite class attributes and methods

# p2_License class attributes and methods

# p2_Vendor class attributes and methods

# p2_Feature class attributes and methods
p2_Feature_application: Property = Property(name="application", type=StringType)
p2_Feature.attributes={p2_Feature_application}

# Tool class attributes and methods

# p2_Plugin class attributes and methods

# FeatureMetadata class attributes and methods

# Bundle class attributes and methods

# p2_FeatureMetadata class attributes and methods
p2_FeatureMetadata_name: Property = Property(name="name", type=StringType)
p2_FeatureMetadata_text: Property = Property(name="text", type=StringType)
p2_FeatureMetadata.attributes={p2_FeatureMetadata_name, p2_FeatureMetadata_text}

# LocatedElement class attributes and methods

# Relationships
copyright0: BinaryAssociation = BinaryAssociation(
    name="copyright0",
    ends={
        Property(name="p2_Copyright", type=p2_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="p2_Feature", type=p2_Copyright, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
description1: BinaryAssociation = BinaryAssociation(
    name="description1",
    ends={
        Property(name="p2_Description", type=p2_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="p2_Feature2", type=p2_Description, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sites3: BinaryAssociation = BinaryAssociation(
    name="sites3",
    ends={
        Property(name="p2_DiscoverySite", type=p2_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="p2_Feature4", type=p2_DiscoverySite, multiplicity=Multiplicity(0, 9999))
    }
)
license5: BinaryAssociation = BinaryAssociation(
    name="license5",
    ends={
        Property(name="p2_License", type=p2_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="p2_Feature6", type=p2_License, multiplicity=Multiplicity(0, 1))
    }
)
provider7: BinaryAssociation = BinaryAssociation(
    name="provider7",
    ends={
        Property(name="p2_Vendor", type=p2_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="p2_Feature8", type=p2_Vendor, multiplicity=Multiplicity(0, 1))
    }
)
plugins9: BinaryAssociation = BinaryAssociation(
    name="plugins9",
    ends={
        Property(name="p2_Plugin", type=p2_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="p2_Feature10", type=p2_Plugin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_p2_Feature_Tool = Generalization(general=Tool, specific=p2_Feature)
gen_p2_Copyright_FeatureMetadata = Generalization(general=FeatureMetadata, specific=p2_Copyright)
gen_p2_Description_FeatureMetadata = Generalization(general=FeatureMetadata, specific=p2_Description)
gen_p2_DiscoverySite_FeatureMetadata = Generalization(general=FeatureMetadata, specific=p2_DiscoverySite)
gen_p2_License_FeatureMetadata = Generalization(general=FeatureMetadata, specific=p2_License)
gen_p2_Plugin_Bundle = Generalization(general=Bundle, specific=p2_Plugin)
gen_p2_FeatureMetadata_LocatedElement = Generalization(general=LocatedElement, specific=p2_FeatureMetadata)

# Domain Model
domain_model = DomainModel(
    name="p2",
    types={p2_Copyright, p2_Description, p2_DiscoverySite, p2_License, p2_Vendor, p2_Feature, Tool, p2_Plugin, FeatureMetadata, Bundle, p2_FeatureMetadata, LocatedElement},
    associations={copyright0, description1, sites3, license5, provider7, plugins9},
    generalizations={gen_p2_Feature_Tool, gen_p2_Copyright_FeatureMetadata, gen_p2_Description_FeatureMetadata, gen_p2_DiscoverySite_FeatureMetadata, gen_p2_License_FeatureMetadata, gen_p2_Plugin_Bundle, gen_p2_FeatureMetadata_LocatedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)