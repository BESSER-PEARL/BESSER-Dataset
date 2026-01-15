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
ExtensionDefinitionKind: Enumeration = Enumeration(
    name="ExtensionDefinitionKind",
    literals={
            EnumerationLiteral(name="Association"),
			EnumerationLiteral(name="Generalization"),
			EnumerationLiteral(name="MultiGeneralization"),
			EnumerationLiteral(name="Fusion")
    }
)

# Classes
facademapping_StereotypedMapping = Class(name="facademapping::StereotypedMapping")
Mapping = Class(name="Mapping")
facademapping_FacadeMappping = Class(name="facademapping::FacadeMappping")
facademapping_Mapping = Class(name="facademapping::Mapping")
facademapping_EObject = Class(name="facademapping::EObject")

# facademapping_StereotypedMapping class attributes and methods
facademapping_StereotypedMapping_kind: Property = Property(name="kind", type=StringType)
facademapping_StereotypedMapping.attributes={facademapping_StereotypedMapping_kind}

# Mapping class attributes and methods

# facademapping_FacadeMappping class attributes and methods

# facademapping_Mapping class attributes and methods

# facademapping_EObject class attributes and methods

# Relationships
appliedStereotypes4: BinaryAssociation = BinaryAssociation(
    name="appliedStereotypes4",
    ends={
        Property(name="facademapping_EObject5", type=facademapping_StereotypedMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="facademapping_StereotypedMapping", type=facademapping_EObject, multiplicity=Multiplicity(1, 9999))
    }
)
mappings6: BinaryAssociation = BinaryAssociation(
    name="mappings6",
    ends={
        Property(name="facademapping_Mapping7", type=facademapping_FacadeMappping, multiplicity=Multiplicity(1, 1)),
        Property(name="facademapping_FacadeMappping", type=facademapping_Mapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
umlElement0: BinaryAssociation = BinaryAssociation(
    name="umlElement0",
    ends={
        Property(name="facademapping_EObject", type=facademapping_Mapping, multiplicity=Multiplicity(1, 1)),
        Property(name="facademapping_Mapping", type=facademapping_EObject, multiplicity=Multiplicity(1, 1))
    }
)
specificDomainElement1: BinaryAssociation = BinaryAssociation(
    name="specificDomainElement1",
    ends={
        Property(name="facademapping_EObject3", type=facademapping_Mapping, multiplicity=Multiplicity(1, 1)),
        Property(name="facademapping_Mapping2", type=facademapping_EObject, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_facademapping_StereotypedMapping_Mapping = Generalization(general=Mapping, specific=facademapping_StereotypedMapping)

# Domain Model
domain_model = DomainModel(
    name="facademapping",
    types={facademapping_StereotypedMapping, Mapping, facademapping_FacadeMappping, facademapping_Mapping, facademapping_EObject, ExtensionDefinitionKind},
    associations={appliedStereotypes4, mappings6, umlElement0, specificDomainElement1},
    generalizations={gen_facademapping_StereotypedMapping_Mapping},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)