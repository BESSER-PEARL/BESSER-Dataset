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
jointPackage_UML2ER_JointMM = Class(name="jointPackage::UML2ER::JointMM")
SrcPackage = Class(name="SrcPackage")
TrgStrongReference = Class(name="TrgStrongReference")
jointPackage_UML2ER_SrcPackage = Class(name="jointPackage::UML2ER::SrcPackage")
SrcNamedElement = Class(name="SrcNamedElement")
SrcClass = Class(name="SrcClass")
jointPackage_UML2ER_SrcClass = Class(name="jointPackage::UML2ER::SrcClass")
SrcProperty = Class(name="SrcProperty")
jointPackage_UML2ER_SrcProperty = Class(name="jointPackage::UML2ER::SrcProperty")
jointPackage_UML2ER_SrcNamedElement = Class(name="jointPackage::UML2ER::SrcNamedElement", is_abstract=True)
jointPackage_UML2ER_TrgERModel = Class(name="jointPackage::UML2ER::TrgERModel")
TrgElement = Class(name="TrgElement")
TrgEntityType = Class(name="TrgEntityType")
jointPackage_UML2ER_TrgWeakReference = Class(name="jointPackage::UML2ER::TrgWeakReference")
TrgReference = Class(name="TrgReference")
jointPackage_UML2ER_TrgStrongReference = Class(name="jointPackage::UML2ER::TrgStrongReference")
jointPackage_UML2ER_TrgEntityType = Class(name="jointPackage::UML2ER::TrgEntityType")
TrgFeature = Class(name="TrgFeature")
jointPackage_UML2ER_TrgFeature = Class(name="jointPackage::UML2ER::TrgFeature", is_abstract=True)
jointPackage_UML2ER_TrgAttribute = Class(name="jointPackage::UML2ER::TrgAttribute")
jointPackage_UML2ER_TrgElement = Class(name="jointPackage::UML2ER::TrgElement", is_abstract=True)
jointPackage_UML2ER_TrgReference = Class(name="jointPackage::UML2ER::TrgReference", is_abstract=True)

# jointPackage_UML2ER_JointMM class attributes and methods

# SrcPackage class attributes and methods

# TrgStrongReference class attributes and methods

# jointPackage_UML2ER_SrcPackage class attributes and methods

# SrcNamedElement class attributes and methods

# SrcClass class attributes and methods

# jointPackage_UML2ER_SrcClass class attributes and methods

# SrcProperty class attributes and methods

# jointPackage_UML2ER_SrcProperty class attributes and methods
jointPackage_UML2ER_SrcProperty_primitiveType: Property = Property(name="primitiveType", type=StringType)
jointPackage_UML2ER_SrcProperty_isContainment: Property = Property(name="isContainment", type=BooleanType)
jointPackage_UML2ER_SrcProperty.attributes={jointPackage_UML2ER_SrcProperty_primitiveType, jointPackage_UML2ER_SrcProperty_isContainment}

# jointPackage_UML2ER_SrcNamedElement class attributes and methods
jointPackage_UML2ER_SrcNamedElement_name: Property = Property(name="name", type=StringType)
jointPackage_UML2ER_SrcNamedElement.attributes={jointPackage_UML2ER_SrcNamedElement_name}

# jointPackage_UML2ER_TrgERModel class attributes and methods

# TrgElement class attributes and methods

# TrgEntityType class attributes and methods

# jointPackage_UML2ER_TrgWeakReference class attributes and methods

# TrgReference class attributes and methods

# jointPackage_UML2ER_TrgStrongReference class attributes and methods

# jointPackage_UML2ER_TrgEntityType class attributes and methods

# TrgFeature class attributes and methods

# jointPackage_UML2ER_TrgFeature class attributes and methods

# jointPackage_UML2ER_TrgAttribute class attributes and methods
jointPackage_UML2ER_TrgAttribute_type: Property = Property(name="type", type=StringType)
jointPackage_UML2ER_TrgAttribute.attributes={jointPackage_UML2ER_TrgAttribute_type}

# jointPackage_UML2ER_TrgElement class attributes and methods
jointPackage_UML2ER_TrgElement_name: Property = Property(name="name", type=StringType)
jointPackage_UML2ER_TrgElement.attributes={jointPackage_UML2ER_TrgElement_name}

# jointPackage_UML2ER_TrgReference class attributes and methods

