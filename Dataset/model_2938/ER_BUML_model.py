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
ER_ERModel = Class(name="ER::ERModel")
Element = Class(name="Element")
ER_EntityType = Class(name="ER::EntityType")
ER_Feature = Class(name="ER::Feature", is_abstract=True)
ER_Attribute = Class(name="ER::Attribute")
Feature = Class(name="Feature")
ER_WeakReference = Class(name="ER::WeakReference")
Reference = Class(name="Reference")
ER_StrongReference = Class(name="ER::StrongReference")
ER_Element = Class(name="ER::Element", is_abstract=True)
ER_Reference = Class(name="ER::Reference", is_abstract=True)

# ER_ERModel class attributes and methods

# Element class attributes and methods

# ER_EntityType class attributes and methods

# ER_Feature class attributes and methods

# ER_Attribute class attributes and methods
ER_Attribute_type: Property = Property(name="type", type=StringType)
ER_Attribute.attributes={ER_Attribute_type}

# Feature class attributes and methods

# ER_WeakReference class attributes and methods

# Reference class attributes and methods

# ER_StrongReference class attributes and methods

# ER_Element class attributes and methods
ER_Element_name: Property = Property(name="name", type=StringType)
ER_Element.attributes={ER_Element_name}

# ER_Reference class attributes and methods

# Relationships
entities0: BinaryAssociation = BinaryAssociation(
    name="entities0",
    ends={
        Property(name="ER_EntityType", type=ER_ERModel, multiplicity=Multiplicity(1, 1)),
        Property(name="ER_ERModel", type=ER_EntityType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
features1: BinaryAssociation = BinaryAssociation(
    name="features1",
    ends={
        Property(name="ER_Feature", type=ER_EntityType, multiplicity=Multiplicity(1, 1)),
        Property(name="ER_EntityType2", type=ER_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type3: BinaryAssociation = BinaryAssociation(
    name="type3",
    ends={
        Property(name="ER_EntityType4", type=ER_Reference, multiplicity=Multiplicity(1, 1)),
        Property(name="ER_Reference", type=ER_EntityType, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_ER_ERModel_Element = Generalization(general=Element, specific=ER_ERModel)
gen_ER_EntityType_Element = Generalization(general=Element, specific=ER_EntityType)
gen_ER_Feature_Element = Generalization(general=Element, specific=ER_Feature)
gen_ER_Attribute_Feature = Generalization(general=Feature, specific=ER_Attribute)
gen_ER_WeakReference_Reference = Generalization(general=Reference, specific=ER_WeakReference)
gen_ER_StrongReference_Reference = Generalization(general=Reference, specific=ER_StrongReference)
gen_ER_Reference_Feature = Generalization(general=Feature, specific=ER_Reference)

# Domain Model
domain_model = DomainModel(
    name="ER",
    types={ER_ERModel, Element, ER_EntityType, ER_Feature, ER_Attribute, Feature, ER_WeakReference, Reference, ER_StrongReference, ER_Element, ER_Reference},
    associations={entities0, features1, type3},
    generalizations={gen_ER_ERModel_Element, gen_ER_EntityType_Element, gen_ER_Feature_Element, gen_ER_Attribute_Feature, gen_ER_WeakReference_Reference, gen_ER_StrongReference_Reference, gen_ER_Reference_Feature},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)