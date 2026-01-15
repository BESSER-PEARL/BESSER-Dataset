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
fM_FeatureDiagram = Class(name="fM::FeatureDiagram")
fM_Constraints = Class(name="fM::Constraints")
fM_Child = Class(name="fM::Child")
fM_Leaf = Class(name="fM::Leaf")
Child = Class(name="Child")
fM_Node = Class(name="fM::Node")
fM_Rule = Class(name="fM::Rule")
fM_Formula = Class(name="fM::Formula")
fM_RuleElement = Class(name="fM::RuleElement")
Formula = Class(name="Formula")
fM_Var = Class(name="fM::Var")
fM_FeatureModel = Class(name="fM::FeatureModel")

# fM_FeatureDiagram class attributes and methods

# fM_Constraints class attributes and methods

# fM_Child class attributes and methods
fM_Child_mandatory: Property = Property(name="mandatory", type=BooleanType)
fM_Child_name: Property = Property(name="name", type=StringType)
fM_Child.attributes={fM_Child_name, fM_Child_mandatory}

# fM_Leaf class attributes and methods

# Child class attributes and methods

# fM_Node class attributes and methods
fM_Node_open_relation: Property = Property(name="open_relation", type=StringType)
fM_Node_close_relation: Property = Property(name="close_relation", type=StringType)
fM_Node.attributes={fM_Node_close_relation, fM_Node_open_relation}

# fM_Rule class attributes and methods

# fM_Formula class attributes and methods

# fM_RuleElement class attributes and methods
fM_RuleElement_open_operator: Property = Property(name="open_operator", type=StringType)
fM_RuleElement_close_operator: Property = Property(name="close_operator", type=StringType)
fM_RuleElement.attributes={fM_RuleElement_close_operator, fM_RuleElement_open_operator}

# Formula class attributes and methods

# fM_Var class attributes and methods
fM_Var_not: Property = Property(name="not", type=BooleanType)
fM_Var_name: Property = Property(name="name", type=StringType)
fM_Var.attributes={fM_Var_not, fM_Var_name}

# fM_FeatureModel class attributes and methods

# Relationships
diagram0: BinaryAssociation = BinaryAssociation(
    name="diagram0",
    ends={
        Property(name="fM_FeatureDiagram", type=fM_FeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="fM_FeatureModel", type=fM_FeatureDiagram, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constraints1: BinaryAssociation = BinaryAssociation(
    name="constraints1",
    ends={
        Property(name="fM_Constraints", type=fM_FeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="fM_FeatureModel2", type=fM_Constraints, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
root3: BinaryAssociation = BinaryAssociation(
    name="root3",
    ends={
        Property(name="fM_Child", type=fM_FeatureDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="fM_FeatureDiagram4", type=fM_Child, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
children5: BinaryAssociation = BinaryAssociation(
    name="children5",
    ends={
        Property(name="fM_Child6", type=fM_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="fM_Node", type=fM_Child, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rules7: BinaryAssociation = BinaryAssociation(
    name="rules7",
    ends={
        Property(name="fM_Rule", type=fM_Constraints, multiplicity=Multiplicity(1, 1)),
        Property(name="fM_Constraints8", type=fM_Rule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements9: BinaryAssociation = BinaryAssociation(
    name="elements9",
    ends={
        Property(name="fM_Formula", type=fM_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="fM_Rule10", type=fM_Formula, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
left_side11: BinaryAssociation = BinaryAssociation(
    name="left_side11",
    ends={
        Property(name="fM_Var", type=fM_RuleElement, multiplicity=Multiplicity(1, 1)),
        Property(name="fM_RuleElement", type=fM_Var, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right_side12: BinaryAssociation = BinaryAssociation(
    name="right_side12",
    ends={
        Property(name="fM_Var14", type=fM_RuleElement, multiplicity=Multiplicity(1, 1)),
        Property(name="fM_RuleElement13", type=fM_Var, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_fM_Leaf_Child = Generalization(general=Child, specific=fM_Leaf)
gen_fM_Node_Child = Generalization(general=Child, specific=fM_Node)
gen_fM_RuleElement_Formula = Generalization(general=Formula, specific=fM_RuleElement)
gen_fM_Var_Formula = Generalization(general=Formula, specific=fM_Var)

# Domain Model
domain_model = DomainModel(
    name="fM",
    types={fM_FeatureDiagram, fM_Constraints, fM_Child, fM_Leaf, Child, fM_Node, fM_Rule, fM_Formula, fM_RuleElement, Formula, fM_Var, fM_FeatureModel},
    associations={diagram0, constraints1, root3, children5, rules7, elements9, left_side11, right_side12},
    generalizations={gen_fM_Leaf_Child, gen_fM_Node_Child, gen_fM_RuleElement_Formula, gen_fM_Var_Formula},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)