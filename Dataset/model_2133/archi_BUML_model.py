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
architecture_Relationship = Class(name="architecture::Relationship", is_abstract=True)
architecture_AnalysedElement = Class(name="architecture::AnalysedElement", is_abstract=True)
architecture_Project = Class(name="architecture::Project")
architecture_Method = Class(name="architecture::Method")
architecture_ReturnTypeRelationship = Class(name="architecture::ReturnTypeRelationship")
architecture_ParameterRelationship = Class(name="architecture::ParameterRelationship")
architecture_CallRelationship = Class(name="architecture::CallRelationship")
architecture_Field = Class(name="architecture::Field")
architecture_DeclaredType = Class(name="architecture::DeclaredType")
architecture_Type = Class(name="architecture::Type")
AnalysedElement = Class(name="AnalysedElement")
architecture_ArchitectureFile = Class(name="architecture::ArchitectureFile")
architecture_InheritanceDependency = Class(name="architecture::InheritanceDependency")
Dependency = Class(name="Dependency")
architecture_ReferenceDependency = Class(name="architecture::ReferenceDependency")
architecture_Dependency = Class(name="architecture::Dependency", is_abstract=True)
Relationship = Class(name="Relationship")
architecture_Library = Class(name="architecture::Library")
architecture_RuntimeDependency = Class(name="architecture::RuntimeDependency")
architecture_InjectionDependency = Class(name="architecture::InjectionDependency")
RuntimeDependency = Class(name="RuntimeDependency")
architecture_FieldReferenceDependency = Class(name="architecture::FieldReferenceDependency")
ReferenceDependency = Class(name="ReferenceDependency")
architecture_ImportReferenceDependency = Class(name="architecture::ImportReferenceDependency")
architecture_extension_Pattern = Class(name="architecture::extension::Pattern", is_abstract=True)
architecture_extension_Role = Class(name="architecture::extension::Role", is_abstract=True)
architecture_extension_RelationshipConstraint = Class(name="architecture::extension::RelationshipConstraint", is_abstract=True)
architecture_extension_ExtensionRelationship = Class(name="architecture::extension::ExtensionRelationship")
architecture_extension_RoleRelationship = Class(name="architecture::extension::RoleRelationship")
architecture_extension_PatternRelationship = Class(name="architecture::extension::PatternRelationship")
architecture_extension_Bop = Class(name="architecture::extension::Bop")

# architecture_Relationship class attributes and methods
architecture_Relationship_relationShipId: Property = Property(name="relationShipId", type=IntegerType)
architecture_Relationship.attributes={architecture_Relationship_relationShipId}

# architecture_AnalysedElement class attributes and methods
architecture_AnalysedElement_idAnalyzedElement: Property = Property(name="idAnalyzedElement", type=IntegerType)
architecture_AnalysedElement_name: Property = Property(name="name", type=StringType)
architecture_AnalysedElement_properties: Property = Property(name="properties", type=IntegerType)
architecture_AnalysedElement.attributes={architecture_AnalysedElement_name, architecture_AnalysedElement_idAnalyzedElement, architecture_AnalysedElement_properties}

# architecture_Project class attributes and methods

# architecture_Method class attributes and methods

# architecture_ReturnTypeRelationship class attributes and methods

# architecture_ParameterRelationship class attributes and methods

# architecture_CallRelationship class attributes and methods

# architecture_Field class attributes and methods

# architecture_DeclaredType class attributes and methods

# architecture_Type class attributes and methods
architecture_Type_qualifiedName: Property = Property(name="qualifiedName", type=StringType)
architecture_Type_source: Property = Property(name="source", type=BooleanType)
architecture_Type_binary: Property = Property(name="binary", type=BooleanType)
architecture_Type.attributes={architecture_Type_binary, architecture_Type_source, architecture_Type_qualifiedName}

# AnalysedElement class attributes and methods

# architecture_ArchitectureFile class attributes and methods
architecture_ArchitectureFile_path: Property = Property(name="path", type=StringType)
architecture_ArchitectureFile.attributes={architecture_ArchitectureFile_path}

# architecture_InheritanceDependency class attributes and methods

# Dependency class attributes and methods

# architecture_ReferenceDependency class attributes and methods
architecture_ReferenceDependency_uri: Property = Property(name="uri", type=StringType)
architecture_ReferenceDependency_name: Property = Property(name="name", type=StringType)
architecture_ReferenceDependency.attributes={architecture_ReferenceDependency_name, architecture_ReferenceDependency_uri}

# architecture_Dependency class attributes and methods

# Relationship class attributes and methods

# architecture_Library class attributes and methods

# architecture_RuntimeDependency class attributes and methods

