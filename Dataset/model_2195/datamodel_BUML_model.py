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
ConstraintType: Enumeration = Enumeration(
    name="ConstraintType",
    literals={
            EnumerationLiteral(name="Undefined"),
			EnumerationLiteral(name="NotAllowed"),
			EnumerationLiteral(name="GlobalIncoming"),
			EnumerationLiteral(name="LocalIncoming"),
			EnumerationLiteral(name="GlobalOutgoing"),
			EnumerationLiteral(name="LocalOutgoing"),
			EnumerationLiteral(name="Expected")
    }
)

# Classes
datamodel_Ensemble = Class(name="datamodel::Ensemble", is_abstract=True)
TreeNode = Class(name="TreeNode")
datamodel_Constraint = Class(name="datamodel::Constraint")
datamodel_SliceRepository = Class(name="datamodel::SliceRepository")
datamodel_Slice = Class(name="datamodel::Slice")
datamodel_EnsembleRepository = Class(name="datamodel::EnsembleRepository")
datamodel_TreeNode = Class(name="datamodel::TreeNode", is_abstract=True)
datamodel_EmptyEnsemble = Class(name="datamodel::EmptyEnsemble")
Ensemble = Class(name="Ensemble")
datamodel_ConcreteEnsemble = Class(name="datamodel::ConcreteEnsemble")

# datamodel_Ensemble class attributes and methods
datamodel_Ensemble_name: Property = Property(name="name", type=StringType)
datamodel_Ensemble_derived: Property = Property(name="derived", type=BooleanType)
datamodel_Ensemble_description: Property = Property(name="description", type=StringType)
datamodel_Ensemble_query: Property = Property(name="query", type=StringType)
datamodel_Ensemble.attributes={datamodel_Ensemble_name, datamodel_Ensemble_query, datamodel_Ensemble_description, datamodel_Ensemble_derived}

# TreeNode class attributes and methods

# datamodel_Constraint class attributes and methods
datamodel_Constraint_dependencyKind: Property = Property(name="dependencyKind", type=StringType)
datamodel_Constraint_constraintType: Property = Property(name="constraintType", type=StringType)
datamodel_Constraint.attributes={datamodel_Constraint_constraintType, datamodel_Constraint_dependencyKind}

# datamodel_SliceRepository class attributes and methods

# datamodel_Slice class attributes and methods
datamodel_Slice_diagram: Property = Property(name="diagram", type=StringType)
datamodel_Slice_name: Property = Property(name="name", type=StringType)
datamodel_Slice.attributes={datamodel_Slice_name, datamodel_Slice_diagram}

# datamodel_EnsembleRepository class attributes and methods

# datamodel_TreeNode class attributes and methods

# datamodel_EmptyEnsemble class attributes and methods

# Ensemble class attributes and methods

# datamodel_ConcreteEnsemble class attributes and methods

# Relationships
constraints0: BinaryAssociation = BinaryAssociation(
    name="constraints0",
    ends={
        Property(name="datamodel_Constraint", type=datamodel_Ensemble, multiplicity=Multiplicity(1, 1)),
        Property(name="datamodel_Ensemble", type=datamodel_Constraint, multiplicity=Multiplicity(0, 9999))
    }
)
source2: BinaryAssociation = BinaryAssociation(
    name="source2",
    ends={
        Property(name="datamodel_Ensemble4", type=datamodel_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="datamodel_Constraint3", type=datamodel_Ensemble, multiplicity=Multiplicity(1, 1))
    }
)
target5: BinaryAssociation = BinaryAssociation(
    name="target5",
    ends={
        Property(name="datamodel_Ensemble7", type=datamodel_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="datamodel_Constraint6", type=datamodel_Ensemble, multiplicity=Multiplicity(1, 1))
    }
)
slices8: BinaryAssociation = BinaryAssociation(
    name="slices8",
    ends={
        Property(name="Slice9", type=datamodel_SliceRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="sliceRepository", type=datamodel_Slice, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
slices1: BinaryAssociation = BinaryAssociation(
    name="slices1",
    ends={
        Property(name="Slice", type=datamodel_Ensemble, multiplicity=Multiplicity(1, 1)),
        Property(name="ensembles", type=datamodel_Slice, multiplicity=Multiplicity(0, 9999))
    }
)
constraints12: BinaryAssociation = BinaryAssociation(
    name="constraints12",
    ends={
        Property(name="datamodel_Constraint13", type=datamodel_Slice, multiplicity=Multiplicity(1, 1)),
        Property(name="datamodel_Slice", type=datamodel_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ensembles14: BinaryAssociation = BinaryAssociation(
    name="ensembles14",
    ends={
        Property(name="Ensemble", type=datamodel_Slice, multiplicity=Multiplicity(1, 1)),
        Property(name="slices", type=datamodel_Ensemble, multiplicity=Multiplicity(0, 9999))
    }
)
sliceRepository15: BinaryAssociation = BinaryAssociation(
    name="sliceRepository15",
    ends={
        Property(name="SliceRepository", type=datamodel_Slice, multiplicity=Multiplicity(1, 1)),
        Property(name="slices16", type=datamodel_SliceRepository, multiplicity=Multiplicity(1, 1))
    }
)
parent18: BinaryAssociation = BinaryAssociation(
    name="parent18",
    ends={
        Property(name="TreeNode", type=datamodel_TreeNode, multiplicity=Multiplicity(1, 1)),
        Property(name="children", type=datamodel_TreeNode, multiplicity=Multiplicity(0, 1))
    }
)
emptyEnsemble10: BinaryAssociation = BinaryAssociation(
    name="emptyEnsemble10",
    ends={
        Property(name="datamodel_Ensemble11", type=datamodel_SliceRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="datamodel_SliceRepository", type=datamodel_Ensemble, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
children20: BinaryAssociation = BinaryAssociation(
    name="children20",
    ends={
        Property(name="TreeNode21", type=datamodel_TreeNode, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=datamodel_TreeNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_datamodel_Ensemble_TreeNode = Generalization(general=TreeNode, specific=datamodel_Ensemble)
gen_datamodel_EnsembleRepository_TreeNode = Generalization(general=TreeNode, specific=datamodel_EnsembleRepository)
gen_datamodel_EmptyEnsemble_Ensemble = Generalization(general=Ensemble, specific=datamodel_EmptyEnsemble)
gen_datamodel_ConcreteEnsemble_Ensemble = Generalization(general=Ensemble, specific=datamodel_ConcreteEnsemble)

# Domain Model
domain_model = DomainModel(
    name="datamodel",
    types={datamodel_Ensemble, TreeNode, datamodel_Constraint, datamodel_SliceRepository, datamodel_Slice, datamodel_EnsembleRepository, datamodel_TreeNode, datamodel_EmptyEnsemble, Ensemble, datamodel_ConcreteEnsemble, ConstraintType},
    associations={constraints0, source2, target5, slices8, slices1, constraints12, ensembles14, sliceRepository15, parent18, emptyEnsemble10, children20},
    generalizations={gen_datamodel_Ensemble_TreeNode, gen_datamodel_EnsembleRepository_TreeNode, gen_datamodel_EmptyEnsemble_Ensemble, gen_datamodel_ConcreteEnsemble_Ensemble},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)