# Relationships
sourceRoot0: BinaryAssociation = BinaryAssociation(
    name="sourceRoot0",
    ends={
        Property(name="SrcPackage", type=jointPackage_UML2ER_JointMM, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_UML2ER_JointMM", type=SrcPackage, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
targetRoot1: BinaryAssociation = BinaryAssociation(
    name="targetRoot1",
    ends={
        Property(name="TrgStrongReference", type=jointPackage_UML2ER_JointMM, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_UML2ER_JointMM2", type=TrgStrongReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ownedElements3: BinaryAssociation = BinaryAssociation(
    name="ownedElements3",
    ends={
        Property(name="SrcClass", type=jointPackage_UML2ER_SrcPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_UML2ER_SrcPackage", type=SrcClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedProperty4: BinaryAssociation = BinaryAssociation(
    name="ownedProperty4",
    ends={
        Property(name="SrcProperty", type=jointPackage_UML2ER_SrcClass, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_UML2ER_SrcClass", type=SrcProperty, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superClasses5: BinaryAssociation = BinaryAssociation(
    name="superClasses5",
    ends={
        Property(name="SrcClass7", type=jointPackage_UML2ER_SrcClass, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_UML2ER_SrcClass6", type=SrcClass, multiplicity=Multiplicity(0, 9999))
    }
)
complexType8: BinaryAssociation = BinaryAssociation(
    name="complexType8",
    ends={
        Property(name="SrcClass9", type=jointPackage_UML2ER_SrcProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_UML2ER_SrcProperty", type=SrcClass, multiplicity=Multiplicity(0, 1))
    }
)
entities10: BinaryAssociation = BinaryAssociation(
    name="entities10",
    ends={
        Property(name="TrgEntityType", type=jointPackage_UML2ER_TrgERModel, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_UML2ER_TrgERModel", type=TrgEntityType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
features11: BinaryAssociation = BinaryAssociation(
    name="features11",
    ends={
        Property(name="TrgFeature", type=jointPackage_UML2ER_TrgEntityType, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_UML2ER_TrgEntityType", type=TrgFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type12: BinaryAssociation = BinaryAssociation(
    name="type12",
    ends={
        Property(name="TrgEntityType13", type=jointPackage_UML2ER_TrgReference, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_UML2ER_TrgReference", type=TrgEntityType, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_jointPackage_UML2ER_SrcPackage_SrcNamedElement = Generalization(general=SrcNamedElement, specific=jointPackage_UML2ER_SrcPackage)
gen_jointPackage_UML2ER_SrcClass_SrcNamedElement = Generalization(general=SrcNamedElement, specific=jointPackage_UML2ER_SrcClass)
gen_jointPackage_UML2ER_SrcProperty_SrcNamedElement = Generalization(general=SrcNamedElement, specific=jointPackage_UML2ER_SrcProperty)
gen_jointPackage_UML2ER_TrgERModel_TrgElement = Generalization(general=TrgElement, specific=jointPackage_UML2ER_TrgERModel)
gen_jointPackage_UML2ER_TrgWeakReference_TrgReference = Generalization(general=TrgReference, specific=jointPackage_UML2ER_TrgWeakReference)
gen_jointPackage_UML2ER_TrgStrongReference_TrgReference = Generalization(general=TrgReference, specific=jointPackage_UML2ER_TrgStrongReference)
gen_jointPackage_UML2ER_TrgEntityType_TrgElement = Generalization(general=TrgElement, specific=jointPackage_UML2ER_TrgEntityType)
gen_jointPackage_UML2ER_TrgFeature_TrgElement = Generalization(general=TrgElement, specific=jointPackage_UML2ER_TrgFeature)
gen_jointPackage_UML2ER_TrgAttribute_TrgFeature = Generalization(general=TrgFeature, specific=jointPackage_UML2ER_TrgAttribute)
gen_jointPackage_UML2ER_TrgReference_TrgFeature = Generalization(general=TrgFeature, specific=jointPackage_UML2ER_TrgReference)

# Domain Model
domain_model = DomainModel(
    name="jointPackage_UML2ER",
    types={jointPackage_UML2ER_JointMM, SrcPackage, TrgStrongReference, jointPackage_UML2ER_SrcPackage, SrcNamedElement, SrcClass, jointPackage_UML2ER_SrcClass, SrcProperty, jointPackage_UML2ER_SrcProperty, jointPackage_UML2ER_SrcNamedElement, jointPackage_UML2ER_TrgERModel, TrgElement, TrgEntityType, jointPackage_UML2ER_TrgWeakReference, TrgReference, jointPackage_UML2ER_TrgStrongReference, jointPackage_UML2ER_TrgEntityType, TrgFeature, jointPackage_UML2ER_TrgFeature, jointPackage_UML2ER_TrgAttribute, jointPackage_UML2ER_TrgElement, jointPackage_UML2ER_TrgReference},
    associations={sourceRoot0, targetRoot1, ownedElements3, ownedProperty4, superClasses5, complexType8, entities10, features11, type12},
    generalizations={gen_jointPackage_UML2ER_SrcPackage_SrcNamedElement, gen_jointPackage_UML2ER_SrcClass_SrcNamedElement, gen_jointPackage_UML2ER_SrcProperty_SrcNamedElement, gen_jointPackage_UML2ER_TrgERModel_TrgElement, gen_jointPackage_UML2ER_TrgWeakReference_TrgReference, gen_jointPackage_UML2ER_TrgStrongReference_TrgReference, gen_jointPackage_UML2ER_TrgEntityType_TrgElement, gen_jointPackage_UML2ER_TrgFeature_TrgElement, gen_jointPackage_UML2ER_TrgAttribute_TrgFeature, gen_jointPackage_UML2ER_TrgReference_TrgFeature},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)