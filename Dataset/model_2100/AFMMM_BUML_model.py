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
afmmm_CrossTreeConstraint = Class(name="afmmm::CrossTreeConstraint")
afmmm_Relation = Class(name="afmmm::Relation", is_abstract=True)
afmmm_Attribute = Class(name="afmmm::Attribute")
afmmm_AttributedFeatureDiagram = Class(name="afmmm::AttributedFeatureDiagram")
afmmm_Feature = Class(name="afmmm::Feature")
afmmm_Domain = Class(name="afmmm::Domain", is_abstract=True)
afmmm_Boolean = Class(name="afmmm::Boolean")
Domain = Class(name="Domain")
afmmm_Integer = Class(name="afmmm::Integer")
afmmm_Real = Class(name="afmmm::Real")
afmmm_Enum = Class(name="afmmm::Enum")
afmmm_AttributedFeatureModel = Class(name="afmmm::AttributedFeatureModel")
afmmm_Mandatory = Class(name="afmmm::Mandatory")
Relation = Class(name="Relation")
afmmm_Optional = Class(name="afmmm::Optional")
afmmm_Mutex = Class(name="afmmm::Mutex")
afmmm_XOr = Class(name="afmmm::XOr")
afmmm_Or = Class(name="afmmm::Or")
afmmm_EClass0 = Class(name="afmmm::EClass0")

# afmmm_CrossTreeConstraint class attributes and methods

# afmmm_Relation class attributes and methods

# afmmm_Attribute class attributes and methods
afmmm_Attribute_name: Property = Property(name="name", type=StringType)
afmmm_Attribute.attributes={afmmm_Attribute_name}

# afmmm_AttributedFeatureDiagram class attributes and methods

# afmmm_Feature class attributes and methods
afmmm_Feature_name: Property = Property(name="name", type=StringType)
afmmm_Feature.attributes={afmmm_Feature_name}

# afmmm_Domain class attributes and methods

# afmmm_Boolean class attributes and methods

# Domain class attributes and methods

# afmmm_Integer class attributes and methods

# afmmm_Real class attributes and methods

# afmmm_Enum class attributes and methods
afmmm_Enum_literals: Property = Property(name="literals", type=StringType)
afmmm_Enum.attributes={afmmm_Enum_literals}

# afmmm_AttributedFeatureModel class attributes and methods

# afmmm_Mandatory class attributes and methods

# Relation class attributes and methods

# afmmm_Optional class attributes and methods

# afmmm_Mutex class attributes and methods

# afmmm_XOr class attributes and methods

# afmmm_Or class attributes and methods

# afmmm_EClass0 class attributes and methods

# Relationships
features0: BinaryAssociation = BinaryAssociation(
    name="features0",
    ends={
        Property(name="afmmm_AttributedFeatureDiagram", type=afmmm_Feature, multiplicity=Multiplicity(1, 9999), is_composite=True),
        Property(name="afmmm_Feature", type=afmmm_AttributedFeatureDiagram, multiplicity=Multiplicity(1, 1))
    }
)
root1: BinaryAssociation = BinaryAssociation(
    name="root1",
    ends={
        Property(name="afmmm_Feature3", type=afmmm_AttributedFeatureDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="afmmm_AttributedFeatureDiagram2", type=afmmm_Feature, multiplicity=Multiplicity(1, 1))
    }
)
readableConstraints4: BinaryAssociation = BinaryAssociation(
    name="readableConstraints4",
    ends={
        Property(name="afmmm_CrossTreeConstraint", type=afmmm_AttributedFeatureDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="afmmm_AttributedFeatureDiagram5", type=afmmm_CrossTreeConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relations6: BinaryAssociation = BinaryAssociation(
    name="relations6",
    ends={
        Property(name="afmmm_Relation", type=afmmm_AttributedFeatureDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="afmmm_AttributedFeatureDiagram7", type=afmmm_Relation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes8: BinaryAssociation = BinaryAssociation(
    name="attributes8",
    ends={
        Property(name="afmmm_Attribute", type=afmmm_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="afmmm_Feature9", type=afmmm_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
diagram16: BinaryAssociation = BinaryAssociation(
    name="diagram16",
    ends={
        Property(name="afmmm_AttributedFeatureDiagram17", type=afmmm_AttributedFeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="afmmm_AttributedFeatureModel", type=afmmm_AttributedFeatureDiagram, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parent10: BinaryAssociation = BinaryAssociation(
    name="parent10",
    ends={
        Property(name="afmmm_Feature12", type=afmmm_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="afmmm_Relation11", type=afmmm_Feature, multiplicity=Multiplicity(1, 1))
    }
)
children13: BinaryAssociation = BinaryAssociation(
    name="children13",
    ends={
        Property(name="afmmm_Feature15", type=afmmm_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="afmmm_Relation14", type=afmmm_Feature, multiplicity=Multiplicity(1, 9999))
    }
)
constraint18: BinaryAssociation = BinaryAssociation(
    name="constraint18",
    ends={
        Property(name="afmmm_CrossTreeConstraint20", type=afmmm_AttributedFeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="afmmm_AttributedFeatureModel19", type=afmmm_CrossTreeConstraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
domains21: BinaryAssociation = BinaryAssociation(
    name="domains21",
    ends={
        Property(name="afmmm_Domain", type=afmmm_AttributedFeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="afmmm_AttributedFeatureModel22", type=afmmm_Domain, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
domain23: BinaryAssociation = BinaryAssociation(
    name="domain23",
    ends={
        Property(name="afmmm_Domain25", type=afmmm_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="afmmm_Attribute24", type=afmmm_Domain, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_afmmm_Or_Relation = Generalization(general=Relation, specific=afmmm_Or)
gen_afmmm_Boolean_Domain = Generalization(general=Domain, specific=afmmm_Boolean)
gen_afmmm_Integer_Domain = Generalization(general=Domain, specific=afmmm_Integer)
gen_afmmm_Real_Domain = Generalization(general=Domain, specific=afmmm_Real)
gen_afmmm_Enum_Domain = Generalization(general=Domain, specific=afmmm_Enum)
gen_afmmm_Mandatory_Relation = Generalization(general=Relation, specific=afmmm_Mandatory)
gen_afmmm_Optional_Relation = Generalization(general=Relation, specific=afmmm_Optional)
gen_afmmm_Mutex_Relation = Generalization(general=Relation, specific=afmmm_Mutex)
gen_afmmm_XOr_Relation = Generalization(general=Relation, specific=afmmm_XOr)

# Domain Model
domain_model = DomainModel(
    name="afmmm",
    types={afmmm_CrossTreeConstraint, afmmm_Relation, afmmm_Attribute, afmmm_AttributedFeatureDiagram, afmmm_Feature, afmmm_Domain, afmmm_Boolean, Domain, afmmm_Integer, afmmm_Real, afmmm_Enum, afmmm_AttributedFeatureModel, afmmm_Mandatory, Relation, afmmm_Optional, afmmm_Mutex, afmmm_XOr, afmmm_Or, afmmm_EClass0},
    associations={features0, root1, readableConstraints4, relations6, attributes8, diagram16, parent10, children13, constraint18, domains21, domain23},
    generalizations={gen_afmmm_Or_Relation, gen_afmmm_Boolean_Domain, gen_afmmm_Integer_Domain, gen_afmmm_Real_Domain, gen_afmmm_Enum_Domain, gen_afmmm_Mandatory_Relation, gen_afmmm_Optional_Relation, gen_afmmm_Mutex_Relation, gen_afmmm_XOr_Relation},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)