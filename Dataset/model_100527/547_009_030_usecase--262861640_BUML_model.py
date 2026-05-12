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
mtpusecase_NamedElement = Class(name="mtpusecase_NamedElement")
mtpusecase_Package = Class(name="mtpusecase_Package")
NamedElement = Class(name="NamedElement")
mtpusecase_PackableElement = Class(name="mtpusecase_PackableElement")
mtpusecase_HasInheritance = Class(name="mtpusecase_HasInheritance")
PackableElement = Class(name="PackableElement")
mtpusecase_Generalization = Class(name="mtpusecase_Generalization")
mtpusecase_UseCase = Class(name="mtpusecase_UseCase")
HasInheritance = Class(name="HasInheritance")
mtpusecase_Include = Class(name="mtpusecase_Include")
mtpusecase_Extend = Class(name="mtpusecase_Extend")
mtpusecase_Actor = Class(name="mtpusecase_Actor")
mtpusecase_Relation = Class(name="mtpusecase_Relation")
mtpusecase_DirectedAssociation = Class(name="mtpusecase_DirectedAssociation")
Relation = Class(name="Relation")
mtpusecase_Association = Class(name="mtpusecase_Association")
mtpusecase_Comment = Class(name="mtpusecase_Comment")
mtpusecase_TransformationActor = Class(name="mtpusecase_TransformationActor")
Actor = Class(name="Actor")
mtpusecase_RequirementUseCase = Class(name="mtpusecase_RequirementUseCase")
UseCase = Class(name="UseCase")
mtpusecase_ConstraintComment = Class(name="mtpusecase_ConstraintComment")
Comment = Class(name="Comment")

# mtpusecase_NamedElement class attributes and methods
mtpusecase_NamedElement_name: Property = Property(name="name", type=StringType)
mtpusecase_NamedElement.attributes={mtpusecase_NamedElement_name}

# mtpusecase_Package class attributes and methods

# NamedElement class attributes and methods

# mtpusecase_PackableElement class attributes and methods

# mtpusecase_HasInheritance class attributes and methods

# PackableElement class attributes and methods

# mtpusecase_Generalization class attributes and methods

# mtpusecase_UseCase class attributes and methods

# HasInheritance class attributes and methods

# mtpusecase_Include class attributes and methods

# mtpusecase_Extend class attributes and methods

# mtpusecase_Actor class attributes and methods

# mtpusecase_Relation class attributes and methods

# mtpusecase_DirectedAssociation class attributes and methods
mtpusecase_DirectedAssociation_targetName: Property = Property(name="targetName", type=StringType)
mtpusecase_DirectedAssociation.attributes={mtpusecase_DirectedAssociation_targetName}

# Relation class attributes and methods

# mtpusecase_Association class attributes and methods
mtpusecase_Association_targetName: Property = Property(name="targetName", type=StringType)
mtpusecase_Association_sourceName: Property = Property(name="sourceName", type=StringType)
mtpusecase_Association.attributes={mtpusecase_Association_targetName, mtpusecase_Association_sourceName}

# mtpusecase_Comment class attributes and methods

# mtpusecase_TransformationActor class attributes and methods

# Actor class attributes and methods

# mtpusecase_RequirementUseCase class attributes and methods

# UseCase class attributes and methods

# mtpusecase_ConstraintComment class attributes and methods

# Comment class attributes and methods

