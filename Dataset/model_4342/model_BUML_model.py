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
migration_Repository = Class(name="migration::Repository")
migration_Model = Class(name="migration::Model")
migration_Metamodel = Class(name="migration::Metamodel")
migration_Type = Class(name="migration::Type")
migration_ModelResource = Class(name="migration::ModelResource")
AbstractResource = Class(name="AbstractResource")
migration_Instance = Class(name="migration::Instance")
migration_EClass = Class(name="migration::EClass")
migration_AttributeSlot = Class(name="migration::AttributeSlot")
Slot = Class(name="Slot")
migration_EAttribute = Class(name="migration::EAttribute")
migration_EReference = Class(name="migration::EReference")
migration_Slot = Class(name="migration::Slot", is_abstract=True)
migration_ReferenceSlot = Class(name="migration::ReferenceSlot")
migration_EPackage = Class(name="migration::EPackage")
migration_AbstractResource = Class(name="migration::AbstractResource", is_abstract=True)
migration_MetamodelResource = Class(name="migration::MetamodelResource")

# migration_Repository class attributes and methods

# migration_Model class attributes and methods
migration_Model_reflection: Property = Property(name="reflection", type=BooleanType)
migration_Model_m_getAllInstances: Method = Method(name="getAllInstances", parameters={Parameter(name='eClass')}, type=StringType)
migration_Model_m_getAllInstances: Method = Method(name="getAllInstances", parameters={Parameter(name='className')}, type=StringType)
migration_Model_m_getInstances: Method = Method(name="getInstances", parameters={Parameter(name='eClass')}, type=StringType)
migration_Model_m_getInstances: Method = Method(name="getInstances", parameters={Parameter(name='className')}, type=StringType)
migration_Model_m_newInstance: Method = Method(name="newInstance", parameters={Parameter(name='className')}, type=StringType)
migration_Model_m_delete: Method = Method(name="delete", parameters={Parameter(name='instance')})
migration_Model_m_validate: Method = Method(name="validate", parameters={})
migration_Model_m_checkConformance: Method = Method(name="checkConformance", parameters={})
migration_Model_m_commit: Method = Method(name="commit", parameters={})
migration_Model_m_newResource: Method = Method(name="newResource", parameters={Parameter(name='uri')}, type=StringType)
migration_Model_m_getType: Method = Method(name="getType", parameters={Parameter(name='eClass')}, type=StringType)
migration_Model_m_createExtentMap: Method = Method(name="createExtentMap", parameters={})
migration_Model_m_newInstance: Method = Method(name="newInstance", parameters={Parameter(name='eClass')}, type=StringType)
migration_Model.attributes={migration_Model_reflection}
migration_Model.methods={migration_Model_m_getAllInstances, migration_Model_m_getAllInstances, migration_Model_m_createExtentMap, migration_Model_m_newInstance, migration_Model_m_getType, migration_Model_m_commit, migration_Model_m_getInstances, migration_Model_m_newResource, migration_Model_m_validate, migration_Model_m_newInstance, migration_Model_m_delete, migration_Model_m_getInstances, migration_Model_m_checkConformance}

