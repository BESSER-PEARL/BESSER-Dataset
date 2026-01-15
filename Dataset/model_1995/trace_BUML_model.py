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
ReferenceMappingType: Enumeration = Enumeration(
    name="ReferenceMappingType",
    literals={
            EnumerationLiteral(name="NONE"),
			EnumerationLiteral(name="TRANSLATED"),
			EnumerationLiteral(name="MAPPED")
    }
)

# Classes
trace_Trace = Class(name="trace::Trace")
trace_ClassMapping = Class(name="trace::ClassMapping")
trace_AttributeMapping = Class(name="trace::AttributeMapping")
trace_ReferenceMapping = Class(name="trace::ReferenceMapping")
trace_EClass = Class(name="trace::EClass")
trace_EAttribute = Class(name="trace::EAttribute")
trace_EReference = Class(name="trace::EReference")
trace_EStructuralFeature = Class(name="trace::EStructuralFeature")

# trace_Trace class attributes and methods

# trace_ClassMapping class attributes and methods

# trace_AttributeMapping class attributes and methods

# trace_ReferenceMapping class attributes and methods
trace_ReferenceMapping_type: Property = Property(name="type", type=StringType)
trace_ReferenceMapping.attributes={trace_ReferenceMapping_type}

# trace_EClass class attributes and methods

# trace_EAttribute class attributes and methods

# trace_EReference class attributes and methods

# trace_EStructuralFeature class attributes and methods

# Relationships
classMappings0: BinaryAssociation = BinaryAssociation(
    name="classMappings0",
    ends={
        Property(name="trace_ClassMapping", type=trace_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Trace", type=trace_ClassMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributeMappings1: BinaryAssociation = BinaryAssociation(
    name="attributeMappings1",
    ends={
        Property(name="trace_AttributeMapping", type=trace_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Trace2", type=trace_AttributeMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referenceMappings3: BinaryAssociation = BinaryAssociation(
    name="referenceMappings3",
    ends={
        Property(name="trace_ReferenceMapping", type=trace_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Trace4", type=trace_ReferenceMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
proto5: BinaryAssociation = BinaryAssociation(
    name="proto5",
    ends={
        Property(name="trace_EClass", type=trace_ClassMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_ClassMapping6", type=trace_EClass, multiplicity=Multiplicity(1, 1))
    }
)
image7: BinaryAssociation = BinaryAssociation(
    name="image7",
    ends={
        Property(name="trace_EClass9", type=trace_ClassMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_ClassMapping8", type=trace_EClass, multiplicity=Multiplicity(1, 1))
    }
)
proto10: BinaryAssociation = BinaryAssociation(
    name="proto10",
    ends={
        Property(name="trace_EAttribute", type=trace_AttributeMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_AttributeMapping11", type=trace_EAttribute, multiplicity=Multiplicity(1, 1))
    }
)
image12: BinaryAssociation = BinaryAssociation(
    name="image12",
    ends={
        Property(name="trace_EAttribute14", type=trace_AttributeMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_AttributeMapping13", type=trace_EAttribute, multiplicity=Multiplicity(1, 1))
    }
)
proto15: BinaryAssociation = BinaryAssociation(
    name="proto15",
    ends={
        Property(name="trace_EReference", type=trace_ReferenceMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_ReferenceMapping16", type=trace_EReference, multiplicity=Multiplicity(1, 1))
    }
)
image17: BinaryAssociation = BinaryAssociation(
    name="image17",
    ends={
        Property(name="trace_EStructuralFeature", type=trace_ReferenceMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_ReferenceMapping18", type=trace_EStructuralFeature, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="trace",
    types={trace_Trace, trace_ClassMapping, trace_AttributeMapping, trace_ReferenceMapping, trace_EClass, trace_EAttribute, trace_EReference, trace_EStructuralFeature, ReferenceMappingType},
    associations={classMappings0, attributeMappings1, referenceMappings3, proto5, image7, proto10, image12, proto15, image17},
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