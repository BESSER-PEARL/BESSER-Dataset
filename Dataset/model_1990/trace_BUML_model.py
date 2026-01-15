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
trace_EStructuralFeature = Class(name="trace::EStructuralFeature")
trace_Trace = Class(name="trace::Trace")
trace_OutputFile = Class(name="trace::OutputFile")
trace_InputElement = Class(name="trace::InputElement")
trace_EObject = Class(name="trace::EObject")

# trace_EStructuralFeature class attributes and methods

# trace_Trace class attributes and methods

# trace_OutputFile class attributes and methods
trace_OutputFile_fileName: Property = Property(name="fileName", type=StringType)
trace_OutputFile_outlet: Property = Property(name="outlet", type=StringType)
trace_OutputFile.attributes={trace_OutputFile_outlet, trace_OutputFile_fileName}

# trace_InputElement class attributes and methods

# trace_EObject class attributes and methods

# Relationships
feature8: BinaryAssociation = BinaryAssociation(
    name="feature8",
    ends={
        Property(name="trace_EStructuralFeature", type=trace_InputElement, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_InputElement9", type=trace_EStructuralFeature, multiplicity=Multiplicity(1, 1))
    }
)
outputFiles0: BinaryAssociation = BinaryAssociation(
    name="outputFiles0",
    ends={
        Property(name="trace_OutputFile", type=trace_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Trace", type=trace_OutputFile, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputElements1: BinaryAssociation = BinaryAssociation(
    name="inputElements1",
    ends={
        Property(name="trace_InputElement", type=trace_OutputFile, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_OutputFile2", type=trace_InputElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
targetObject3: BinaryAssociation = BinaryAssociation(
    name="targetObject3",
    ends={
        Property(name="trace_EObject", type=trace_OutputFile, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_OutputFile4", type=trace_EObject, multiplicity=Multiplicity(1, 1))
    }
)
modelElement5: BinaryAssociation = BinaryAssociation(
    name="modelElement5",
    ends={
        Property(name="trace_EObject7", type=trace_InputElement, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_InputElement6", type=trace_EObject, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="trace",
    types={trace_EStructuralFeature, trace_Trace, trace_OutputFile, trace_InputElement, trace_EObject},
    associations={feature8, outputFiles0, inputElements1, targetObject3, modelElement5},
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