# migration_Metamodel class attributes and methods
migration_Metamodel_m_getEReference: Method = Method(name="getEReference", parameters={Parameter(name='name')}, type=StringType)
migration_Metamodel_m_getEAttribute: Method = Method(name="getEAttribute", parameters={Parameter(name='name')}, type=StringType)
migration_Metamodel_m_getEDataType: Method = Method(name="getEDataType", parameters={Parameter(name='name')}, type=StringType)
migration_Metamodel_m_getElement: Method = Method(name="getElement", parameters={Parameter(name='name')}, type=StringType)
migration_Metamodel_m_validate: Method = Method(name="validate", parameters={})
migration_Metamodel_m_getEPackages: Method = Method(name="getEPackages", parameters={}, type=StringType)
migration_Metamodel_m_setDefaultPackage: Method = Method(name="setDefaultPackage", parameters={Parameter(name='packageName')})
migration_Metamodel_m_getEEnum: Method = Method(name="getEEnum", parameters={Parameter(name='name')}, type=StringType)
migration_Metamodel_m_getEEnumLiteral: Method = Method(name="getEEnumLiteral", parameters={Parameter(name='name')}, type=StringType)
migration_Metamodel_m_delete: Method = Method(name="delete", parameters={Parameter(name='metamodelElement')})
migration_Metamodel_m_getInverse: Method = Method(name="getInverse", parameters={Parameter(name='metamodelElement'), Parameter(name='reference')})
migration_Metamodel_m_getEPackage: Method = Method(name="getEPackage", parameters={Parameter(name='name')}, type=StringType)
migration_Metamodel_m_getEClassifier: Method = Method(name="getEClassifier", parameters={Parameter(name='name')}, type=StringType)
migration_Metamodel_m_getEFeature: Method = Method(name="getEFeature", parameters={Parameter(name='name')}, type=StringType)
migration_Metamodel_m_getEClass: Method = Method(name="getEClass", parameters={Parameter(name='name')}, type=StringType)
migration_Metamodel_m_getESubTypes: Method = Method(name="getESubTypes", parameters={Parameter(name='eClass')}, type=StringType)
migration_Metamodel_m_getEAllSubTypes: Method = Method(name="getEAllSubTypes", parameters={Parameter(name='eClass')}, type=StringType)
migration_Metamodel_m_setEOpposite: Method = Method(name="setEOpposite", parameters={Parameter(name='reference'), Parameter(name='opposite')})
migration_Metamodel.methods={migration_Metamodel_m_getEClassifier, migration_Metamodel_m_getInverse, migration_Metamodel_m_setEOpposite, migration_Metamodel_m_setDefaultPackage, migration_Metamodel_m_getEEnum, migration_Metamodel_m_validate, migration_Metamodel_m_getEClass, migration_Metamodel_m_delete, migration_Metamodel_m_getElement, migration_Metamodel_m_getEReference, migration_Metamodel_m_getEEnumLiteral, migration_Metamodel_m_getEFeature, migration_Metamodel_m_getEAllSubTypes, migration_Metamodel_m_getEDataType, migration_Metamodel_m_getEAttribute, migration_Metamodel_m_getESubTypes, migration_Metamodel_m_getEPackage, migration_Metamodel_m_getEPackages}

# migration_Type class attributes and methods
migration_Type_m_newInstance: Method = Method(name="newInstance", parameters={}, type=StringType)
migration_Type.methods={migration_Type_m_newInstance}

# migration_ModelResource class attributes and methods

# AbstractResource class attributes and methods