# architecture_InjectionDependency class attributes and methods

# RuntimeDependency class attributes and methods

# architecture_FieldReferenceDependency class attributes and methods

# ReferenceDependency class attributes and methods

# architecture_ImportReferenceDependency class attributes and methods

# architecture_extension_Pattern class attributes and methods

# architecture_extension_Role class attributes and methods
architecture_extension_Role_attachedElement: Property = Property(name="attachedElement", type=StringType)
architecture_extension_Role.attributes={architecture_extension_Role_attachedElement}

# architecture_extension_RelationshipConstraint class attributes and methods
architecture_extension_RelationshipConstraint_m_check: Method = Method(name="check", parameters={Parameter(name='relationship')}, type=BooleanType)
architecture_extension_RelationshipConstraint.methods={architecture_extension_RelationshipConstraint_m_check}

# architecture_extension_ExtensionRelationship class attributes and methods
architecture_extension_ExtensionRelationship_m_checkConstraint: Method = Method(name="checkConstraint", parameters={}, type=BooleanType)
architecture_extension_ExtensionRelationship.methods={architecture_extension_ExtensionRelationship_m_checkConstraint}

# architecture_extension_RoleRelationship class attributes and methods
architecture_extension_RoleRelationship_m_checkConstraint: Method = Method(name="checkConstraint", parameters={}, type=BooleanType)
architecture_extension_RoleRelationship_m_getTarget: Method = Method(name="getTarget", parameters={})
architecture_extension_RoleRelationship.methods={architecture_extension_RoleRelationship_m_checkConstraint, architecture_extension_RoleRelationship_m_getTarget}

# architecture_extension_PatternRelationship class attributes and methods
architecture_extension_PatternRelationship_referenceName: Property = Property(name="referenceName", type=StringType)
architecture_extension_PatternRelationship_m_checkConstraint: Method = Method(name="checkConstraint", parameters={}, type=BooleanType)
architecture_extension_PatternRelationship_m_getTarget: Method = Method(name="getTarget", parameters={})
architecture_extension_PatternRelationship_m_getSource: Method = Method(name="getSource", parameters={}, type=StringType)
architecture_extension_PatternRelationship.attributes={architecture_extension_PatternRelationship_referenceName}
architecture_extension_PatternRelationship.methods={architecture_extension_PatternRelationship_m_checkConstraint, architecture_extension_PatternRelationship_m_getSource, architecture_extension_PatternRelationship_m_getTarget}

# architecture_extension_Bop class attributes and methods

