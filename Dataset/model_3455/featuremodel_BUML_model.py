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
GroupType: Enumeration = Enumeration(
    name="GroupType",
    literals={
            EnumerationLiteral(name="OR"),
			EnumerationLiteral(name="ALT")
    }
)

# Classes
FeatureModel_FeatureModel = Class(name="FeatureModel_FeatureModel")
NamedElement = Class(name="NamedElement")
FeatureModel_RequireConstraint = Class(name="FeatureModel_RequireConstraint")
FeatureModel_ExcludeConstraint = Class(name="FeatureModel_ExcludeConstraint")
FeatureModel_Comment = Class(name="FeatureModel_Comment")
FeatureModel_Constraint = Class(name="FeatureModel_Constraint", is_abstract=True)
FeatureModel_Feature = Class(name="FeatureModel_Feature")
FeatureModel_Group = Class(name="FeatureModel_Group")
FeatureModel_NamedElement = Class(name="FeatureModel_NamedElement", is_abstract=True)
Constraint = Class(name="Constraint")

# FeatureModel_FeatureModel class attributes and methods
FeatureModel_FeatureModel_version: Property = Property(name="version", type=FloatType)
FeatureModel_FeatureModel.attributes={FeatureModel_FeatureModel_version}

# NamedElement class attributes and methods

# FeatureModel_RequireConstraint class attributes and methods

# FeatureModel_ExcludeConstraint class attributes and methods

# FeatureModel_Comment class attributes and methods
FeatureModel_Comment_text: Property = Property(name="text", type=StringType)
FeatureModel_Comment.attributes={FeatureModel_Comment_text}

# FeatureModel_Constraint class attributes and methods
FeatureModel_Constraint_language: Property = Property(name="language", type=StringType)
FeatureModel_Constraint_code: Property = Property(name="code", type=StringType)
FeatureModel_Constraint.attributes={FeatureModel_Constraint_language, FeatureModel_Constraint_code}

# FeatureModel_Feature class attributes and methods
FeatureModel_Feature_mandatory: Property = Property(name="mandatory", type=BooleanType)
FeatureModel_Feature_abstract: Property = Property(name="abstract", type=BooleanType)
FeatureModel_Feature_m_atMostInOneGroup: Method = Method(name="atMostInOneGroup", parameters={Parameter(name='FeatureModel_context', type=StringType), Parameter(name='FeatureModel_chain', type=StringType)}, type=BooleanType)
FeatureModel_Feature.attributes={FeatureModel_Feature_mandatory, FeatureModel_Feature_abstract}
FeatureModel_Feature.methods={FeatureModel_Feature_m_atMostInOneGroup}

# FeatureModel_Group class attributes and methods
FeatureModel_Group_groupType: Property = Property(name="groupType", type=StringType)
FeatureModel_Group.attributes={FeatureModel_Group_groupType}

# FeatureModel_NamedElement class attributes and methods
FeatureModel_NamedElement_name: Property = Property(name="name", type=StringType)
FeatureModel_NamedElement.attributes={FeatureModel_NamedElement_name}

# Constraint class attributes and methods

