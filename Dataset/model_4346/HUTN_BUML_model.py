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
hutn_Spec = Class(name="hutn_Spec")
hutn_NsUri = Class(name="hutn_NsUri")
hutn_PackageObject = Class(name="hutn_PackageObject")
ModelElement = Class(name="ModelElement")
hutn_Object = Class(name="hutn_Object", is_abstract=True)
Object = Class(name="Object")
hutn_EPackage = Class(name="hutn_EPackage")
hutn_ClassObject = Class(name="hutn_ClassObject")
hutn_Slot = Class(name="hutn_Slot", is_abstract=True)
hutn_ModelElement = Class(name="hutn_ModelElement")
hutn_ContainmentSlot = Class(name="hutn_ContainmentSlot")
hutn_ReferenceSlot = Class(name="hutn_ReferenceSlot")
hutn_AttributeSlot = Class(name="hutn_AttributeSlot")
hutn_ClassObjectSlot = Class(name="hutn_ClassObjectSlot", is_abstract=True)

# hutn_Spec class attributes and methods
hutn_Spec_modelFile: Property = Property(name="modelFile", type=StringType)
hutn_Spec_sourceFile: Property = Property(name="sourceFile", type=StringType)
hutn_Spec.attributes={hutn_Spec_sourceFile, hutn_Spec_modelFile}

# hutn_NsUri class attributes and methods
hutn_NsUri_value: Property = Property(name="value", type=StringType)
hutn_NsUri.attributes={hutn_NsUri_value}

# hutn_PackageObject class attributes and methods
hutn_PackageObject_m_getAllEClasses: Method = Method(name="getAllEClasses", parameters={}, type=StringType)
hutn_PackageObject.methods={hutn_PackageObject_m_getAllEClasses}

# ModelElement class attributes and methods

# hutn_Object class attributes and methods
hutn_Object_type: Property = Property(name="type", type=StringType)
hutn_Object_identifier: Property = Property(name="identifier", type=StringType)
hutn_Object.attributes={hutn_Object_identifier, hutn_Object_type}

# Object class attributes and methods

# hutn_EPackage class attributes and methods

# hutn_ClassObject class attributes and methods
hutn_ClassObject_m_findSlot: Method = Method(name="findSlot", parameters={Parameter(name='hutn_feature', type=StringType)})
hutn_ClassObject_m_getPackageObject: Method = Method(name="getPackageObject", parameters={}, type=StringType)
hutn_ClassObject_m_getEClass: Method = Method(name="getEClass", parameters={}, type=StringType)
hutn_ClassObject_m_hasEClass: Method = Method(name="hasEClass", parameters={}, type=BooleanType)
hutn_ClassObject_m_typeCompatibleWith: Method = Method(name="typeCompatibleWith", parameters={Parameter(name='hutn_eClass', type=StringType)}, type=BooleanType)
hutn_ClassObject_m_findOrCreateAttributeSlot: Method = Method(name="findOrCreateAttributeSlot", parameters={Parameter(name='hutn_feature', type=StringType)}, type=StringType)
hutn_ClassObject_m_findOrCreateReferenceSlot: Method = Method(name="findOrCreateReferenceSlot", parameters={Parameter(name='hutn_feature', type=StringType)}, type=StringType)
hutn_ClassObject_m_findOrCreateContainmentSlot: Method = Method(name="findOrCreateContainmentSlot", parameters={Parameter(name='hutn_feature', type=StringType)}, type=StringType)
hutn_ClassObject.methods={hutn_ClassObject_m_hasEClass, hutn_ClassObject_m_typeCompatibleWith, hutn_ClassObject_m_findSlot, hutn_ClassObject_m_getPackageObject, hutn_ClassObject_m_findOrCreateContainmentSlot, hutn_ClassObject_m_getEClass, hutn_ClassObject_m_findOrCreateReferenceSlot, hutn_ClassObject_m_findOrCreateAttributeSlot}

# hutn_Slot class attributes and methods
hutn_Slot_feature: Property = Property(name="feature", type=StringType)
hutn_Slot_values: Property = Property(name="values", type=StringType)
hutn_Slot_m_typeCompatibleWith: Method = Method(name="typeCompatibleWith", parameters={Parameter(name='hutn_eStructuralFeature', type=StringType)}, type=BooleanType)
hutn_Slot_m_multiplicityCompatibleWith: Method = Method(name="multiplicityCompatibleWith", parameters={Parameter(name='hutn_eStructuralFeature', type=StringType)}, type=BooleanType)
hutn_Slot_m_compatibleWith: Method = Method(name="compatibleWith", parameters={Parameter(name='hutn_eStructuralFeature', type=StringType)}, type=BooleanType)
hutn_Slot_m_getEStructuralFeature: Method = Method(name="getEStructuralFeature", parameters={}, type=StringType)
hutn_Slot_m_hasEStructuralFeature: Method = Method(name="hasEStructuralFeature", parameters={}, type=BooleanType)
hutn_Slot_m_setValues: Method = Method(name="setValues", parameters={Parameter(name='hutn_values', type=StringType)})
hutn_Slot.attributes={hutn_Slot_feature, hutn_Slot_values}
hutn_Slot.methods={hutn_Slot_m_multiplicityCompatibleWith, hutn_Slot_m_typeCompatibleWith, hutn_Slot_m_getEStructuralFeature, hutn_Slot_m_setValues, hutn_Slot_m_compatibleWith, hutn_Slot_m_hasEStructuralFeature}