# Relationships
outgoingRelationships0: BinaryAssociation = BinaryAssociation(
    name="outgoingRelationships0",
    ends={
        Property(name="Relationship", type=architecture_AnalysedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=architecture_Relationship, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
incomingRelationships1: BinaryAssociation = BinaryAssociation(
    name="incomingRelationships1",
    ends={
        Property(name="Relationship2", type=architecture_AnalysedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=architecture_Relationship, multiplicity=Multiplicity(0, 9999))
    }
)
containedElements4: BinaryAssociation = BinaryAssociation(
    name="containedElements4",
    ends={
        Property(name="AnalysedElement", type=architecture_AnalysedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=architecture_AnalysedElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent6: BinaryAssociation = BinaryAssociation(
    name="parent6",
    ends={
        Property(name="AnalysedElement7", type=architecture_AnalysedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="containedElements", type=architecture_AnalysedElement, multiplicity=Multiplicity(0, 1))
    }
)
target8: BinaryAssociation = BinaryAssociation(
    name="target8",
    ends={
        Property(name="AnalysedElement9", type=architecture_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingRelationships", type=architecture_AnalysedElement, multiplicity=Multiplicity(1, 1))
    }
)
source10: BinaryAssociation = BinaryAssociation(
    name="source10",
    ends={
        Property(name="AnalysedElement11", type=architecture_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingRelationships", type=architecture_AnalysedElement, multiplicity=Multiplicity(1, 1))
    }
)
mapping12: BinaryAssociation = BinaryAssociation(
    name="mapping12",
    ends={
        Property(name="architecture_AnalysedElement", type=architecture_InjectionDependency, multiplicity=Multiplicity(1, 1)),
        Property(name="architecture_InjectionDependency", type=architecture_AnalysedElement, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_architecture_Project_AnalysedElement = Generalization(general=AnalysedElement, specific=architecture_Project)
gen_architecture_Method_AnalysedElement = Generalization(general=AnalysedElement, specific=architecture_Method)
gen_architecture_ReturnTypeRelationship_Relationship = Generalization(general=Relationship, specific=architecture_ReturnTypeRelationship)
gen_architecture_ParameterRelationship_Relationship = Generalization(general=Relationship, specific=architecture_ParameterRelationship)
gen_architecture_CallRelationship_Relationship = Generalization(general=Relationship, specific=architecture_CallRelationship)
gen_architecture_Field_AnalysedElement = Generalization(general=AnalysedElement, specific=architecture_Field)
gen_architecture_DeclaredType_Relationship = Generalization(general=Relationship, specific=architecture_DeclaredType)
gen_architecture_Type_AnalysedElement = Generalization(general=AnalysedElement, specific=architecture_Type)
gen_architecture_ArchitectureFile_AnalysedElement = Generalization(general=AnalysedElement, specific=architecture_ArchitectureFile)
gen_architecture_InheritanceDependency_Dependency = Generalization(general=Dependency, specific=architecture_InheritanceDependency)
gen_architecture_ReferenceDependency_Dependency = Generalization(general=Dependency, specific=architecture_ReferenceDependency)
gen_architecture_Dependency_Relationship = Generalization(general=Relationship, specific=architecture_Dependency)
gen_architecture_Library_AnalysedElement = Generalization(general=AnalysedElement, specific=architecture_Library)
gen_architecture_RuntimeDependency_Dependency = Generalization(general=Dependency, specific=architecture_RuntimeDependency)
gen_architecture_InjectionDependency_RuntimeDependency = Generalization(general=RuntimeDependency, specific=architecture_InjectionDependency)
gen_architecture_FieldReferenceDependency_ReferenceDependency = Generalization(general=ReferenceDependency, specific=architecture_FieldReferenceDependency)
gen_architecture_ImportReferenceDependency_ReferenceDependency = Generalization(general=ReferenceDependency, specific=architecture_ImportReferenceDependency)
gen_architecture_extension_Pattern_AnalysedElement = Generalization(general=AnalysedElement, specific=architecture_extension_Pattern)
gen_architecture_extension_Role_AnalysedElement = Generalization(general=AnalysedElement, specific=architecture_extension_Role)
gen_architecture_extension_ExtensionRelationship_Relationship = Generalization(general=Relationship, specific=architecture_extension_ExtensionRelationship)
gen_architecture_extension_RoleRelationship_Relationship = Generalization(general=Relationship, specific=architecture_extension_RoleRelationship)
gen_architecture_extension_PatternRelationship_Relationship = Generalization(general=Relationship, specific=architecture_extension_PatternRelationship)

# Domain Model
domain_model = DomainModel(
    name="architecture",
    types={architecture_Relationship, architecture_AnalysedElement, architecture_Project, architecture_Method, architecture_ReturnTypeRelationship, architecture_ParameterRelationship, architecture_CallRelationship, architecture_Field, architecture_DeclaredType, architecture_Type, AnalysedElement, architecture_ArchitectureFile, architecture_InheritanceDependency, Dependency, architecture_ReferenceDependency, architecture_Dependency, Relationship, architecture_Library, architecture_RuntimeDependency, architecture_InjectionDependency, RuntimeDependency, architecture_FieldReferenceDependency, ReferenceDependency, architecture_ImportReferenceDependency, architecture_extension_Pattern, architecture_extension_Role, architecture_extension_RelationshipConstraint, architecture_extension_ExtensionRelationship, architecture_extension_RoleRelationship, architecture_extension_PatternRelationship, architecture_extension_Bop},
    associations={outgoingRelationships0, incomingRelationships1, containedElements4, parent6, target8, source10, mapping12},
    generalizations={gen_architecture_Project_AnalysedElement, gen_architecture_Method_AnalysedElement, gen_architecture_ReturnTypeRelationship_Relationship, gen_architecture_ParameterRelationship_Relationship, gen_architecture_CallRelationship_Relationship, gen_architecture_Field_AnalysedElement, gen_architecture_DeclaredType_Relationship, gen_architecture_Type_AnalysedElement, gen_architecture_ArchitectureFile_AnalysedElement, gen_architecture_InheritanceDependency_Dependency, gen_architecture_ReferenceDependency_Dependency, gen_architecture_Dependency_Relationship, gen_architecture_Library_AnalysedElement, gen_architecture_RuntimeDependency_Dependency, gen_architecture_InjectionDependency_RuntimeDependency, gen_architecture_FieldReferenceDependency_ReferenceDependency, gen_architecture_ImportReferenceDependency_ReferenceDependency, gen_architecture_extension_Pattern_AnalysedElement, gen_architecture_extension_Role_AnalysedElement, gen_architecture_extension_ExtensionRelationship_Relationship, gen_architecture_extension_RoleRelationship_Relationship, gen_architecture_extension_PatternRelationship_Relationship},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)