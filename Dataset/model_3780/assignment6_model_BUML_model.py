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
			EnumerationLiteral(name="XOR")
    }
)

BinaryOperator: Enumeration = Enumeration(
    name="BinaryOperator",
    literals={
            EnumerationLiteral(name="AND"),
			EnumerationLiteral(name="OR")
    }
)

# Classes
assignment6_model_Configurator = Class(name="assignment6::model::Configurator")
assignment6_model_Feature = Class(name="assignment6::model::Feature", is_abstract=True)
assignment6_model_IntegerFeature = Class(name="assignment6::model::IntegerFeature")
assignment6_model_Group = Class(name="assignment6::model::Group")
assignment6_model_Dependency = Class(name="assignment6::model::Dependency", is_abstract=True)
assignment6_model_SimpleFeature = Class(name="assignment6::model::SimpleFeature")
Feature = Class(name="Feature")
assignment6_model_UnaryDependency = Class(name="assignment6::model::UnaryDependency", is_abstract=True)
Dependency = Class(name="Dependency")
assignment6_model_BinaryDependency = Class(name="assignment6::model::BinaryDependency")
assignment6_model_IsSelectedDependency = Class(name="assignment6::model::IsSelectedDependency")
UnaryDependency = Class(name="UnaryDependency")
assignment6_model_IntegerValueDependency = Class(name="assignment6::model::IntegerValueDependency")

# assignment6_model_Configurator class attributes and methods
assignment6_model_Configurator_name: Property = Property(name="name", type=StringType)
assignment6_model_Configurator.attributes={assignment6_model_Configurator_name}

# assignment6_model_Feature class attributes and methods
assignment6_model_Feature_name: Property = Property(name="name", type=StringType)
assignment6_model_Feature_mandatory: Property = Property(name="mandatory", type=BooleanType)
assignment6_model_Feature_selected: Property = Property(name="selected", type=BooleanType)
assignment6_model_Feature.attributes={assignment6_model_Feature_name, assignment6_model_Feature_mandatory, assignment6_model_Feature_selected}

# assignment6_model_IntegerFeature class attributes and methods
assignment6_model_IntegerFeature_minValue: Property = Property(name="minValue", type=IntegerType)
assignment6_model_IntegerFeature_maxValue: Property = Property(name="maxValue", type=IntegerType)
assignment6_model_IntegerFeature_step: Property = Property(name="step", type=IntegerType)
assignment6_model_IntegerFeature_value: Property = Property(name="value", type=IntegerType)
assignment6_model_IntegerFeature.attributes={assignment6_model_IntegerFeature_value, assignment6_model_IntegerFeature_minValue, assignment6_model_IntegerFeature_step, assignment6_model_IntegerFeature_maxValue}

# assignment6_model_Group class attributes and methods
assignment6_model_Group_name: Property = Property(name="name", type=StringType)
assignment6_model_Group_groupType: Property = Property(name="groupType", type=StringType)
assignment6_model_Group.attributes={assignment6_model_Group_name, assignment6_model_Group_groupType}

# assignment6_model_Dependency class attributes and methods
assignment6_model_Dependency_not: Property = Property(name="not", type=BooleanType)
assignment6_model_Dependency.attributes={assignment6_model_Dependency_not}

# assignment6_model_SimpleFeature class attributes and methods

# Feature class attributes and methods

# assignment6_model_UnaryDependency class attributes and methods

# Dependency class attributes and methods

# assignment6_model_BinaryDependency class attributes and methods
assignment6_model_BinaryDependency_operator: Property = Property(name="operator", type=StringType)
assignment6_model_BinaryDependency.attributes={assignment6_model_BinaryDependency_operator}

# assignment6_model_IsSelectedDependency class attributes and methods

# UnaryDependency class attributes and methods

# assignment6_model_IntegerValueDependency class attributes and methods
assignment6_model_IntegerValueDependency_value: Property = Property(name="value", type=IntegerType)
assignment6_model_IntegerValueDependency.attributes={assignment6_model_IntegerValueDependency_value}