# hutn_ModelElement class attributes and methods
hutn_ModelElement_line: Property = Property(name="line", type=IntegerType)
hutn_ModelElement_col: Property = Property(name="col", type=IntegerType)
hutn_ModelElement.attributes={hutn_ModelElement_line, hutn_ModelElement_col}

# hutn_ContainmentSlot class attributes and methods

# hutn_ReferenceSlot class attributes and methods

# hutn_AttributeSlot class attributes and methods

# hutn_ClassObjectSlot class attributes and methods
hutn_ClassObjectSlot_m_getClassObjects: Method = Method(name="getClassObjects", parameters={}, type=StringType)
hutn_ClassObjectSlot_m_setClassObjects: Method = Method(name="setClassObjects", parameters={Parameter(name='hutn_classObjects', type=StringType)})
hutn_ClassObjectSlot_m_addClassObject: Method = Method(name="addClassObject", parameters={Parameter(name='hutn_classObject', type=StringType)})
hutn_ClassObjectSlot.methods={hutn_ClassObjectSlot_m_setClassObjects, hutn_ClassObjectSlot_m_addClassObject, hutn_ClassObjectSlot_m_getClassObjects}

# Relationships
nsUris0: BinaryAssociation = BinaryAssociation(
    name="nsUris0",
    ends={
        Property(name="hutn_NsUri", type=hutn_Spec, multiplicity=Multiplicity(1, 1)),
        Property(name="hutn_Spec", type=hutn_NsUri, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
objects1: BinaryAssociation = BinaryAssociation(
    name="objects1",
    ends={
        Property(name="hutn_PackageObject", type=hutn_Spec, multiplicity=Multiplicity(1, 1)),
        Property(name="hutn_Spec2", type=hutn_PackageObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
metamodel3: BinaryAssociation = BinaryAssociation(
    name="metamodel3",
    ends={
        Property(name="hutn_EPackage", type=hutn_PackageObject, multiplicity=Multiplicity(1, 1)),
        Property(name="hutn_PackageObject4", type=hutn_EPackage, multiplicity=Multiplicity(0, 9999))
    }
)
classObjects5: BinaryAssociation = BinaryAssociation(
    name="classObjects5",
    ends={
        Property(name="hutn_ClassObject", type=hutn_PackageObject, multiplicity=Multiplicity(1, 1)),
        Property(name="hutn_PackageObject6", type=hutn_ClassObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owner7: BinaryAssociation = BinaryAssociation(
    name="owner7",
    ends={
        Property(name="ClassObject", type=hutn_Slot, multiplicity=Multiplicity(1, 1)),
        Property(name="slots", type=hutn_ClassObject, multiplicity=Multiplicity(1, 1))
    }
)
classObjects8: BinaryAssociation = BinaryAssociation(
    name="classObjects8",
    ends={
        Property(name="hutn_ClassObject9", type=hutn_ContainmentSlot, multiplicity=Multiplicity(1, 1)),
        Property(name="hutn_ContainmentSlot", type=hutn_ClassObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_hutn_NsUri_ModelElement = Generalization(general=ModelElement, specific=hutn_NsUri)
gen_hutn_Object_ModelElement = Generalization(general=ModelElement, specific=hutn_Object)
gen_hutn_PackageObject_Object = Generalization(general=Object, specific=hutn_PackageObject)
gen_hutn_ClassObject_Object = Generalization(general=Object, specific=hutn_ClassObject)
gen_hutn_Slot_ModelElement = Generalization(general=ModelElement, specific=hutn_Slot)

# Domain Model
domain_model = DomainModel(
    name="hutn",
    types={hutn_Spec, hutn_NsUri, hutn_PackageObject, ModelElement, hutn_Object, Object, hutn_EPackage, hutn_ClassObject, hutn_Slot, hutn_ModelElement, hutn_ContainmentSlot, hutn_ReferenceSlot, hutn_AttributeSlot, hutn_ClassObjectSlot},
    associations={nsUris0, objects1, metamodel3, classObjects5, owner7, classObjects8},
    generalizations={gen_hutn_NsUri_ModelElement, gen_hutn_Object_ModelElement, gen_hutn_PackageObject_Object, gen_hutn_ClassObject_Object, gen_hutn_Slot_ModelElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)