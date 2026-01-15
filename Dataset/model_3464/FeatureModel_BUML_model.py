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
featureModel_FeatureModel = Class(name="featureModel::FeatureModel")
featureModel_Feature = Class(name="featureModel::Feature")
featureModel_Constraints = Class(name="featureModel::Constraints")
featureModel_PropFormula = Class(name="featureModel::PropFormula")
Group = Class(name="Group")
featureModel_Group = Class(name="featureModel::Group")
featureModel_Constraint = Class(name="featureModel::Constraint")
featureModel_ImplyConstraint = Class(name="featureModel::ImplyConstraint")
Constraint = Class(name="Constraint")
featureModel_Proposition = Class(name="featureModel::Proposition")
featureModel_ExcludeConstraint = Class(name="featureModel::ExcludeConstraint")

# featureModel_FeatureModel class attributes and methods

# featureModel_Feature class attributes and methods
featureModel_Feature_name: Property = Property(name="name", type=StringType)
featureModel_Feature.attributes={featureModel_Feature_name}

# featureModel_Constraints class attributes and methods

# featureModel_PropFormula class attributes and methods

# Group class attributes and methods

# featureModel_Group class attributes and methods

# featureModel_Constraint class attributes and methods
featureModel_Constraint_nameA: Property = Property(name="nameA", type=StringType)
featureModel_Constraint_nameB: Property = Property(name="nameB", type=StringType)
featureModel_Constraint.attributes={featureModel_Constraint_nameB, featureModel_Constraint_nameA}

# featureModel_ImplyConstraint class attributes and methods

# Constraint class attributes and methods

# featureModel_Proposition class attributes and methods
featureModel_Proposition_nameA: Property = Property(name="nameA", type=StringType)
featureModel_Proposition_nameRest: Property = Property(name="nameRest", type=StringType)
featureModel_Proposition.attributes={featureModel_Proposition_nameA, featureModel_Proposition_nameRest}

# featureModel_ExcludeConstraint class attributes and methods

# Relationships
rootFeature0: BinaryAssociation = BinaryAssociation(
    name="rootFeature0",
    ends={
        Property(name="featureModel_Feature", type=featureModel_FeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="featureModel_FeatureModel", type=featureModel_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constraints1: BinaryAssociation = BinaryAssociation(
    name="constraints1",
    ends={
        Property(name="featureModel_Constraints", type=featureModel_FeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="featureModel_FeatureModel2", type=featureModel_Constraints, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
propFormula3: BinaryAssociation = BinaryAssociation(
    name="propFormula3",
    ends={
        Property(name="featureModel_PropFormula", type=featureModel_FeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="featureModel_FeatureModel4", type=featureModel_PropFormula, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
children5: BinaryAssociation = BinaryAssociation(
    name="children5",
    ends={
        Property(name="featureModel_Group", type=featureModel_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="featureModel_Feature6", type=featureModel_Group, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constraints7: BinaryAssociation = BinaryAssociation(
    name="constraints7",
    ends={
        Property(name="featureModel_Constraint", type=featureModel_Constraints, multiplicity=Multiplicity(1, 1)),
        Property(name="featureModel_Constraints8", type=featureModel_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
firstProp9: BinaryAssociation = BinaryAssociation(
    name="firstProp9",
    ends={
        Property(name="featureModel_Proposition", type=featureModel_PropFormula, multiplicity=Multiplicity(1, 1)),
        Property(name="featureModel_PropFormula10", type=featureModel_Proposition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rest11: BinaryAssociation = BinaryAssociation(
    name="rest11",
    ends={
        Property(name="featureModel_Proposition13", type=featureModel_PropFormula, multiplicity=Multiplicity(1, 1)),
        Property(name="featureModel_PropFormula12", type=featureModel_Proposition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_featureModel_Feature_Group = Generalization(general=Group, specific=featureModel_Feature)
gen_featureModel_ImplyConstraint_Constraint = Generalization(general=Constraint, specific=featureModel_ImplyConstraint)
gen_featureModel_ExcludeConstraint_Constraint = Generalization(general=Constraint, specific=featureModel_ExcludeConstraint)

# Domain Model
domain_model = DomainModel(
    name="featureModel",
    types={featureModel_FeatureModel, featureModel_Feature, featureModel_Constraints, featureModel_PropFormula, Group, featureModel_Group, featureModel_Constraint, featureModel_ImplyConstraint, Constraint, featureModel_Proposition, featureModel_ExcludeConstraint},
    associations={rootFeature0, constraints1, propFormula3, children5, constraints7, firstProp9, rest11},
    generalizations={gen_featureModel_Feature_Group, gen_featureModel_ImplyConstraint_Constraint, gen_featureModel_ExcludeConstraint_Constraint},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)