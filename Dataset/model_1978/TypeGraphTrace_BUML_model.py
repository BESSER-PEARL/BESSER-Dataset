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
TypeGraphTrace_ClassListTrace = Class(name="TypeGraphTrace_ClassListTrace")
TypeGraphTrace_TMethodSignature = Class(name="TypeGraphTrace_TMethodSignature")
TypeGraphTrace_TClass = Class(name="TypeGraphTrace_TClass")
TypeGraphTrace_Trace = Class(name="TypeGraphTrace_Trace")
TypeGraphTrace_TypeGraph = Class(name="TypeGraphTrace_TypeGraph")
TypeGraphTrace_MethodSignatureTrace = Class(name="TypeGraphTrace_MethodSignatureTrace")

# TypeGraphTrace_ClassListTrace class attributes and methods
TypeGraphTrace_ClassListTrace_concatSignature: Property = Property(name="concatSignature", type=StringType)
TypeGraphTrace_ClassListTrace.attributes={TypeGraphTrace_ClassListTrace_concatSignature}

# TypeGraphTrace_TMethodSignature class attributes and methods

# TypeGraphTrace_TClass class attributes and methods

# TypeGraphTrace_Trace class attributes and methods

# TypeGraphTrace_TypeGraph class attributes and methods

# TypeGraphTrace_MethodSignatureTrace class attributes and methods
TypeGraphTrace_MethodSignatureTrace_signatureString: Property = Property(name="signatureString", type=StringType)
TypeGraphTrace_MethodSignatureTrace.attributes={TypeGraphTrace_MethodSignatureTrace_signatureString}

# Relationships
classLists3: BinaryAssociation = BinaryAssociation(
    name="classLists3",
    ends={
        Property(name="TypeGraphTrace_ClassListTrace", type=TypeGraphTrace_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="TypeGraphTrace_Trace4", type=TypeGraphTrace_ClassListTrace, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tMethodSignature5: BinaryAssociation = BinaryAssociation(
    name="tMethodSignature5",
    ends={
        Property(name="TypeGraphTrace_TMethodSignature", type=TypeGraphTrace_MethodSignatureTrace, multiplicity=Multiplicity(1, 1)),
        Property(name="TypeGraphTrace_MethodSignatureTrace6", type=TypeGraphTrace_TMethodSignature, multiplicity=Multiplicity(0, 1))
    }
)
tClasses7: BinaryAssociation = BinaryAssociation(
    name="tClasses7",
    ends={
        Property(name="TypeGraphTrace_TClass", type=TypeGraphTrace_ClassListTrace, multiplicity=Multiplicity(1, 1)),
        Property(name="TypeGraphTrace_ClassListTrace8", type=TypeGraphTrace_TClass, multiplicity=Multiplicity(0, 9999))
    }
)
programGraph0: BinaryAssociation = BinaryAssociation(
    name="programGraph0",
    ends={
        Property(name="TypeGraphTrace_TypeGraph", type=TypeGraphTrace_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="TypeGraphTrace_Trace", type=TypeGraphTrace_TypeGraph, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
methodSignatures1: BinaryAssociation = BinaryAssociation(
    name="methodSignatures1",
    ends={
        Property(name="TypeGraphTrace_MethodSignatureTrace", type=TypeGraphTrace_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="TypeGraphTrace_Trace2", type=TypeGraphTrace_MethodSignatureTrace, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="TypeGraphTrace",
    types={TypeGraphTrace_ClassListTrace, TypeGraphTrace_TMethodSignature, TypeGraphTrace_TClass, TypeGraphTrace_Trace, TypeGraphTrace_TypeGraph, TypeGraphTrace_MethodSignatureTrace},
    associations={classLists3, tMethodSignature5, tClasses7, programGraph0, methodSignatures1},
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