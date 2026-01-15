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
ScopeKind: Enumeration = Enumeration(
    name="ScopeKind",
    literals={
            EnumerationLiteral(name="instance"),
			EnumerationLiteral(name="classifier")
    }
)

# Classes
uml_15_to_20_associationEndToProperty_Attribute = Class(name="uml::15::to::20::associationEndToProperty::Attribute")
StructuralFeature = Class(name="StructuralFeature")
uml_15_to_20_associationEndToProperty_Operation = Class(name="uml::15::to::20::associationEndToProperty::Operation")
uml_15_to_20_associationEndToProperty_Model = Class(name="uml::15::to::20::associationEndToProperty::Model")
uml_15_to_20_associationEndToProperty_Class = Class(name="uml::15::to::20::associationEndToProperty::Class")
uml_15_to_20_associationEndToProperty_Association = Class(name="uml::15::to::20::associationEndToProperty::Association")
uml_15_to_20_associationEndToProperty_StructuralFeature = Class(name="uml::15::to::20::associationEndToProperty::StructuralFeature", is_abstract=True)
uml_15_to_20_associationEndToProperty_AssociationEnd = Class(name="uml::15::to::20::associationEndToProperty::AssociationEnd")

# uml_15_to_20_associationEndToProperty_Attribute class attributes and methods

# StructuralFeature class attributes and methods

# uml_15_to_20_associationEndToProperty_Operation class attributes and methods

# uml_15_to_20_associationEndToProperty_Model class attributes and methods

# uml_15_to_20_associationEndToProperty_Class class attributes and methods

# uml_15_to_20_associationEndToProperty_Association class attributes and methods

# uml_15_to_20_associationEndToProperty_StructuralFeature class attributes and methods
uml_15_to_20_associationEndToProperty_StructuralFeature_ownerScope: Property = Property(name="ownerScope", type=StringType)
uml_15_to_20_associationEndToProperty_StructuralFeature_targetScope: Property = Property(name="targetScope", type=StringType)
uml_15_to_20_associationEndToProperty_StructuralFeature.attributes={uml_15_to_20_associationEndToProperty_StructuralFeature_targetScope, uml_15_to_20_associationEndToProperty_StructuralFeature_ownerScope}

# uml_15_to_20_associationEndToProperty_AssociationEnd class attributes and methods
uml_15_to_20_associationEndToProperty_AssociationEnd_isNavigable: Property = Property(name="isNavigable", type=BooleanType)
uml_15_to_20_associationEndToProperty_AssociationEnd.attributes={uml_15_to_20_associationEndToProperty_AssociationEnd_isNavigable}

# Relationships
association9: BinaryAssociation = BinaryAssociation(
    name="association9",
    ends={
        Property(name="Association", type=uml_15_to_20_associationEndToProperty_AssociationEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="connections", type=uml_15_to_20_associationEndToProperty_Association, multiplicity=Multiplicity(1, 1))
    }
)
classes0: BinaryAssociation = BinaryAssociation(
    name="classes0",
    ends={
        Property(name="uml_15_to_20_associationEndToProperty_Class", type=uml_15_to_20_associationEndToProperty_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_15_to_20_associationEndToProperty_Model", type=uml_15_to_20_associationEndToProperty_Class, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
associations1: BinaryAssociation = BinaryAssociation(
    name="associations1",
    ends={
        Property(name="uml_15_to_20_associationEndToProperty_Association", type=uml_15_to_20_associationEndToProperty_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_15_to_20_associationEndToProperty_Model2", type=uml_15_to_20_associationEndToProperty_Association, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
features3: BinaryAssociation = BinaryAssociation(
    name="features3",
    ends={
        Property(name="uml_15_to_20_associationEndToProperty_StructuralFeature", type=uml_15_to_20_associationEndToProperty_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_15_to_20_associationEndToProperty_Class4", type=uml_15_to_20_associationEndToProperty_StructuralFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
associations5: BinaryAssociation = BinaryAssociation(
    name="associations5",
    ends={
        Property(name="AssociationEnd", type=uml_15_to_20_associationEndToProperty_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="participant", type=uml_15_to_20_associationEndToProperty_AssociationEnd, multiplicity=Multiplicity(0, 9999))
    }
)
connections6: BinaryAssociation = BinaryAssociation(
    name="connections6",
    ends={
        Property(name="AssociationEnd7", type=uml_15_to_20_associationEndToProperty_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="association", type=uml_15_to_20_associationEndToProperty_AssociationEnd, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
participant8: BinaryAssociation = BinaryAssociation(
    name="participant8",
    ends={
        Property(name="Class", type=uml_15_to_20_associationEndToProperty_AssociationEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="associations", type=uml_15_to_20_associationEndToProperty_Class, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_uml_15_to_20_associationEndToProperty_Attribute_StructuralFeature = Generalization(general=StructuralFeature, specific=uml_15_to_20_associationEndToProperty_Attribute)
gen_uml_15_to_20_associationEndToProperty_Operation_StructuralFeature = Generalization(general=StructuralFeature, specific=uml_15_to_20_associationEndToProperty_Operation)

# Domain Model
domain_model = DomainModel(
    name="uml_15_to_20_associationEndToProperty",
    types={uml_15_to_20_associationEndToProperty_Attribute, StructuralFeature, uml_15_to_20_associationEndToProperty_Operation, uml_15_to_20_associationEndToProperty_Model, uml_15_to_20_associationEndToProperty_Class, uml_15_to_20_associationEndToProperty_Association, uml_15_to_20_associationEndToProperty_StructuralFeature, uml_15_to_20_associationEndToProperty_AssociationEnd, ScopeKind},
    associations={association9, classes0, associations1, features3, associations5, connections6, participant8},
    generalizations={gen_uml_15_to_20_associationEndToProperty_Attribute_StructuralFeature, gen_uml_15_to_20_associationEndToProperty_Operation_StructuralFeature},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)