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
qvtimperativecs_ImperativeDomainCS = Class(name="qvtimperativecs::ImperativeDomainCS")
DomainCS = Class(name="DomainCS")
qvtimperativecs_PathNameCS = Class(name="qvtimperativecs::PathNameCS")
qvtimperativecs_ImperativePredicateOrAssignmentCS = Class(name="qvtimperativecs::ImperativePredicateOrAssignmentCS")
MappingStatementCS = Class(name="MappingStatementCS")
PredicateOrAssignmentCS = Class(name="PredicateOrAssignmentCS")
qvtimperativecs_MappingCS = Class(name="qvtimperativecs::MappingCS")
AbstractMappingCS = Class(name="AbstractMappingCS")
qvtimperativecs_MappingSequenceCS = Class(name="qvtimperativecs::MappingSequenceCS")
qvtimperativecs_MappingCallBindingCS = Class(name="qvtimperativecs::MappingCallBindingCS")
ExpCS = Class(name="ExpCS")
qvtimperativecs_ExpCS = Class(name="qvtimperativecs::ExpCS")
qvtimperativecs_MappingCallCS = Class(name="qvtimperativecs::MappingCallCS")
qvtimperativecs_Variable = Class(name="qvtimperativecs::Variable")
qvtimperativecs_Mapping = Class(name="qvtimperativecs::Mapping")
qvtimperativecs_MappingLoopCS = Class(name="qvtimperativecs::MappingLoopCS")
qvtimperativecs_VariableCS = Class(name="qvtimperativecs::VariableCS")
qvtimperativecs_MappingStatementCS = Class(name="qvtimperativecs::MappingStatementCS", is_abstract=True)
ModelElementCS = Class(name="ModelElementCS")
qvtimperativecs_TopLevelCS = Class(name="qvtimperativecs::TopLevelCS")
RootPackageCS = Class(name="RootPackageCS")
qvtimperativecs_TransformationCS = Class(name="qvtimperativecs::TransformationCS")
qvtimperativecs_QueryCS = Class(name="qvtimperativecs::QueryCS")

# qvtimperativecs_ImperativeDomainCS class attributes and methods

# DomainCS class attributes and methods

# qvtimperativecs_PathNameCS class attributes and methods

# qvtimperativecs_ImperativePredicateOrAssignmentCS class attributes and methods
qvtimperativecs_ImperativePredicateOrAssignmentCS_isAccumulate: Property = Property(name="isAccumulate", type=BooleanType)
qvtimperativecs_ImperativePredicateOrAssignmentCS.attributes={qvtimperativecs_ImperativePredicateOrAssignmentCS_isAccumulate}

# MappingStatementCS class attributes and methods

# PredicateOrAssignmentCS class attributes and methods

# qvtimperativecs_MappingCS class attributes and methods

# AbstractMappingCS class attributes and methods

# qvtimperativecs_MappingSequenceCS class attributes and methods

# qvtimperativecs_MappingCallBindingCS class attributes and methods
qvtimperativecs_MappingCallBindingCS_isPolled: Property = Property(name="isPolled", type=BooleanType)
qvtimperativecs_MappingCallBindingCS.attributes={qvtimperativecs_MappingCallBindingCS_isPolled}

# ExpCS class attributes and methods

# qvtimperativecs_ExpCS class attributes and methods

# qvtimperativecs_MappingCallCS class attributes and methods
qvtimperativecs_MappingCallCS_isInfinite: Property = Property(name="isInfinite", type=BooleanType)
qvtimperativecs_MappingCallCS.attributes={qvtimperativecs_MappingCallCS_isInfinite}

# qvtimperativecs_Variable class attributes and methods

# qvtimperativecs_Mapping class attributes and methods

# qvtimperativecs_MappingLoopCS class attributes and methods

# qvtimperativecs_VariableCS class attributes and methods

# qvtimperativecs_MappingStatementCS class attributes and methods

# ModelElementCS class attributes and methods

# qvtimperativecs_TopLevelCS class attributes and methods

# RootPackageCS class attributes and methods

# qvtimperativecs_TransformationCS class attributes and methods

# qvtimperativecs_QueryCS class attributes and methods

