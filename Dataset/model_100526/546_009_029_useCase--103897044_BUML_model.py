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
UsecaseDSL_Generalization = Class(name="UsecaseDSL_Generalization")
UsecaseDSL_Relationship = Class(name="UsecaseDSL_Relationship", is_abstract=True)
UsecaseDSL_DirectedRelationship = Class(name="UsecaseDSL_DirectedRelationship", is_abstract=True)
Relationship = Class(name="Relationship")
UsecaseDSL_Association_c = Class(name="UsecaseDSL_Association_c")
Classifier = Class(name="Classifier")
MultiplicityElement_c = Class(name="MultiplicityElement_c")
UsecaseDSL_NamedElement = Class(name="UsecaseDSL_NamedElement", is_abstract=True)
UsecaseDSL_Namespace = Class(name="UsecaseDSL_Namespace", is_abstract=True)
NamedElement = Class(name="NamedElement")
UsecaseDSL_Classifier = Class(name="UsecaseDSL_Classifier", is_abstract=True)
Namespace = Class(name="Namespace")
UsecaseDSL_UseCaseDiagram_c = Class(name="UsecaseDSL_UseCaseDiagram_c")
UsecaseDSL_Actor = Class(name="UsecaseDSL_Actor")
UsecaseDSL_MultiplicityElement_c = Class(name="UsecaseDSL_MultiplicityElement_c", is_abstract=True)
DirectedRelationship = Class(name="DirectedRelationship")
UsecaseDSL_Extend_c = Class(name="UsecaseDSL_Extend_c")
UsecaseDSL_ExtensionPoint = Class(name="UsecaseDSL_ExtensionPoint")
UsecaseDSL_System_c = Class(name="UsecaseDSL_System_c")
UsecaseDSL_UseCase = Class(name="UsecaseDSL_UseCase")
UsecaseDSL_Include = Class(name="UsecaseDSL_Include")

# UsecaseDSL_Generalization class attributes and methods

# UsecaseDSL_Relationship class attributes and methods

# UsecaseDSL_DirectedRelationship class attributes and methods

# Relationship class attributes and methods

# UsecaseDSL_Association_c class attributes and methods

# Classifier class attributes and methods

# MultiplicityElement_c class attributes and methods

# UsecaseDSL_NamedElement class attributes and methods
UsecaseDSL_NamedElement_name: Property = Property(name="name", type=StringType)
UsecaseDSL_NamedElement.attributes={UsecaseDSL_NamedElement_name}

# UsecaseDSL_Namespace class attributes and methods

# NamedElement class attributes and methods

# UsecaseDSL_Classifier class attributes and methods

# Namespace class attributes and methods

# UsecaseDSL_UseCaseDiagram_c class attributes and methods

# UsecaseDSL_Actor class attributes and methods

# UsecaseDSL_MultiplicityElement_c class attributes and methods
UsecaseDSL_MultiplicityElement_c_sourceLower: Property = Property(name="sourceLower", type=StringType)
UsecaseDSL_MultiplicityElement_c_sourceUpper: Property = Property(name="sourceUpper", type=StringType)
UsecaseDSL_MultiplicityElement_c_targetLower: Property = Property(name="targetLower", type=StringType)
UsecaseDSL_MultiplicityElement_c_targetUpper: Property = Property(name="targetUpper", type=StringType)
UsecaseDSL_MultiplicityElement_c.attributes={UsecaseDSL_MultiplicityElement_c_sourceLower, UsecaseDSL_MultiplicityElement_c_sourceUpper, UsecaseDSL_MultiplicityElement_c_targetLower, UsecaseDSL_MultiplicityElement_c_targetUpper}

# DirectedRelationship class attributes and methods

# UsecaseDSL_Extend_c class attributes and methods
UsecaseDSL_Extend_c_Expression: Property = Property(name="Expression", type=StringType)
UsecaseDSL_Extend_c.attributes={UsecaseDSL_Extend_c_Expression}

# UsecaseDSL_ExtensionPoint class attributes and methods

# UsecaseDSL_System_c class attributes and methods

# UsecaseDSL_UseCase class attributes and methods

# UsecaseDSL_Include class attributes and methods

