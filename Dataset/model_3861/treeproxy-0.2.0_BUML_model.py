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
internal_treeproxy_TreeElement = Class(name="internal::treeproxy::TreeElement", is_abstract=True)
internal_treeproxy_EObjectTreeElement = Class(name="internal::treeproxy::EObjectTreeElement")
TreeElement = Class(name="TreeElement")
treeproxy_internal_EObject = Class(name="treeproxy::internal::EObject")
EStructuralFeatureTreeElement = Class(name="EStructuralFeatureTreeElement")
internal_treeproxy_EReferenceTreeElement = Class(name="internal::treeproxy::EReferenceTreeElement")
treeproxy_internal_EReference = Class(name="treeproxy::internal::EReference")
internal_treeproxy_EAttributeTreeElement = Class(name="internal::treeproxy::EAttributeTreeElement")
treeproxy_internal_EAttribute = Class(name="treeproxy::internal::EAttribute")
internal_treeproxy_EStructuralFeatureTreeElement = Class(name="internal::treeproxy::EStructuralFeatureTreeElement")
EObjectTreeElement = Class(name="EObjectTreeElement")

# internal_treeproxy_TreeElement class attributes and methods

# internal_treeproxy_EObjectTreeElement class attributes and methods

# TreeElement class attributes and methods

# treeproxy_internal_EObject class attributes and methods

# EStructuralFeatureTreeElement class attributes and methods

# internal_treeproxy_EReferenceTreeElement class attributes and methods

# treeproxy_internal_EReference class attributes and methods

# internal_treeproxy_EAttributeTreeElement class attributes and methods

# treeproxy_internal_EAttribute class attributes and methods

# internal_treeproxy_EStructuralFeatureTreeElement class attributes and methods

# EObjectTreeElement class attributes and methods

# Relationships
eObject0: BinaryAssociation = BinaryAssociation(
    name="eObject0",
    ends={
        Property(name="treeproxy_internal_EObject", type=internal_treeproxy_EObjectTreeElement, multiplicity=Multiplicity(1, 1)),
        Property(name="internal_treeproxy_EObjectTreeElement", type=treeproxy_internal_EObject, multiplicity=Multiplicity(0, 1))
    }
)
referedEObjectTE9: BinaryAssociation = BinaryAssociation(
    name="referedEObjectTE9",
    ends={
        Property(name="treeproxy11", type=internal_treeproxy_EStructuralFeatureTreeElement, multiplicity=Multiplicity(1, 1)),
        Property(name="EObjectTreeElement10", type=EObjectTreeElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sfTreeElmement1: BinaryAssociation = BinaryAssociation(
    name="sfTreeElmement1",
    ends={
        Property(name="treeproxy", type=internal_treeproxy_EObjectTreeElement, multiplicity=Multiplicity(1, 1)),
        Property(name="EStructuralFeatureTreeElement", type=EStructuralFeatureTreeElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent2: BinaryAssociation = BinaryAssociation(
    name="parent2",
    ends={
        Property(name="treeproxy4", type=internal_treeproxy_EObjectTreeElement, multiplicity=Multiplicity(1, 1)),
        Property(name="EStructuralFeatureTreeElement3", type=EStructuralFeatureTreeElement, multiplicity=Multiplicity(0, 1))
    }
)
eReference5: BinaryAssociation = BinaryAssociation(
    name="eReference5",
    ends={
        Property(name="treeproxy_internal_EReference", type=internal_treeproxy_EReferenceTreeElement, multiplicity=Multiplicity(1, 1)),
        Property(name="internal_treeproxy_EReferenceTreeElement", type=treeproxy_internal_EReference, multiplicity=Multiplicity(0, 1))
    }
)
eAttribute6: BinaryAssociation = BinaryAssociation(
    name="eAttribute6",
    ends={
        Property(name="treeproxy_internal_EAttribute", type=internal_treeproxy_EAttributeTreeElement, multiplicity=Multiplicity(1, 1)),
        Property(name="internal_treeproxy_EAttributeTreeElement", type=treeproxy_internal_EAttribute, multiplicity=Multiplicity(0, 1))
    }
)
parent7: BinaryAssociation = BinaryAssociation(
    name="parent7",
    ends={
        Property(name="treeproxy8", type=internal_treeproxy_EStructuralFeatureTreeElement, multiplicity=Multiplicity(1, 1)),
        Property(name="EObjectTreeElement", type=EObjectTreeElement, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_internal_treeproxy_EObjectTreeElement_TreeElement = Generalization(general=TreeElement, specific=internal_treeproxy_EObjectTreeElement)
gen_internal_treeproxy_EReferenceTreeElement_EStructuralFeatureTreeElement = Generalization(general=EStructuralFeatureTreeElement, specific=internal_treeproxy_EReferenceTreeElement)
gen_internal_treeproxy_EAttributeTreeElement_EStructuralFeatureTreeElement = Generalization(general=EStructuralFeatureTreeElement, specific=internal_treeproxy_EAttributeTreeElement)
gen_internal_treeproxy_EStructuralFeatureTreeElement_TreeElement = Generalization(general=TreeElement, specific=internal_treeproxy_EStructuralFeatureTreeElement)

# Domain Model
domain_model = DomainModel(
    name="internal",
    types={internal_treeproxy_TreeElement, internal_treeproxy_EObjectTreeElement, TreeElement, treeproxy_internal_EObject, EStructuralFeatureTreeElement, internal_treeproxy_EReferenceTreeElement, treeproxy_internal_EReference, internal_treeproxy_EAttributeTreeElement, treeproxy_internal_EAttribute, internal_treeproxy_EStructuralFeatureTreeElement, EObjectTreeElement},
    associations={eObject0, referedEObjectTE9, sfTreeElmement1, parent2, eReference5, eAttribute6, parent7},
    generalizations={gen_internal_treeproxy_EObjectTreeElement_TreeElement, gen_internal_treeproxy_EReferenceTreeElement_EStructuralFeatureTreeElement, gen_internal_treeproxy_EAttributeTreeElement_EStructuralFeatureTreeElement, gen_internal_treeproxy_EStructuralFeatureTreeElement_TreeElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)