# Relationships
features0: BinaryAssociation = BinaryAssociation(
    name="features0",
    ends={
        Property(name="assignment6_model_Feature", type=assignment6_model_Configurator, multiplicity=Multiplicity(1, 1)),
        Property(name="assignment6_model_Configurator", type=assignment6_model_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
features11: BinaryAssociation = BinaryAssociation(
    name="features11",
    ends={
        Property(name="assignment6_model_SimpleFeature", type=assignment6_model_Group, multiplicity=Multiplicity(1, 1)),
        Property(name="assignment6_model_Group12", type=assignment6_model_SimpleFeature, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
groups1: BinaryAssociation = BinaryAssociation(
    name="groups1",
    ends={
        Property(name="assignment6_model_Group", type=assignment6_model_Configurator, multiplicity=Multiplicity(1, 1)),
        Property(name="assignment6_model_Configurator2", type=assignment6_model_Group, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
features4: BinaryAssociation = BinaryAssociation(
    name="features4",
    ends={
        Property(name="assignment6_model_Feature5", type=assignment6_model_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="assignment6_model_Feature3", type=assignment6_model_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
groups6: BinaryAssociation = BinaryAssociation(
    name="groups6",
    ends={
        Property(name="assignment6_model_Group8", type=assignment6_model_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="assignment6_model_Feature7", type=assignment6_model_Group, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dependencies9: BinaryAssociation = BinaryAssociation(
    name="dependencies9",
    ends={
        Property(name="assignment6_model_Dependency", type=assignment6_model_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="assignment6_model_Feature10", type=assignment6_model_Dependency, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target20: BinaryAssociation = BinaryAssociation(
    name="target20",
    ends={
        Property(name="assignment6_model_IntegerFeature", type=assignment6_model_IntegerValueDependency, multiplicity=Multiplicity(1, 1)),
        Property(name="assignment6_model_IntegerValueDependency", type=assignment6_model_IntegerFeature, multiplicity=Multiplicity(1, 1))
    }
)
rightHand13: BinaryAssociation = BinaryAssociation(
    name="rightHand13",
    ends={
        Property(name="assignment6_model_Dependency14", type=assignment6_model_BinaryDependency, multiplicity=Multiplicity(1, 1)),
        Property(name="assignment6_model_BinaryDependency", type=assignment6_model_Dependency, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
leftHand15: BinaryAssociation = BinaryAssociation(
    name="leftHand15",
    ends={
        Property(name="assignment6_model_Dependency17", type=assignment6_model_BinaryDependency, multiplicity=Multiplicity(1, 1)),
        Property(name="assignment6_model_BinaryDependency16", type=assignment6_model_Dependency, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
target18: BinaryAssociation = BinaryAssociation(
    name="target18",
    ends={
        Property(name="assignment6_model_Feature19", type=assignment6_model_IsSelectedDependency, multiplicity=Multiplicity(1, 1)),
        Property(name="assignment6_model_IsSelectedDependency", type=assignment6_model_Feature, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_assignment6_model_IntegerFeature_Feature = Generalization(general=Feature, specific=assignment6_model_IntegerFeature)
gen_assignment6_model_SimpleFeature_Feature = Generalization(general=Feature, specific=assignment6_model_SimpleFeature)
gen_assignment6_model_UnaryDependency_Dependency = Generalization(general=Dependency, specific=assignment6_model_UnaryDependency)
gen_assignment6_model_BinaryDependency_Dependency = Generalization(general=Dependency, specific=assignment6_model_BinaryDependency)
gen_assignment6_model_IsSelectedDependency_UnaryDependency = Generalization(general=UnaryDependency, specific=assignment6_model_IsSelectedDependency)
gen_assignment6_model_IntegerValueDependency_UnaryDependency = Generalization(general=UnaryDependency, specific=assignment6_model_IntegerValueDependency)

# Domain Model
domain_model = DomainModel(
    name="assignment6_model",
    types={assignment6_model_Configurator, assignment6_model_Feature, assignment6_model_IntegerFeature, assignment6_model_Group, assignment6_model_Dependency, assignment6_model_SimpleFeature, Feature, assignment6_model_UnaryDependency, Dependency, assignment6_model_BinaryDependency, assignment6_model_IsSelectedDependency, UnaryDependency, assignment6_model_IntegerValueDependency, GroupType, BinaryOperator},
    associations={features0, features11, groups1, features4, groups6, dependencies9, target20, rightHand13, leftHand15, target18},
    generalizations={gen_assignment6_model_IntegerFeature_Feature, gen_assignment6_model_SimpleFeature_Feature, gen_assignment6_model_UnaryDependency_Dependency, gen_assignment6_model_BinaryDependency_Dependency, gen_assignment6_model_IsSelectedDependency_UnaryDependency, gen_assignment6_model_IntegerValueDependency_UnaryDependency},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)