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
PrimitiveType: Enumeration = Enumeration(
    name="PrimitiveType",
    literals={
            EnumerationLiteral(name="String"),
			EnumerationLiteral(name="Short"),
			EnumerationLiteral(name="Integer"),
			EnumerationLiteral(name="Long"),
			EnumerationLiteral(name="Float"),
			EnumerationLiteral(name="Double"),
			EnumerationLiteral(name="Boolean"),
			EnumerationLiteral(name="Byte"),
			EnumerationLiteral(name="Date"),
			EnumerationLiteral(name="Datetime"),
			EnumerationLiteral(name="Timestamp"),
			EnumerationLiteral(name="Decimal")
    }
)

# Classes
soa_Architecture = Class(name="soa::Architecture")
soa_Module = Class(name="soa::Module")
soa_Import = Class(name="soa::Import")
soa_Model = Class(name="soa::Model")
soa_Entities = Class(name="soa::Entities")
soa_Comment = Class(name="soa::Comment")
soa_Enum = Class(name="soa::Enum")
Entities = Class(name="Entities")
soa_Entity = Class(name="soa::Entity")
soa_Feature = Class(name="soa::Feature")
soa_Exceptions = Class(name="soa::Exceptions")
soa_Service = Class(name="soa::Service")
soa_PrimitiveFeature = Class(name="soa::PrimitiveFeature")
soa_GenericListFeature = Class(name="soa::GenericListFeature")
soa_Exception = Class(name="soa::Exception")
soa_FeatureType = Class(name="soa::FeatureType")
soa_EntitiesFeature = Class(name="soa::EntitiesFeature")
FeatureType = Class(name="FeatureType")
soa_Operation = Class(name="soa::Operation")

# soa_Architecture class attributes and methods
soa_Architecture_name: Property = Property(name="name", type=StringType)
soa_Architecture.attributes={soa_Architecture_name}

# soa_Module class attributes and methods
soa_Module_name: Property = Property(name="name", type=StringType)
soa_Module_version: Property = Property(name="version", type=StringType)
soa_Module_event: Property = Property(name="event", type=StringType)
soa_Module.attributes={soa_Module_name, soa_Module_version, soa_Module_event}

# soa_Import class attributes and methods
soa_Import_importedNamespace: Property = Property(name="importedNamespace", type=StringType)
soa_Import.attributes={soa_Import_importedNamespace}

# soa_Model class attributes and methods

# soa_Entities class attributes and methods
soa_Entities_name: Property = Property(name="name", type=StringType)
soa_Entities.attributes={soa_Entities_name}

# soa_Comment class attributes and methods
soa_Comment_value: Property = Property(name="value", type=StringType)
soa_Comment.attributes={soa_Comment_value}

# soa_Enum class attributes and methods
soa_Enum_features: Property = Property(name="features", type=StringType)
soa_Enum.attributes={soa_Enum_features}

# Entities class attributes and methods

# soa_Entity class attributes and methods

# soa_Feature class attributes and methods
soa_Feature_name: Property = Property(name="name", type=StringType)
soa_Feature.attributes={soa_Feature_name}

# soa_Exceptions class attributes and methods

# soa_Service class attributes and methods
soa_Service_name: Property = Property(name="name", type=StringType)
soa_Service.attributes={soa_Service_name}

# soa_PrimitiveFeature class attributes and methods
soa_PrimitiveFeature_type: Property = Property(name="type", type=StringType)
soa_PrimitiveFeature.attributes={soa_PrimitiveFeature_type}

# soa_GenericListFeature class attributes and methods

# soa_Exception class attributes and methods
soa_Exception_name: Property = Property(name="name", type=StringType)
soa_Exception_msg: Property = Property(name="msg", type=StringType)
soa_Exception.attributes={soa_Exception_name, soa_Exception_msg}

# soa_FeatureType class attributes and methods

# soa_EntitiesFeature class attributes and methods

# FeatureType class attributes and methods

# soa_Operation class attributes and methods
soa_Operation_name: Property = Property(name="name", type=StringType)
soa_Operation.attributes={soa_Operation_name}

