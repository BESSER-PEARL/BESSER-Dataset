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
kind: Enumeration = Enumeration(
    name="kind",
    literals={
            EnumerationLiteral(name="optional"),
			EnumerationLiteral(name="mandatory")
    }
)

Type: Enumeration = Enumeration(
    name="Type",
    literals={
            EnumerationLiteral(name="require"),
			EnumerationLiteral(name="exclude")
    }
)

# Classes
FeatureModel_FeatureModel = Class(name="FeatureModel::FeatureModel")
FeatureModel_RootFeature = Class(name="FeatureModel::RootFeature")
FeatureModel_FeatureConstraint = Class(name="FeatureModel::FeatureConstraint")
FeatureModel_ConfigConstraint = Class(name="FeatureModel::ConfigConstraint", is_abstract=True)
Constraint = Class(name="Constraint")
FeatureModel_Feature = Class(name="FeatureModel::Feature")
FeatureModel_And = Class(name="FeatureModel::And")
ConfigConstraint = Class(name="ConfigConstraint")
FeatureModel_Or = Class(name="FeatureModel::Or")
FeatureModel_Constraint = Class(name="FeatureModel::Constraint", is_abstract=True)
FeatureModel_Xor = Class(name="FeatureModel::Xor")

# FeatureModel_FeatureModel class attributes and methods

# FeatureModel_RootFeature class attributes and methods

# FeatureModel_FeatureConstraint class attributes and methods
FeatureModel_FeatureConstraint_type: Property = Property(name="type", type=StringType)
FeatureModel_FeatureConstraint.attributes={FeatureModel_FeatureConstraint_type}

# FeatureModel_ConfigConstraint class attributes and methods
FeatureModel_ConfigConstraint_kind: Property = Property(name="kind", type=StringType)
FeatureModel_ConfigConstraint.attributes={FeatureModel_ConfigConstraint_kind}

# Constraint class attributes and methods

# FeatureModel_Feature class attributes and methods
FeatureModel_Feature_id: Property = Property(name="id", type=IntegerType)
FeatureModel_Feature_name: Property = Property(name="name", type=StringType)
FeatureModel_Feature.attributes={FeatureModel_Feature_name, FeatureModel_Feature_id}

# FeatureModel_And class attributes and methods

# ConfigConstraint class attributes and methods

# FeatureModel_Or class attributes and methods

# FeatureModel_Constraint class attributes and methods

# FeatureModel_Xor class attributes and methods

# Relationships
RootFeature0: BinaryAssociation = BinaryAssociation(
    name="RootFeature0",
    ends={
        Property(name="FeatureModel_RootFeature", type=FeatureModel_FeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="FeatureModel_FeatureModel", type=FeatureModel_RootFeature, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
FConst1: BinaryAssociation = BinaryAssociation(
    name="FConst1",
    ends={
        Property(name="FeatureModel_FeatureConstraint", type=FeatureModel_FeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="FeatureModel_FeatureModel2", type=FeatureModel_FeatureConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ConfConst3: BinaryAssociation = BinaryAssociation(
    name="ConfConst3",
    ends={
        Property(name="FeatureModel_ConfigConstraint", type=FeatureModel_RootFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="FeatureModel_RootFeature4", type=FeatureModel_ConfigConstraint, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
Features5: BinaryAssociation = BinaryAssociation(
    name="Features5",
    ends={
        Property(name="FeatureModel_Feature", type=FeatureModel_FeatureConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="FeatureModel_FeatureConstraint6", type=FeatureModel_Feature, multiplicity=Multiplicity(2, 2))
    }
)
Config7: BinaryAssociation = BinaryAssociation(
    name="Config7",
    ends={
        Property(name="ConfigConstraint", type=FeatureModel_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="ConfFeatures", type=FeatureModel_ConfigConstraint, multiplicity=Multiplicity(1, 1))
    }
)
ConfFeatures8: BinaryAssociation = BinaryAssociation(
    name="ConfFeatures8",
    ends={
        Property(name="Feature", type=FeatureModel_ConfigConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="Config", type=FeatureModel_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_FeatureModel_FeatureConstraint_Constraint = Generalization(general=Constraint, specific=FeatureModel_FeatureConstraint)
gen_FeatureModel_ConfigConstraint_Constraint = Generalization(general=Constraint, specific=FeatureModel_ConfigConstraint)
gen_FeatureModel_And_ConfigConstraint = Generalization(general=ConfigConstraint, specific=FeatureModel_And)
gen_FeatureModel_Or_ConfigConstraint = Generalization(general=ConfigConstraint, specific=FeatureModel_Or)
gen_FeatureModel_Xor_ConfigConstraint = Generalization(general=ConfigConstraint, specific=FeatureModel_Xor)

# Domain Model
domain_model = DomainModel(
    name="FeatureModel",
    types={FeatureModel_FeatureModel, FeatureModel_RootFeature, FeatureModel_FeatureConstraint, FeatureModel_ConfigConstraint, Constraint, FeatureModel_Feature, FeatureModel_And, ConfigConstraint, FeatureModel_Or, FeatureModel_Constraint, FeatureModel_Xor, kind, Type},
    associations={RootFeature0, FConst1, ConfConst3, Features5, Config7, ConfFeatures8},
    generalizations={gen_FeatureModel_FeatureConstraint_Constraint, gen_FeatureModel_ConfigConstraint_Constraint, gen_FeatureModel_And_ConfigConstraint, gen_FeatureModel_Or_ConfigConstraint, gen_FeatureModel_Xor_ConfigConstraint},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)