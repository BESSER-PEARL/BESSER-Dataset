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
simple_OO_concept_Package = Class(name="simple::OO::concept::Package")
NamedElement = Class(name="NamedElement")
simple_OO_concept_Class = Class(name="simple::OO::concept::Class")
simple_OO_concept_Dependency = Class(name="simple::OO::concept::Dependency")
simple_OO_concept_NamedElement = Class(name="simple::OO::concept::NamedElement", is_abstract=True)
simple_OO_concept_Parameter = Class(name="simple::OO::concept::Parameter")
simple_OO_concept_Behavior = Class(name="simple::OO::concept::Behavior")
Class_ = Class(name="Class")
simple_OO_concept_Attribute = Class(name="simple::OO::concept::Attribute")
simple_OO_concept_Operation = Class(name="simple::OO::concept::Operation")
simple_OO_concept_Feature = Class(name="simple::OO::concept::Feature", is_abstract=True)
Feature = Class(name="Feature")

# simple_OO_concept_Package class attributes and methods

# NamedElement class attributes and methods

# simple_OO_concept_Class class attributes and methods
simple_OO_concept_Class_isAbstract: Property = Property(name="isAbstract", type=BooleanType)
simple_OO_concept_Class.attributes={simple_OO_concept_Class_isAbstract}

# simple_OO_concept_Dependency class attributes and methods

# simple_OO_concept_NamedElement class attributes and methods
simple_OO_concept_NamedElement_name: Property = Property(name="name", type=StringType)
simple_OO_concept_NamedElement.attributes={simple_OO_concept_NamedElement_name}

# simple_OO_concept_Parameter class attributes and methods

# simple_OO_concept_Behavior class attributes and methods

# Class class attributes and methods

# simple_OO_concept_Attribute class attributes and methods

# simple_OO_concept_Operation class attributes and methods

# simple_OO_concept_Feature class attributes and methods
simple_OO_concept_Feature_isPublic: Property = Property(name="isPublic", type=BooleanType)
simple_OO_concept_Feature_isProtected: Property = Property(name="isProtected", type=BooleanType)
simple_OO_concept_Feature_isPrivate: Property = Property(name="isPrivate", type=BooleanType)
simple_OO_concept_Feature.attributes={simple_OO_concept_Feature_isPublic, simple_OO_concept_Feature_isProtected, simple_OO_concept_Feature_isPrivate}

# Feature class attributes and methods

# Relationships
classes0: BinaryAssociation = BinaryAssociation(
    name="classes0",
    ends={
        Property(name="simple_OO_concept_Class", type=simple_OO_concept_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="simple_OO_concept_Package", type=simple_OO_concept_Class, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dependencies1: BinaryAssociation = BinaryAssociation(
    name="dependencies1",
    ends={
        Property(name="simple_OO_concept_Dependency", type=simple_OO_concept_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="simple_OO_concept_Package2", type=simple_OO_concept_Dependency, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters18: BinaryAssociation = BinaryAssociation(
    name="parameters18",
    ends={
        Property(name="simple_OO_concept_Parameter", type=simple_OO_concept_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="simple_OO_concept_Operation19", type=simple_OO_concept_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
method20: BinaryAssociation = BinaryAssociation(
    name="method20",
    ends={
        Property(name="simple_OO_concept_Behavior", type=simple_OO_concept_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="simple_OO_concept_Operation21", type=simple_OO_concept_Behavior, multiplicity=Multiplicity(0, 9999))
    }
)
partype22: BinaryAssociation = BinaryAssociation(
    name="partype22",
    ends={
        Property(name="simple_OO_concept_Class24", type=simple_OO_concept_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="simple_OO_concept_Parameter23", type=simple_OO_concept_Class, multiplicity=Multiplicity(0, 1))
    }
)
supplier3: BinaryAssociation = BinaryAssociation(
    name="supplier3",
    ends={
        Property(name="simple_OO_concept_NamedElement", type=simple_OO_concept_Dependency, multiplicity=Multiplicity(1, 1)),
        Property(name="simple_OO_concept_Dependency4", type=simple_OO_concept_NamedElement, multiplicity=Multiplicity(1, 9999))
    }
)
client5: BinaryAssociation = BinaryAssociation(
    name="client5",
    ends={
        Property(name="simple_OO_concept_NamedElement7", type=simple_OO_concept_Dependency, multiplicity=Multiplicity(1, 1)),
        Property(name="simple_OO_concept_Dependency6", type=simple_OO_concept_NamedElement, multiplicity=Multiplicity(1, 9999))
    }
)
attributes8: BinaryAssociation = BinaryAssociation(
    name="attributes8",
    ends={
        Property(name="simple_OO_concept_Attribute", type=simple_OO_concept_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="simple_OO_concept_Class9", type=simple_OO_concept_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operations10: BinaryAssociation = BinaryAssociation(
    name="operations10",
    ends={
        Property(name="simple_OO_concept_Operation", type=simple_OO_concept_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="simple_OO_concept_Class11", type=simple_OO_concept_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parents13: BinaryAssociation = BinaryAssociation(
    name="parents13",
    ends={
        Property(name="simple_OO_concept_Class14", type=simple_OO_concept_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="simple_OO_concept_Class12", type=simple_OO_concept_Class, multiplicity=Multiplicity(0, 9999))
    }
)
atttype15: BinaryAssociation = BinaryAssociation(
    name="atttype15",
    ends={
        Property(name="simple_OO_concept_Class17", type=simple_OO_concept_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="simple_OO_concept_Attribute16", type=simple_OO_concept_Class, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_simple_OO_concept_Package_NamedElement = Generalization(general=NamedElement, specific=simple_OO_concept_Package)
gen_simple_OO_concept_Behavior_Class = Generalization(general=Class_, specific=simple_OO_concept_Behavior)
gen_simple_OO_concept_Class_NamedElement = Generalization(general=NamedElement, specific=simple_OO_concept_Class)
gen_simple_OO_concept_Attribute_NamedElement = Generalization(general=NamedElement, specific=simple_OO_concept_Attribute)
gen_simple_OO_concept_Attribute_Feature = Generalization(general=Feature, specific=simple_OO_concept_Attribute)
gen_simple_OO_concept_Operation_NamedElement = Generalization(general=NamedElement, specific=simple_OO_concept_Operation)
gen_simple_OO_concept_Operation_Feature = Generalization(general=Feature, specific=simple_OO_concept_Operation)

# Domain Model
domain_model = DomainModel(
    name="simple_OO_concept",
    types={simple_OO_concept_Package, NamedElement, simple_OO_concept_Class, simple_OO_concept_Dependency, simple_OO_concept_NamedElement, simple_OO_concept_Parameter, simple_OO_concept_Behavior, Class_, simple_OO_concept_Attribute, simple_OO_concept_Operation, simple_OO_concept_Feature, Feature},
    associations={classes0, dependencies1, parameters18, method20, partype22, supplier3, client5, attributes8, operations10, parents13, atttype15},
    generalizations={gen_simple_OO_concept_Package_NamedElement, gen_simple_OO_concept_Behavior_Class, gen_simple_OO_concept_Class_NamedElement, gen_simple_OO_concept_Attribute_NamedElement, gen_simple_OO_concept_Attribute_Feature, gen_simple_OO_concept_Operation_NamedElement, gen_simple_OO_concept_Operation_Feature},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)