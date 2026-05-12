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
builderState_ResourceDescription = Class(name="builderState_ResourceDescription")
builderState_IEObjectDescription = Class(name="builderState_IEObjectDescription", is_abstract=True)
builderState_IReferenceDescription = Class(name="builderState_IReferenceDescription", is_abstract=True)
builderState_UserDataEntry = Class(name="builderState_UserDataEntry")
builderState_ReferenceDescription = Class(name="builderState_ReferenceDescription")
IReferenceDescription = Class(name="IReferenceDescription")
builderState_EObjectDescription = Class(name="builderState_EObjectDescription")
IEObjectDescription = Class(name="IEObjectDescription")
builderState_EClass = Class(name="builderState_EClass")

# builderState_ResourceDescription class attributes and methods
builderState_ResourceDescription_URI: Property = Property(name="URI", type=StringType)
builderState_ResourceDescription_importedNames: Property = Property(name="importedNames", type=StringType)
builderState_ResourceDescription_m_isEmpty: Method = Method(name="isEmpty", parameters={}, type=BooleanType)
builderState_ResourceDescription_m_getExportedObjectsByType: Method = Method(name="getExportedObjectsByType", parameters={Parameter(name='builderState_type', type=StringType)}, type=StringType)
builderState_ResourceDescription_m_getExportedObjects: Method = Method(name="getExportedObjects", parameters={Parameter(name='builderState_type', type=StringType), Parameter(name='builderState_name', type=StringType), Parameter(name='builderState_ignoreCase', type=StringType)}, type=StringType)
builderState_ResourceDescription_m_getExportedObjectsByObject: Method = Method(name="getExportedObjectsByObject", parameters={Parameter(name='builderState_object', type=StringType)}, type=StringType)
builderState_ResourceDescription.attributes={builderState_ResourceDescription_URI, builderState_ResourceDescription_importedNames}
builderState_ResourceDescription.methods={builderState_ResourceDescription_m_getExportedObjects, builderState_ResourceDescription_m_getExportedObjectsByType, builderState_ResourceDescription_m_getExportedObjectsByObject, builderState_ResourceDescription_m_isEmpty}

# builderState_IEObjectDescription class attributes and methods
builderState_IEObjectDescription_name: Property = Property(name="name", type=StringType)
builderState_IEObjectDescription_m_getEObjectURI: Method = Method(name="getEObjectURI", parameters={}, type=StringType)
builderState_IEObjectDescription_m_getEObjectOrProxy: Method = Method(name="getEObjectOrProxy", parameters={}, type=StringType)
builderState_IEObjectDescription_m_getUserDataKeys: Method = Method(name="getUserDataKeys", parameters={}, type=StringType)
builderState_IEObjectDescription_m_getQualifiedName: Method = Method(name="getQualifiedName", parameters={}, type=StringType)
builderState_IEObjectDescription_m_getUserData: Method = Method(name="getUserData", parameters={Parameter(name='builderState_name', type=StringType)}, type=StringType)
builderState_IEObjectDescription.attributes={builderState_IEObjectDescription_name}
builderState_IEObjectDescription.methods={builderState_IEObjectDescription_m_getUserDataKeys, builderState_IEObjectDescription_m_getUserData, builderState_IEObjectDescription_m_getQualifiedName, builderState_IEObjectDescription_m_getEObjectOrProxy, builderState_IEObjectDescription_m_getEObjectURI}

# builderState_IReferenceDescription class attributes and methods
builderState_IReferenceDescription_sourceEObjectUri: Property = Property(name="sourceEObjectUri", type=StringType)
builderState_IReferenceDescription_targetEObjectUri: Property = Property(name="targetEObjectUri", type=StringType)
builderState_IReferenceDescription_indexInList: Property = Property(name="indexInList", type=IntegerType)
builderState_IReferenceDescription_containerEObjectURI: Property = Property(name="containerEObjectURI", type=StringType)
builderState_IReferenceDescription.attributes={builderState_IReferenceDescription_sourceEObjectUri, builderState_IReferenceDescription_indexInList, builderState_IReferenceDescription_targetEObjectUri, builderState_IReferenceDescription_containerEObjectURI}

# builderState_UserDataEntry class attributes and methods
builderState_UserDataEntry_key: Property = Property(name="key", type=StringType)
builderState_UserDataEntry_value: Property = Property(name="value", type=StringType)
builderState_UserDataEntry.attributes={builderState_UserDataEntry_value, builderState_UserDataEntry_key}

# builderState_ReferenceDescription class attributes and methods
builderState_ReferenceDescription_externalFormOfEReference: Property = Property(name="externalFormOfEReference", type=StringType)
builderState_ReferenceDescription.attributes={builderState_ReferenceDescription_externalFormOfEReference}

# IReferenceDescription class attributes and methods

# builderState_EObjectDescription class attributes and methods
builderState_EObjectDescription_fragment: Property = Property(name="fragment", type=StringType)
builderState_EObjectDescription.attributes={builderState_EObjectDescription_fragment}

# IEObjectDescription class attributes and methods

# builderState_EClass class attributes and methods

# Relationships
exportedObjects0: BinaryAssociation = BinaryAssociation(
    name="exportedObjects0",
    ends={
        Property(name="builderState_IEObjectDescription", type=builderState_ResourceDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="builderState_ResourceDescription", type=builderState_IEObjectDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
userData3: BinaryAssociation = BinaryAssociation(
    name="userData3",
    ends={
        Property(name="builderState_UserDataEntry", type=builderState_EObjectDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="builderState_EObjectDescription", type=builderState_UserDataEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referenceDescriptions1: BinaryAssociation = BinaryAssociation(
    name="referenceDescriptions1",
    ends={
        Property(name="builderState_IReferenceDescription", type=builderState_ResourceDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="builderState_ResourceDescription2", type=builderState_IReferenceDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eClass4: BinaryAssociation = BinaryAssociation(
    name="eClass4",
    ends={
        Property(name="builderState_EClass", type=builderState_IEObjectDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="builderState_IEObjectDescription5", type=builderState_EClass, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_builderState_ReferenceDescription_IReferenceDescription = Generalization(general=IReferenceDescription, specific=builderState_ReferenceDescription)
gen_builderState_EObjectDescription_IEObjectDescription = Generalization(general=IEObjectDescription, specific=builderState_EObjectDescription)

# Domain Model
domain_model = DomainModel(
    name="builderState",
    types={builderState_ResourceDescription, builderState_IEObjectDescription, builderState_IReferenceDescription, builderState_UserDataEntry, builderState_ReferenceDescription, IReferenceDescription, builderState_EObjectDescription, IEObjectDescription, builderState_EClass},
    associations={exportedObjects0, userData3, referenceDescriptions1, eClass4},
    generalizations={gen_builderState_ReferenceDescription_IReferenceDescription, gen_builderState_EObjectDescription_IEObjectDescription},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)