# Relationships
generalization2: BinaryAssociation = BinaryAssociation(
    name="generalization2",
    ends={
        Property(name="UsecaseDSL_Generalization", type=UsecaseDSL_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="UsecaseDSL_Classifier3", type=UsecaseDSL_Generalization, multiplicity=Multiplicity(0, 9999))
    }
)
general1: BinaryAssociation = BinaryAssociation(
    name="general1",
    ends={
        Property(name="UsecaseDSL_Classifier", type=UsecaseDSL_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="UsecaseDSL_Classifier0", type=UsecaseDSL_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
specific12: BinaryAssociation = BinaryAssociation(
    name="specific12",
    ends={
        Property(name="UsecaseDSL_Classifier14", type=UsecaseDSL_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="UsecaseDSL_Generalization13", type=UsecaseDSL_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
relationship15: BinaryAssociation = BinaryAssociation(
    name="relationship15",
    ends={
        Property(name="UsecaseDSL_Relationship", type=UsecaseDSL_UseCaseDiagram_c, multiplicity=Multiplicity(1, 1)),
        Property(name="UsecaseDSL_UseCaseDiagram_c", type=UsecaseDSL_Relationship, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classifier16: BinaryAssociation = BinaryAssociation(
    name="classifier16",
    ends={
        Property(name="UsecaseDSL_Classifier18", type=UsecaseDSL_UseCaseDiagram_c, multiplicity=Multiplicity(1, 1)),
        Property(name="UsecaseDSL_UseCaseDiagram_c17", type=UsecaseDSL_Classifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source4: BinaryAssociation = BinaryAssociation(
    name="source4",
    ends={
        Property(name="UsecaseDSL_Classifier5", type=UsecaseDSL_Association_c, multiplicity=Multiplicity(1, 1)),
        Property(name="UsecaseDSL_Association_c", type=UsecaseDSL_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
target6: BinaryAssociation = BinaryAssociation(
    name="target6",
    ends={
        Property(name="UsecaseDSL_Classifier8", type=UsecaseDSL_Association_c, multiplicity=Multiplicity(1, 1)),
        Property(name="UsecaseDSL_Association_c7", type=UsecaseDSL_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
general9: BinaryAssociation = BinaryAssociation(
    name="general9",
    ends={
        Property(name="UsecaseDSL_Classifier11", type=UsecaseDSL_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="UsecaseDSL_Generalization10", type=UsecaseDSL_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
extend31: BinaryAssociation = BinaryAssociation(
    name="extend31",
    ends={
        Property(name="UsecaseDSL_Extend_c", type=UsecaseDSL_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="UsecaseDSL_UseCase32", type=UsecaseDSL_Extend_c, multiplicity=Multiplicity(0, 9999))
    }
)
extensionPoint33: BinaryAssociation = BinaryAssociation(
    name="extensionPoint33",
    ends={
        Property(name="UsecaseDSL_ExtensionPoint", type=UsecaseDSL_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="UsecaseDSL_UseCase34", type=UsecaseDSL_ExtensionPoint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extendedCase35: BinaryAssociation = BinaryAssociation(
    name="extendedCase35",
    ends={
        Property(name="UsecaseDSL_UseCase37", type=UsecaseDSL_Extend_c, multiplicity=Multiplicity(1, 1)),
        Property(name="UsecaseDSL_Extend_c36", type=UsecaseDSL_UseCase, multiplicity=Multiplicity(1, 1))
    }
)
extension38: BinaryAssociation = BinaryAssociation(
    name="extension38",
    ends={
        Property(name="UsecaseDSL_UseCase40", type=UsecaseDSL_Extend_c, multiplicity=Multiplicity(1, 1)),
        Property(name="UsecaseDSL_Extend_c39", type=UsecaseDSL_UseCase, multiplicity=Multiplicity(1, 1))
    }
)
useCase19: BinaryAssociation = BinaryAssociation(
    name="useCase19",
    ends={
        Property(name="UsecaseDSL_UseCase", type=UsecaseDSL_System_c, multiplicity=Multiplicity(1, 1)),
        Property(name="UsecaseDSL_System_c", type=UsecaseDSL_UseCase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedUseCase20: BinaryAssociation = BinaryAssociation(
    name="ownedUseCase20",
    ends={
        Property(name="UsecaseDSL_UseCase22", type=UsecaseDSL_System_c, multiplicity=Multiplicity(1, 1)),
        Property(name="UsecaseDSL_System_c21", type=UsecaseDSL_UseCase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sub23: BinaryAssociation = BinaryAssociation(
    name="sub23",
    ends={
        Property(name="UsecaseDSL_Classifier25", type=UsecaseDSL_System_c, multiplicity=Multiplicity(1, 1)),
        Property(name="UsecaseDSL_System_c24", type=UsecaseDSL_Classifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subject26: BinaryAssociation = BinaryAssociation(
    name="subject26",
    ends={
        Property(name="UsecaseDSL_Classifier28", type=UsecaseDSL_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="UsecaseDSL_UseCase27", type=UsecaseDSL_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
include29: BinaryAssociation = BinaryAssociation(
    name="include29",
    ends={
        Property(name="UsecaseDSL_Include", type=UsecaseDSL_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="UsecaseDSL_UseCase30", type=UsecaseDSL_Include, multiplicity=Multiplicity(0, 9999))
    }
)
addition41: BinaryAssociation = BinaryAssociation(
    name="addition41",
    ends={
        Property(name="UsecaseDSL_UseCase43", type=UsecaseDSL_Include, multiplicity=Multiplicity(1, 1)),
        Property(name="UsecaseDSL_Include42", type=UsecaseDSL_UseCase, multiplicity=Multiplicity(1, 1))
    }
)
includingCase44: BinaryAssociation = BinaryAssociation(
    name="includingCase44",
    ends={
        Property(name="UsecaseDSL_UseCase46", type=UsecaseDSL_Include, multiplicity=Multiplicity(1, 1)),
        Property(name="UsecaseDSL_Include45", type=UsecaseDSL_UseCase, multiplicity=Multiplicity(1, 1))
    }
)
useCase47: BinaryAssociation = BinaryAssociation(
    name="useCase47",
    ends={
        Property(name="UsecaseDSL_UseCase49", type=UsecaseDSL_ExtensionPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="UsecaseDSL_ExtensionPoint48", type=UsecaseDSL_UseCase, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_UsecaseDSL_DirectedRelationship_Relationship = Generalization(general=Relationship, specific=UsecaseDSL_DirectedRelationship)
gen_UsecaseDSL_Association_c_Classifier = Generalization(general=Classifier, specific=UsecaseDSL_Association_c)
gen_UsecaseDSL_Association_c_MultiplicityElement_c = Generalization(general=MultiplicityElement_c, specific=UsecaseDSL_Association_c)
gen_UsecaseDSL_Association_c_Relationship = Generalization(general=Relationship, specific=UsecaseDSL_Association_c)
gen_UsecaseDSL_Namespace_NamedElement = Generalization(general=NamedElement, specific=UsecaseDSL_Namespace)
gen_UsecaseDSL_Classifier_Namespace = Generalization(general=Namespace, specific=UsecaseDSL_Classifier)
gen_UsecaseDSL_UseCaseDiagram_c_Classifier = Generalization(general=Classifier, specific=UsecaseDSL_UseCaseDiagram_c)
gen_UsecaseDSL_Actor_Classifier = Generalization(general=Classifier, specific=UsecaseDSL_Actor)
gen_UsecaseDSL_Generalization_DirectedRelationship = Generalization(general=DirectedRelationship, specific=UsecaseDSL_Generalization)
gen_UsecaseDSL_Extend_c_NamedElement = Generalization(general=NamedElement, specific=UsecaseDSL_Extend_c)
gen_UsecaseDSL_Extend_c_DirectedRelationship = Generalization(general=DirectedRelationship, specific=UsecaseDSL_Extend_c)
gen_UsecaseDSL_System_c_Classifier = Generalization(general=Classifier, specific=UsecaseDSL_System_c)
gen_UsecaseDSL_UseCase_Classifier = Generalization(general=Classifier, specific=UsecaseDSL_UseCase)
gen_UsecaseDSL_Include_NamedElement = Generalization(general=NamedElement, specific=UsecaseDSL_Include)
gen_UsecaseDSL_Include_DirectedRelationship = Generalization(general=DirectedRelationship, specific=UsecaseDSL_Include)
gen_UsecaseDSL_ExtensionPoint_NamedElement = Generalization(general=NamedElement, specific=UsecaseDSL_ExtensionPoint)

# Domain Model
domain_model = DomainModel(
    name="UsecaseDSL",
    types={UsecaseDSL_Generalization, UsecaseDSL_Relationship, UsecaseDSL_DirectedRelationship, Relationship, UsecaseDSL_Association_c, Classifier, MultiplicityElement_c, UsecaseDSL_NamedElement, UsecaseDSL_Namespace, NamedElement, UsecaseDSL_Classifier, Namespace, UsecaseDSL_UseCaseDiagram_c, UsecaseDSL_Actor, UsecaseDSL_MultiplicityElement_c, DirectedRelationship, UsecaseDSL_Extend_c, UsecaseDSL_ExtensionPoint, UsecaseDSL_System_c, UsecaseDSL_UseCase, UsecaseDSL_Include},
    associations={generalization2, general1, specific12, relationship15, classifier16, source4, target6, general9, extend31, extensionPoint33, extendedCase35, extension38, useCase19, ownedUseCase20, sub23, subject26, include29, addition41, includingCase44, useCase47},
    generalizations={gen_UsecaseDSL_DirectedRelationship_Relationship, gen_UsecaseDSL_Association_c_Classifier, gen_UsecaseDSL_Association_c_MultiplicityElement_c, gen_UsecaseDSL_Association_c_Relationship, gen_UsecaseDSL_Namespace_NamedElement, gen_UsecaseDSL_Classifier_Namespace, gen_UsecaseDSL_UseCaseDiagram_c_Classifier, gen_UsecaseDSL_Actor_Classifier, gen_UsecaseDSL_Generalization_DirectedRelationship, gen_UsecaseDSL_Extend_c_NamedElement, gen_UsecaseDSL_Extend_c_DirectedRelationship, gen_UsecaseDSL_System_c_Classifier, gen_UsecaseDSL_UseCase_Classifier, gen_UsecaseDSL_Include_NamedElement, gen_UsecaseDSL_Include_DirectedRelationship, gen_UsecaseDSL_ExtensionPoint_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)