# Relationships
packableElements0: BinaryAssociation = BinaryAssociation(
    name="packableElements0",
    ends={
        Property(name="mtpusecase_PackableElement", type=mtpusecase_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="mtpusecase_Package", type=mtpusecase_PackableElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inheritances1: BinaryAssociation = BinaryAssociation(
    name="inheritances1",
    ends={
        Property(name="Generalization", type=mtpusecase_HasInheritance, multiplicity=Multiplicity(1, 1)),
        Property(name="src", type=mtpusecase_Generalization, multiplicity=Multiplicity(0, 9999))
    }
)
src2: BinaryAssociation = BinaryAssociation(
    name="src2",
    ends={
        Property(name="HasInheritance", type=mtpusecase_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="inheritances", type=mtpusecase_HasInheritance, multiplicity=Multiplicity(0, 1))
    }
)
target3: BinaryAssociation = BinaryAssociation(
    name="target3",
    ends={
        Property(name="mtpusecase_HasInheritance", type=mtpusecase_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="mtpusecase_Generalization", type=mtpusecase_HasInheritance, multiplicity=Multiplicity(0, 1))
    }
)
target4: BinaryAssociation = BinaryAssociation(
    name="target4",
    ends={
        Property(name="mtpusecase_PackableElement5", type=mtpusecase_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="mtpusecase_Comment", type=mtpusecase_PackableElement, multiplicity=Multiplicity(0, 1))
    }
)
includes6: BinaryAssociation = BinaryAssociation(
    name="includes6",
    ends={
        Property(name="Include", type=mtpusecase_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=mtpusecase_Include, multiplicity=Multiplicity(0, 1))
    }
)
extends7: BinaryAssociation = BinaryAssociation(
    name="extends7",
    ends={
        Property(name="Extend", type=mtpusecase_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="source8", type=mtpusecase_Extend, multiplicity=Multiplicity(0, 1))
    }
)
source9: BinaryAssociation = BinaryAssociation(
    name="source9",
    ends={
        Property(name="mtpusecase_PackableElement10", type=mtpusecase_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="mtpusecase_Relation", type=mtpusecase_PackableElement, multiplicity=Multiplicity(0, 1))
    }
)
target11: BinaryAssociation = BinaryAssociation(
    name="target11",
    ends={
        Property(name="mtpusecase_PackableElement13", type=mtpusecase_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="mtpusecase_Relation12", type=mtpusecase_PackableElement, multiplicity=Multiplicity(0, 1))
    }
)
source14: BinaryAssociation = BinaryAssociation(
    name="source14",
    ends={
        Property(name="UseCase", type=mtpusecase_Include, multiplicity=Multiplicity(1, 1)),
        Property(name="includes", type=mtpusecase_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
target15: BinaryAssociation = BinaryAssociation(
    name="target15",
    ends={
        Property(name="mtpusecase_UseCase", type=mtpusecase_Include, multiplicity=Multiplicity(1, 1)),
        Property(name="mtpusecase_Include", type=mtpusecase_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
source16: BinaryAssociation = BinaryAssociation(
    name="source16",
    ends={
        Property(name="UseCase17", type=mtpusecase_Extend, multiplicity=Multiplicity(1, 1)),
        Property(name="extends", type=mtpusecase_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
target18: BinaryAssociation = BinaryAssociation(
    name="target18",
    ends={
        Property(name="mtpusecase_UseCase19", type=mtpusecase_Extend, multiplicity=Multiplicity(1, 1)),
        Property(name="mtpusecase_Extend", type=mtpusecase_UseCase, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_mtpusecase_Package_NamedElement = Generalization(general=NamedElement, specific=mtpusecase_Package)
gen_mtpusecase_PackableElement_NamedElement = Generalization(general=NamedElement, specific=mtpusecase_PackableElement)
gen_mtpusecase_HasInheritance_PackableElement = Generalization(general=PackableElement, specific=mtpusecase_HasInheritance)
gen_mtpusecase_Generalization_PackableElement = Generalization(general=PackableElement, specific=mtpusecase_Generalization)
gen_mtpusecase_UseCase_HasInheritance = Generalization(general=HasInheritance, specific=mtpusecase_UseCase)
gen_mtpusecase_Actor_HasInheritance = Generalization(general=HasInheritance, specific=mtpusecase_Actor)
gen_mtpusecase_Relation_PackableElement = Generalization(general=PackableElement, specific=mtpusecase_Relation)
gen_mtpusecase_DirectedAssociation_Relation = Generalization(general=Relation, specific=mtpusecase_DirectedAssociation)
gen_mtpusecase_Association_Relation = Generalization(general=Relation, specific=mtpusecase_Association)
gen_mtpusecase_Comment_PackableElement = Generalization(general=PackableElement, specific=mtpusecase_Comment)
gen_mtpusecase_Extend_PackableElement = Generalization(general=PackableElement, specific=mtpusecase_Extend)
gen_mtpusecase_TransformationActor_Actor = Generalization(general=Actor, specific=mtpusecase_TransformationActor)
gen_mtpusecase_RequirementUseCase_UseCase = Generalization(general=UseCase, specific=mtpusecase_RequirementUseCase)
gen_mtpusecase_ConstraintComment_Comment = Generalization(general=Comment, specific=mtpusecase_ConstraintComment)
gen_mtpusecase_Include_PackableElement = Generalization(general=PackableElement, specific=mtpusecase_Include)

# Domain Model
domain_model = DomainModel(
    name="mtpusecase",
    types={mtpusecase_NamedElement, mtpusecase_Package, NamedElement, mtpusecase_PackableElement, mtpusecase_HasInheritance, PackableElement, mtpusecase_Generalization, mtpusecase_UseCase, HasInheritance, mtpusecase_Include, mtpusecase_Extend, mtpusecase_Actor, mtpusecase_Relation, mtpusecase_DirectedAssociation, Relation, mtpusecase_Association, mtpusecase_Comment, mtpusecase_TransformationActor, Actor, mtpusecase_RequirementUseCase, UseCase, mtpusecase_ConstraintComment, Comment},
    associations={packableElements0, inheritances1, src2, target3, target4, includes6, extends7, source9, target11, source14, target15, source16, target18},
    generalizations={gen_mtpusecase_Package_NamedElement, gen_mtpusecase_PackableElement_NamedElement, gen_mtpusecase_HasInheritance_PackableElement, gen_mtpusecase_Generalization_PackableElement, gen_mtpusecase_UseCase_HasInheritance, gen_mtpusecase_Actor_HasInheritance, gen_mtpusecase_Relation_PackableElement, gen_mtpusecase_DirectedAssociation_Relation, gen_mtpusecase_Association_Relation, gen_mtpusecase_Comment_PackableElement, gen_mtpusecase_Extend_PackableElement, gen_mtpusecase_TransformationActor_Actor, gen_mtpusecase_RequirementUseCase_UseCase, gen_mtpusecase_ConstraintComment_Comment, gen_mtpusecase_Include_PackableElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)