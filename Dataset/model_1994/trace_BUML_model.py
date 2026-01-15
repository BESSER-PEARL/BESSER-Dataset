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
trace_EClass = Class(name="trace::EClass")
trace_ClassMapping = Class(name="trace::ClassMapping")
trace_AttributeMapping = Class(name="trace::AttributeMapping")
trace_ReferenceMapping = Class(name="trace::ReferenceMapping")
trace_EAttribute = Class(name="trace::EAttribute")
trace_EReference = Class(name="trace::EReference")
trace_EStructuralFeature = Class(name="trace::EStructuralFeature")
trace_EPackage = Class(name="trace::EPackage")

# trace_Trace class attributes and methods
trace_Trace_m_addClassMapping: Method = Method(name="addClassMapping", parameters={Parameter(name='proto'), Parameter(name='image')}, type=StringType)
trace_Trace_m_addAttributeMapping: Method = Method(name="addAttributeMapping", parameters={Parameter(name='image'), Parameter(name='proto')})
trace_Trace_m_addReferenceMapping: Method = Method(name="addReferenceMapping", parameters={Parameter(name='type'), Parameter(name='image'), Parameter(name='proto')})
trace_Trace.methods={trace_Trace_m_addReferenceMapping, trace_Trace_m_addClassMapping, trace_Trace_m_addAttributeMapping}

# trace_EClass class attributes and methods

# trace_ClassMapping class attributes and methods

# trace_AttributeMapping class attributes and methods

# trace_ReferenceMapping class attributes and methods
trace_ReferenceMapping_type: Property = Property(name="type", type=StringType)
trace_ReferenceMapping.attributes={trace_ReferenceMapping_type}

# trace_EAttribute class attributes and methods

# trace_EReference class attributes and methods

# trace_EStructuralFeature class attributes and methods

# trace_EPackage class attributes and methods

# Relationships
input0: BinaryAssociation = BinaryAssociation(
    name="input0",
    ends={
        Property(name="trace_Trace", type=trace_EPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_EPackage", type=trace_Trace, multiplicity=Multiplicity(1, 1))
    }
)
output1: BinaryAssociation = BinaryAssociation(
    name="output1",
    ends={
        Property(name="trace_EPackage3", type=trace_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Trace2", type=trace_EPackage, multiplicity=Multiplicity(1, 1))
    }
)
inputModelRoot4: BinaryAssociation = BinaryAssociation(
    name="inputModelRoot4",
    ends={
        Property(name="trace_EClass", type=trace_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Trace5", type=trace_EClass, multiplicity=Multiplicity(1, 1))
    }
)
outputModelRoot6: BinaryAssociation = BinaryAssociation(
    name="outputModelRoot6",
    ends={
        Property(name="trace_EClass8", type=trace_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Trace7", type=trace_EClass, multiplicity=Multiplicity(1, 1))
    }
)
classMappings9: BinaryAssociation = BinaryAssociation(
    name="classMappings9",
    ends={
        Property(name="trace_ClassMapping", type=trace_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Trace10", type=trace_ClassMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributeMappings11: BinaryAssociation = BinaryAssociation(
    name="attributeMappings11",
    ends={
        Property(name="trace_AttributeMapping", type=trace_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Trace12", type=trace_AttributeMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referenceMappings13: BinaryAssociation = BinaryAssociation(
    name="referenceMappings13",
    ends={
        Property(name="trace_ReferenceMapping", type=trace_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Trace14", type=trace_ReferenceMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
proto15: BinaryAssociation = BinaryAssociation(
    name="proto15",
    ends={
        Property(name="trace_EClass17", type=trace_ClassMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_ClassMapping16", type=trace_EClass, multiplicity=Multiplicity(1, 1))
    }
)
image18: BinaryAssociation = BinaryAssociation(
    name="image18",
    ends={
        Property(name="trace_EClass20", type=trace_ClassMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_ClassMapping19", type=trace_EClass, multiplicity=Multiplicity(1, 1))
    }
)
proto21: BinaryAssociation = BinaryAssociation(
    name="proto21",
    ends={
        Property(name="trace_EAttribute", type=trace_AttributeMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_AttributeMapping22", type=trace_EAttribute, multiplicity=Multiplicity(1, 1))
    }
)
image23: BinaryAssociation = BinaryAssociation(
    name="image23",
    ends={
        Property(name="trace_EAttribute25", type=trace_AttributeMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_AttributeMapping24", type=trace_EAttribute, multiplicity=Multiplicity(1, 1))
    }
)
proto26: BinaryAssociation = BinaryAssociation(
    name="proto26",
    ends={
        Property(name="trace_EReference", type=trace_ReferenceMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_ReferenceMapping27", type=trace_EReference, multiplicity=Multiplicity(1, 1))
    }
)
image28: BinaryAssociation = BinaryAssociation(
    name="image28",
    ends={
        Property(name="trace_EStructuralFeature", type=trace_ReferenceMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_ReferenceMapping29", type=trace_EStructuralFeature, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="trace",
    types={trace_Trace, trace_EClass, trace_ClassMapping, trace_AttributeMapping, trace_ReferenceMapping, trace_EAttribute, trace_EReference, trace_EStructuralFeature, trace_EPackage, ReferenceMappingType},
    associations={input0, output1, inputModelRoot4, outputModelRoot6, classMappings9, attributeMappings11, referenceMappings13, proto15, image18, proto21, image23, proto26, image28},
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