# migration_Instance class attributes and methods
migration_Instance_uri: Property = Property(name="uri", type=StringType)
migration_Instance_uuid: Property = Property(name="uuid", type=StringType)
migration_Instance_m_unset: Method = Method(name="unset", parameters={Parameter(name='feature')})
migration_Instance_m_getSlot: Method = Method(name="getSlot", parameters={Parameter(name='feature')}, type=StringType)
migration_Instance_m_get: Method = Method(name="get", parameters={Parameter(name='feature')})
migration_Instance_m_get: Method = Method(name="get", parameters={Parameter(name='featureName')})
migration_Instance_m_getInverse: Method = Method(name="getInverse", parameters={Parameter(name='reference')}, type=StringType)
migration_Instance_m_getInverse: Method = Method(name="getInverse", parameters={Parameter(name='referenceName')}, type=StringType)
migration_Instance_m_getEClass: Method = Method(name="getEClass", parameters={}, type=StringType)
migration_Instance_m_isSet: Method = Method(name="isSet", parameters={Parameter(name='feature')}, type=BooleanType)
migration_Instance_m_set: Method = Method(name="set", parameters={Parameter(name='value'), Parameter(name='feature')})
migration_Instance_m_set: Method = Method(name="set", parameters={Parameter(name='value'), Parameter(name='featureName')})
migration_Instance_m_getContainer: Method = Method(name="getContainer", parameters={}, type=StringType)
migration_Instance_m_add: Method = Method(name="add", parameters={Parameter(name='index'), Parameter(name='feature'), Parameter(name='value')})
migration_Instance_m_add: Method = Method(name="add", parameters={Parameter(name='value'), Parameter(name='feature')})
migration_Instance_m_add: Method = Method(name="add", parameters={Parameter(name='value'), Parameter(name='featureName')})
migration_Instance_m_add: Method = Method(name="add", parameters={Parameter(name='featureName'), Parameter(name='index'), Parameter(name='value')})
migration_Instance_m_remove: Method = Method(name="remove", parameters={Parameter(name='feature'), Parameter(name='value')})
migration_Instance_m_remove: Method = Method(name="remove", parameters={Parameter(name='index'), Parameter(name='feature')})
migration_Instance_m_remove: Method = Method(name="remove", parameters={Parameter(name='featureName'), Parameter(name='value')})
migration_Instance_m_migrate: Method = Method(name="migrate", parameters={Parameter(name='eClass')})
migration_Instance_m_migrate: Method = Method(name="migrate", parameters={Parameter(name='className')})
migration_Instance_m_instanceOf: Method = Method(name="instanceOf", parameters={Parameter(name='eClass')}, type=BooleanType)
migration_Instance_m_instanceOf: Method = Method(name="instanceOf", parameters={Parameter(name='className')}, type=BooleanType)
migration_Instance_m_getContents: Method = Method(name="getContents", parameters={}, type=StringType)
migration_Instance_m_getContainerReference: Method = Method(name="getContainerReference", parameters={}, type=StringType)
migration_Instance_m_getResource: Method = Method(name="getResource", parameters={}, type=StringType)
migration_Instance_m_isProxy: Method = Method(name="isProxy", parameters={}, type=BooleanType)
migration_Instance_m_copy: Method = Method(name="copy", parameters={}, type=StringType)
migration_Instance_m_getLink: Method = Method(name="getLink", parameters={Parameter(name='referenceName')}, type=StringType)
migration_Instance_m_getLinks: Method = Method(name="getLinks", parameters={Parameter(name='referenceName')}, type=StringType)
migration_Instance_m_getLink: Method = Method(name="getLink", parameters={Parameter(name='reference')}, type=StringType)
migration_Instance_m_getLinks: Method = Method(name="getLinks", parameters={Parameter(name='reference')}, type=StringType)
migration_Instance_m_validate: Method = Method(name="validate", parameters={})
migration_Instance_m_validate: Method = Method(name="validate", parameters={Parameter(name='chain')}, type=BooleanType)
migration_Instance_m_evaluate: Method = Method(name="evaluate", parameters={Parameter(name='expression')})
migration_Instance.attributes={migration_Instance_uuid, migration_Instance_uri}
migration_Instance.methods={migration_Instance_m_get, migration_Instance_m_add, migration_Instance_m_add, migration_Instance_m_getLink, migration_Instance_m_getLinks, migration_Instance_m_unset, migration_Instance_m_set, migration_Instance_m_instanceOf, migration_Instance_m_copy, migration_Instance_m_getContainerReference, migration_Instance_m_set, migration_Instance_m_getContainer, migration_Instance_m_get, migration_Instance_m_instanceOf, migration_Instance_m_getResource, migration_Instance_m_getLinks, migration_Instance_m_remove, migration_Instance_m_getInverse, migration_Instance_m_isProxy, migration_Instance_m_validate, migration_Instance_m_getContents, migration_Instance_m_isSet, migration_Instance_m_migrate, migration_Instance_m_add, migration_Instance_m_validate, migration_Instance_m_getEClass, migration_Instance_m_migrate, migration_Instance_m_remove, migration_Instance_m_getLink, migration_Instance_m_add, migration_Instance_m_evaluate, migration_Instance_m_remove, migration_Instance_m_getInverse, migration_Instance_m_getSlot}

# migration_EClass class attributes and methods

# migration_AttributeSlot class attributes and methods
migration_AttributeSlot_values: Property = Property(name="values", type=StringType)
migration_AttributeSlot.attributes={migration_AttributeSlot_values}

# Slot class attributes and methods