# Relationships
children10: BinaryAssociation = BinaryAssociation(
    name="children10",
    ends={
        Property(name="FeatureModel_Feature11", type=FeatureModel_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="FeatureModel_Feature9", type=FeatureModel_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredConstraints12: BinaryAssociation = BinaryAssociation(
    name="requiredConstraints12",
    ends={
        Property(name="RequireConstraint", type=FeatureModel_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="requiredFeature", type=FeatureModel_RequireConstraint, multiplicity=Multiplicity(0, 9999))
    }
)
requireConstraints13: BinaryAssociation = BinaryAssociation(
    name="requireConstraints13",
    ends={
        Property(name="RequireConstraint14", type=FeatureModel_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="feature", type=FeatureModel_RequireConstraint, multiplicity=Multiplicity(0, 9999))
    }
)
group15: BinaryAssociation = BinaryAssociation(
    name="group15",
    ends={
        Property(name="Group", type=FeatureModel_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="features", type=FeatureModel_Group, multiplicity=Multiplicity(0, 1))
    }
)
excludeConstraintsA16: BinaryAssociation = BinaryAssociation(
    name="excludeConstraintsA16",
    ends={
        Property(name="ExcludeConstraint", type=FeatureModel_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="excludedFeatureA", type=FeatureModel_ExcludeConstraint, multiplicity=Multiplicity(0, 9999))
    }
)
excludeConstraintsB17: BinaryAssociation = BinaryAssociation(
    name="excludeConstraintsB17",
    ends={
        Property(name="ExcludeConstraint18", type=FeatureModel_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="excludedFeatureB", type=FeatureModel_ExcludeConstraint, multiplicity=Multiplicity(0, 9999))
    }
)
comments0: BinaryAssociation = BinaryAssociation(
    name="comments0",
    ends={
        Property(name="FeatureModel_Comment", type=FeatureModel_FeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="FeatureModel_FeatureModel", type=FeatureModel_Comment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constraints1: BinaryAssociation = BinaryAssociation(
    name="constraints1",
    ends={
        Property(name="FeatureModel_Constraint", type=FeatureModel_FeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="FeatureModel_FeatureModel2", type=FeatureModel_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
root3: BinaryAssociation = BinaryAssociation(
    name="root3",
    ends={
        Property(name="FeatureModel_Feature", type=FeatureModel_FeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="FeatureModel_FeatureModel4", type=FeatureModel_Feature, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
groups5: BinaryAssociation = BinaryAssociation(
    name="groups5",
    ends={
        Property(name="FeatureModel_Group", type=FeatureModel_FeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="FeatureModel_FeatureModel6", type=FeatureModel_Group, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
element7: BinaryAssociation = BinaryAssociation(
    name="element7",
    ends={
        Property(name="FeatureModel_NamedElement", type=FeatureModel_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="FeatureModel_Comment8", type=FeatureModel_NamedElement, multiplicity=Multiplicity(1, 1))
    }
)
requiredFeature19: BinaryAssociation = BinaryAssociation(
    name="requiredFeature19",
    ends={
        Property(name="Feature", type=FeatureModel_RequireConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="requiredConstraints", type=FeatureModel_Feature, multiplicity=Multiplicity(1, 1))
    }
)
feature20: BinaryAssociation = BinaryAssociation(
    name="feature20",
    ends={
        Property(name="Feature21", type=FeatureModel_RequireConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="requireConstraints", type=FeatureModel_Feature, multiplicity=Multiplicity(1, 1))
    }
)
excludedFeatureA22: BinaryAssociation = BinaryAssociation(
    name="excludedFeatureA22",
    ends={
        Property(name="Feature23", type=FeatureModel_ExcludeConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="excludeConstraintsA", type=FeatureModel_Feature, multiplicity=Multiplicity(1, 1))
    }
)
excludedFeatureB24: BinaryAssociation = BinaryAssociation(
    name="excludedFeatureB24",
    ends={
        Property(name="Feature25", type=FeatureModel_ExcludeConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="excludeConstraintsB", type=FeatureModel_Feature, multiplicity=Multiplicity(1, 1))
    }
)
features26: BinaryAssociation = BinaryAssociation(
    name="features26",
    ends={
        Property(name="Feature27", type=FeatureModel_Group, multiplicity=Multiplicity(1, 1)),
        Property(name="group", type=FeatureModel_Feature, multiplicity=Multiplicity(2, 9999))
    }
)

# Generalizations
gen_FeatureModel_FeatureModel_NamedElement = Generalization(general=NamedElement, specific=FeatureModel_FeatureModel)
gen_FeatureModel_Constraint_NamedElement = Generalization(general=NamedElement, specific=FeatureModel_Constraint)
gen_FeatureModel_Feature_NamedElement = Generalization(general=NamedElement, specific=FeatureModel_Feature)
gen_FeatureModel_Comment_NamedElement = Generalization(general=NamedElement, specific=FeatureModel_Comment)
gen_FeatureModel_RequireConstraint_Constraint = Generalization(general=Constraint, specific=FeatureModel_RequireConstraint)
gen_FeatureModel_ExcludeConstraint_Constraint = Generalization(general=Constraint, specific=FeatureModel_ExcludeConstraint)
gen_FeatureModel_Group_NamedElement = Generalization(general=NamedElement, specific=FeatureModel_Group)

# Domain Model
domain_model = DomainModel(
    name="FeatureModel",
    types={FeatureModel_FeatureModel, NamedElement, FeatureModel_RequireConstraint, FeatureModel_ExcludeConstraint, FeatureModel_Comment, FeatureModel_Constraint, FeatureModel_Feature, FeatureModel_Group, FeatureModel_NamedElement, Constraint, GroupType},
    associations={children10, requiredConstraints12, requireConstraints13, group15, excludeConstraintsA16, excludeConstraintsB17, comments0, constraints1, root3, groups5, element7, requiredFeature19, feature20, excludedFeatureA22, excludedFeatureB24, features26},
    generalizations={gen_FeatureModel_FeatureModel_NamedElement, gen_FeatureModel_Constraint_NamedElement, gen_FeatureModel_Feature_NamedElement, gen_FeatureModel_Comment_NamedElement, gen_FeatureModel_RequireConstraint_Constraint, gen_FeatureModel_ExcludeConstraint_Constraint, gen_FeatureModel_Group_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)