# Relationships
module0: BinaryAssociation = BinaryAssociation(
    name="module0",
    ends={
        Property(name="soa_Module", type=soa_Architecture, multiplicity=Multiplicity(1, 1)),
        Property(name="soa_Architecture", type=soa_Module, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
imports1: BinaryAssociation = BinaryAssociation(
    name="imports1",
    ends={
        Property(name="soa_Import", type=soa_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="soa_Module2", type=soa_Import, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
model3: BinaryAssociation = BinaryAssociation(
    name="model3",
    ends={
        Property(name="soa_Model", type=soa_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="soa_Module4", type=soa_Model, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entities9: BinaryAssociation = BinaryAssociation(
    name="entities9",
    ends={
        Property(name="soa_Entities", type=soa_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="soa_Model10", type=soa_Entities, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
features11: BinaryAssociation = BinaryAssociation(
    name="features11",
    ends={
        Property(name="soa_Feature", type=soa_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="soa_Entity", type=soa_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
featureComment12: BinaryAssociation = BinaryAssociation(
    name="featureComment12",
    ends={
        Property(name="soa_Comment", type=soa_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="soa_Feature13", type=soa_Comment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exceptions5: BinaryAssociation = BinaryAssociation(
    name="exceptions5",
    ends={
        Property(name="soa_Exceptions", type=soa_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="soa_Module6", type=soa_Exceptions, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
services7: BinaryAssociation = BinaryAssociation(
    name="services7",
    ends={
        Property(name="soa_Service", type=soa_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="soa_Module8", type=soa_Service, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type18: BinaryAssociation = BinaryAssociation(
    name="type18",
    ends={
        Property(name="soa_FeatureType19", type=soa_GenericListFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="soa_GenericListFeature", type=soa_FeatureType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exceptions20: BinaryAssociation = BinaryAssociation(
    name="exceptions20",
    ends={
        Property(name="soa_Exception", type=soa_Exceptions, multiplicity=Multiplicity(1, 1)),
        Property(name="soa_Exceptions21", type=soa_Exception, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type14: BinaryAssociation = BinaryAssociation(
    name="type14",
    ends={
        Property(name="soa_FeatureType", type=soa_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="soa_Feature15", type=soa_FeatureType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type16: BinaryAssociation = BinaryAssociation(
    name="type16",
    ends={
        Property(name="soa_Entities17", type=soa_EntitiesFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="soa_EntitiesFeature", type=soa_Entities, multiplicity=Multiplicity(0, 1))
    }
)
operations22: BinaryAssociation = BinaryAssociation(
    name="operations22",
    ends={
        Property(name="soa_Operation", type=soa_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="soa_Service23", type=soa_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
featuresInput24: BinaryAssociation = BinaryAssociation(
    name="featuresInput24",
    ends={
        Property(name="soa_Feature26", type=soa_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="soa_Operation25", type=soa_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
featuresOutput27: BinaryAssociation = BinaryAssociation(
    name="featuresOutput27",
    ends={
        Property(name="soa_Feature29", type=soa_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="soa_Operation28", type=soa_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exceptionts30: BinaryAssociation = BinaryAssociation(
    name="exceptionts30",
    ends={
        Property(name="soa_Exception32", type=soa_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="soa_Operation31", type=soa_Exception, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_soa_Enum_Entities = Generalization(general=Entities, specific=soa_Enum)
gen_soa_Entity_Entities = Generalization(general=Entities, specific=soa_Entity)
gen_soa_PrimitiveFeature_FeatureType = Generalization(general=FeatureType, specific=soa_PrimitiveFeature)
gen_soa_GenericListFeature_FeatureType = Generalization(general=FeatureType, specific=soa_GenericListFeature)
gen_soa_EntitiesFeature_FeatureType = Generalization(general=FeatureType, specific=soa_EntitiesFeature)

# Domain Model
domain_model = DomainModel(
    name="soa",
    types={soa_Architecture, soa_Module, soa_Import, soa_Model, soa_Entities, soa_Comment, soa_Enum, Entities, soa_Entity, soa_Feature, soa_Exceptions, soa_Service, soa_PrimitiveFeature, soa_GenericListFeature, soa_Exception, soa_FeatureType, soa_EntitiesFeature, FeatureType, soa_Operation, PrimitiveType},
    associations={module0, imports1, model3, entities9, features11, featureComment12, exceptions5, services7, type18, exceptions20, type14, type16, operations22, featuresInput24, featuresOutput27, exceptionts30},
    generalizations={gen_soa_Enum_Entities, gen_soa_Entity_Entities, gen_soa_PrimitiveFeature_FeatureType, gen_soa_GenericListFeature_FeatureType, gen_soa_EntitiesFeature_FeatureType},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)