# migration_EAttribute class attributes and methods

# migration_EReference class attributes and methods

# migration_Slot class attributes and methods
migration_Slot_m_getEFeature: Method = Method(name="getEFeature", parameters={}, type=StringType)
migration_Slot.methods={migration_Slot_m_getEFeature}

# migration_ReferenceSlot class attributes and methods

# migration_EPackage class attributes and methods

# migration_AbstractResource class attributes and methods
migration_AbstractResource_uri: Property = Property(name="uri", type=StringType)
migration_AbstractResource_encoding: Property = Property(name="encoding", type=StringType)
migration_AbstractResource.attributes={migration_AbstractResource_encoding, migration_AbstractResource_uri}

# migration_MetamodelResource class attributes and methods

# Relationships
model0: BinaryAssociation = BinaryAssociation(
    name="model0",
    ends={
        Property(name="Model", type=migration_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="repository", type=migration_Model, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
metamodel1: BinaryAssociation = BinaryAssociation(
    name="metamodel1",
    ends={
        Property(name="Metamodel", type=migration_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="repository2", type=migration_Metamodel, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
metamodel3: BinaryAssociation = BinaryAssociation(
    name="metamodel3",
    ends={
        Property(name="migration_Metamodel", type=migration_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="migration_Model", type=migration_Metamodel, multiplicity=Multiplicity(0, 1))
    }
)
types4: BinaryAssociation = BinaryAssociation(
    name="types4",
    ends={
        Property(name="Type", type=migration_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="model", type=migration_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resources5: BinaryAssociation = BinaryAssociation(
    name="resources5",
    ends={
        Property(name="ModelResource", type=migration_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="model6", type=migration_ModelResource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
repository7: BinaryAssociation = BinaryAssociation(
    name="repository7",
    ends={
        Property(name="Repository", type=migration_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="model8", type=migration_Repository, multiplicity=Multiplicity(0, 1))
    }
)
rootInstances9: BinaryAssociation = BinaryAssociation(
    name="rootInstances9",
    ends={
        Property(name="migration_Instance", type=migration_ModelResource, multiplicity=Multiplicity(1, 1)),
        Property(name="migration_ModelResource", type=migration_Instance, multiplicity=Multiplicity(0, 9999))
    }
)
model10: BinaryAssociation = BinaryAssociation(
    name="model10",
    ends={
        Property(name="Model11", type=migration_ModelResource, multiplicity=Multiplicity(1, 1)),
        Property(name="resources", type=migration_Model, multiplicity=Multiplicity(0, 1))
    }
)
eClass12: BinaryAssociation = BinaryAssociation(
    name="eClass12",
    ends={
        Property(name="migration_EClass", type=migration_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="migration_Type", type=migration_EClass, multiplicity=Multiplicity(1, 1))
    }
)
instances13: BinaryAssociation = BinaryAssociation(
    name="instances13",
    ends={
        Property(name="Instance", type=migration_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="type", type=migration_Instance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
model14: BinaryAssociation = BinaryAssociation(
    name="model14",
    ends={
        Property(name="Model15", type=migration_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="types", type=migration_Model, multiplicity=Multiplicity(1, 1))
    }
)
instance20: BinaryAssociation = BinaryAssociation(
    name="instance20",
    ends={
        Property(name="Instance21", type=migration_Slot, multiplicity=Multiplicity(1, 1)),
        Property(name="slots", type=migration_Instance, multiplicity=Multiplicity(1, 1))
    }
)
eAttribute22: BinaryAssociation = BinaryAssociation(
    name="eAttribute22",
    ends={
        Property(name="migration_EAttribute", type=migration_AttributeSlot, multiplicity=Multiplicity(1, 1)),
        Property(name="migration_AttributeSlot", type=migration_EAttribute, multiplicity=Multiplicity(1, 1))
    }
)
eReference23: BinaryAssociation = BinaryAssociation(
    name="eReference23",
    ends={
        Property(name="migration_EReference", type=migration_ReferenceSlot, multiplicity=Multiplicity(1, 1)),
        Property(name="migration_ReferenceSlot", type=migration_EReference, multiplicity=Multiplicity(1, 1))
    }
)
slots16: BinaryAssociation = BinaryAssociation(
    name="slots16",
    ends={
        Property(name="Slot", type=migration_Instance, multiplicity=Multiplicity(1, 1)),
        Property(name="instance", type=migration_Slot, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type17: BinaryAssociation = BinaryAssociation(
    name="type17",
    ends={
        Property(name="Type18", type=migration_Instance, multiplicity=Multiplicity(1, 1)),
        Property(name="instances", type=migration_Type, multiplicity=Multiplicity(1, 1))
    }
)
references19: BinaryAssociation = BinaryAssociation(
    name="references19",
    ends={
        Property(name="ReferenceSlot", type=migration_Instance, multiplicity=Multiplicity(1, 1)),
        Property(name="values", type=migration_ReferenceSlot, multiplicity=Multiplicity(0, 9999))
    }
)
values24: BinaryAssociation = BinaryAssociation(
    name="values24",
    ends={
        Property(name="Instance25", type=migration_ReferenceSlot, multiplicity=Multiplicity(1, 1)),
        Property(name="references", type=migration_Instance, multiplicity=Multiplicity(0, 9999))
    }
)
repository27: BinaryAssociation = BinaryAssociation(
    name="repository27",
    ends={
        Property(name="Repository29", type=migration_Metamodel, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel28", type=migration_Repository, multiplicity=Multiplicity(0, 1))
    }
)
defaultPackage30: BinaryAssociation = BinaryAssociation(
    name="defaultPackage30",
    ends={
        Property(name="migration_EPackage", type=migration_Metamodel, multiplicity=Multiplicity(1, 1)),
        Property(name="migration_Metamodel31", type=migration_EPackage, multiplicity=Multiplicity(0, 1))
    }
)
rootPackages32: BinaryAssociation = BinaryAssociation(
    name="rootPackages32",
    ends={
        Property(name="migration_EPackage33", type=migration_MetamodelResource, multiplicity=Multiplicity(1, 1)),
        Property(name="migration_MetamodelResource", type=migration_EPackage, multiplicity=Multiplicity(0, 9999))
    }
)
metamodel34: BinaryAssociation = BinaryAssociation(
    name="metamodel34",
    ends={
        Property(name="Metamodel36", type=migration_MetamodelResource, multiplicity=Multiplicity(1, 1)),
        Property(name="resources35", type=migration_Metamodel, multiplicity=Multiplicity(0, 1))
    }
)
resources26: BinaryAssociation = BinaryAssociation(
    name="resources26",
    ends={
        Property(name="MetamodelResource", type=migration_Metamodel, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel", type=migration_MetamodelResource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_migration_ModelResource_AbstractResource = Generalization(general=AbstractResource, specific=migration_ModelResource)
gen_migration_AttributeSlot_Slot = Generalization(general=Slot, specific=migration_AttributeSlot)
gen_migration_ReferenceSlot_Slot = Generalization(general=Slot, specific=migration_ReferenceSlot)
gen_migration_MetamodelResource_AbstractResource = Generalization(general=AbstractResource, specific=migration_MetamodelResource)

# Domain Model
domain_model = DomainModel(
    name="migration",
    types={migration_Repository, migration_Model, migration_Metamodel, migration_Type, migration_ModelResource, AbstractResource, migration_Instance, migration_EClass, migration_AttributeSlot, Slot, migration_EAttribute, migration_EReference, migration_Slot, migration_ReferenceSlot, migration_EPackage, migration_AbstractResource, migration_MetamodelResource},
    associations={model0, metamodel1, metamodel3, types4, resources5, repository7, rootInstances9, model10, eClass12, instances13, model14, instance20, eAttribute22, eReference23, slots16, type17, references19, values24, repository27, defaultPackage30, rootPackages32, metamodel34, resources26},
    generalizations={gen_migration_ModelResource_AbstractResource, gen_migration_AttributeSlot_Slot, gen_migration_ReferenceSlot_Slot, gen_migration_MetamodelResource_AbstractResource},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)