# Relationships
ownedMappingSequence4: BinaryAssociation = BinaryAssociation(
    name="ownedMappingSequence4",
    ends={
        Property(name="qvtimperativecs_MappingSequenceCS", type=qvtimperativecs_MappingCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtimperativecs_MappingCS", type=qvtimperativecs_MappingSequenceCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedUsesPathNames5: BinaryAssociation = BinaryAssociation(
    name="ownedUsesPathNames5",
    ends={
        Property(name="qvtimperativecs_PathNameCS7", type=qvtimperativecs_MappingCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtimperativecs_MappingCS6", type=qvtimperativecs_PathNameCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
checkedProperties0: BinaryAssociation = BinaryAssociation(
    name="checkedProperties0",
    ends={
        Property(name="qvtimperativecs_PathNameCS", type=qvtimperativecs_ImperativeDomainCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtimperativecs_ImperativeDomainCS", type=qvtimperativecs_PathNameCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedValue8: BinaryAssociation = BinaryAssociation(
    name="ownedValue8",
    ends={
        Property(name="qvtimperativecs_ExpCS", type=qvtimperativecs_MappingCallBindingCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtimperativecs_MappingCallBindingCS", type=qvtimperativecs_ExpCS, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
owningMappingCall9: BinaryAssociation = BinaryAssociation(
    name="owningMappingCall9",
    ends={
        Property(name="MappingCallCS", type=qvtimperativecs_MappingCallBindingCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedBindings", type=qvtimperativecs_MappingCallCS, multiplicity=Multiplicity(0, 1))
    }
)
enforcedProperties1: BinaryAssociation = BinaryAssociation(
    name="enforcedProperties1",
    ends={
        Property(name="qvtimperativecs_PathNameCS3", type=qvtimperativecs_ImperativeDomainCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtimperativecs_ImperativeDomainCS2", type=qvtimperativecs_PathNameCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referredVariable10: BinaryAssociation = BinaryAssociation(
    name="referredVariable10",
    ends={
        Property(name="qvtimperativecs_Variable", type=qvtimperativecs_MappingCallBindingCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtimperativecs_MappingCallBindingCS11", type=qvtimperativecs_Variable, multiplicity=Multiplicity(1, 1))
    }
)
ownedMappingSequence21: BinaryAssociation = BinaryAssociation(
    name="ownedMappingSequence21",
    ends={
        Property(name="qvtimperativecs_MappingSequenceCS23", type=qvtimperativecs_MappingLoopCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtimperativecs_MappingLoopCS22", type=qvtimperativecs_MappingSequenceCS, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ownedBindings12: BinaryAssociation = BinaryAssociation(
    name="ownedBindings12",
    ends={
        Property(name="MappingCallBindingCS", type=qvtimperativecs_MappingCallCS, multiplicity=Multiplicity(1, 1)),
        Property(name="owningMappingCall", type=qvtimperativecs_MappingCallBindingCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedPathName13: BinaryAssociation = BinaryAssociation(
    name="ownedPathName13",
    ends={
        Property(name="qvtimperativecs_PathNameCS14", type=qvtimperativecs_MappingCallCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtimperativecs_MappingCallCS", type=qvtimperativecs_PathNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
referredMapping15: BinaryAssociation = BinaryAssociation(
    name="referredMapping15",
    ends={
        Property(name="qvtimperativecs_Mapping", type=qvtimperativecs_MappingCallCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtimperativecs_MappingCallCS16", type=qvtimperativecs_Mapping, multiplicity=Multiplicity(0, 1))
    }
)
ownedIterator17: BinaryAssociation = BinaryAssociation(
    name="ownedIterator17",
    ends={
        Property(name="qvtimperativecs_VariableCS", type=qvtimperativecs_MappingLoopCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtimperativecs_MappingLoopCS", type=qvtimperativecs_VariableCS, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ownedInExpression18: BinaryAssociation = BinaryAssociation(
    name="ownedInExpression18",
    ends={
        Property(name="qvtimperativecs_ExpCS20", type=qvtimperativecs_MappingLoopCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtimperativecs_MappingLoopCS19", type=qvtimperativecs_ExpCS, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ownedMappingStatements24: BinaryAssociation = BinaryAssociation(
    name="ownedMappingStatements24",
    ends={
        Property(name="qvtimperativecs_MappingStatementCS", type=qvtimperativecs_MappingSequenceCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtimperativecs_MappingSequenceCS25", type=qvtimperativecs_MappingStatementCS, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
ownedTransformations26: BinaryAssociation = BinaryAssociation(
    name="ownedTransformations26",
    ends={
        Property(name="qvtimperativecs_TransformationCS", type=qvtimperativecs_TopLevelCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtimperativecs_TopLevelCS", type=qvtimperativecs_TransformationCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedQueries27: BinaryAssociation = BinaryAssociation(
    name="ownedQueries27",
    ends={
        Property(name="qvtimperativecs_QueryCS", type=qvtimperativecs_TopLevelCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtimperativecs_TopLevelCS28", type=qvtimperativecs_QueryCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedMappings29: BinaryAssociation = BinaryAssociation(
    name="ownedMappings29",
    ends={
        Property(name="qvtimperativecs_MappingCS31", type=qvtimperativecs_TopLevelCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtimperativecs_TopLevelCS30", type=qvtimperativecs_MappingCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_qvtimperativecs_ImperativeDomainCS_DomainCS = Generalization(general=DomainCS, specific=qvtimperativecs_ImperativeDomainCS)
gen_qvtimperativecs_MappingCallCS_MappingStatementCS = Generalization(general=MappingStatementCS, specific=qvtimperativecs_MappingCallCS)
gen_qvtimperativecs_ImperativePredicateOrAssignmentCS_PredicateOrAssignmentCS = Generalization(general=PredicateOrAssignmentCS, specific=qvtimperativecs_ImperativePredicateOrAssignmentCS)
gen_qvtimperativecs_MappingCS_AbstractMappingCS = Generalization(general=AbstractMappingCS, specific=qvtimperativecs_MappingCS)
gen_qvtimperativecs_MappingCallBindingCS_ExpCS = Generalization(general=ExpCS, specific=qvtimperativecs_MappingCallBindingCS)
gen_qvtimperativecs_MappingLoopCS_MappingStatementCS = Generalization(general=MappingStatementCS, specific=qvtimperativecs_MappingLoopCS)
gen_qvtimperativecs_MappingSequenceCS_MappingStatementCS = Generalization(general=MappingStatementCS, specific=qvtimperativecs_MappingSequenceCS)
gen_qvtimperativecs_MappingStatementCS_ModelElementCS = Generalization(general=ModelElementCS, specific=qvtimperativecs_MappingStatementCS)
gen_qvtimperativecs_TopLevelCS_RootPackageCS = Generalization(general=RootPackageCS, specific=qvtimperativecs_TopLevelCS)

# Domain Model
domain_model = DomainModel(
    name="qvtimperativecs",
    types={qvtimperativecs_ImperativeDomainCS, DomainCS, qvtimperativecs_PathNameCS, qvtimperativecs_ImperativePredicateOrAssignmentCS, MappingStatementCS, PredicateOrAssignmentCS, qvtimperativecs_MappingCS, AbstractMappingCS, qvtimperativecs_MappingSequenceCS, qvtimperativecs_MappingCallBindingCS, ExpCS, qvtimperativecs_ExpCS, qvtimperativecs_MappingCallCS, qvtimperativecs_Variable, qvtimperativecs_Mapping, qvtimperativecs_MappingLoopCS, qvtimperativecs_VariableCS, qvtimperativecs_MappingStatementCS, ModelElementCS, qvtimperativecs_TopLevelCS, RootPackageCS, qvtimperativecs_TransformationCS, qvtimperativecs_QueryCS},
    associations={ownedMappingSequence4, ownedUsesPathNames5, checkedProperties0, ownedValue8, owningMappingCall9, enforcedProperties1, referredVariable10, ownedMappingSequence21, ownedBindings12, ownedPathName13, referredMapping15, ownedIterator17, ownedInExpression18, ownedMappingStatements24, ownedTransformations26, ownedQueries27, ownedMappings29},
    generalizations={gen_qvtimperativecs_ImperativeDomainCS_DomainCS, gen_qvtimperativecs_MappingCallCS_MappingStatementCS, gen_qvtimperativecs_ImperativePredicateOrAssignmentCS_PredicateOrAssignmentCS, gen_qvtimperativecs_MappingCS_AbstractMappingCS, gen_qvtimperativecs_MappingCallBindingCS_ExpCS, gen_qvtimperativecs_MappingLoopCS_MappingStatementCS, gen_qvtimperativecs_MappingSequenceCS_MappingStatementCS, gen_qvtimperativecs_MappingStatementCS_ModelElementCS, gen_qvtimperativecs_TopLevelCS_RootPackageCS},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)