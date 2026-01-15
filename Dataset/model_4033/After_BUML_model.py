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
AggregationKind: Enumeration = Enumeration(
    name="AggregationKind",
    literals={
            EnumerationLiteral(name="none"),
			EnumerationLiteral(name="shared"),
			EnumerationLiteral(name="composite")
    }
)

ScopeKind: Enumeration = Enumeration(
    name="ScopeKind",
    literals={
            EnumerationLiteral(name="instance"),
			EnumerationLiteral(name="classifier")
    }
)

# Classes
uml_15_to_20_associationEndToProperty_Model = Class(name="uml::15::to::20::associationEndToProperty::Model")
uml_15_to_20_associationEndToProperty_Class = Class(name="uml::15::to::20::associationEndToProperty::Class")
uml_15_to_20_associationEndToProperty_Association = Class(name="uml::15::to::20::associationEndToProperty::Association")
uml_15_to_20_associationEndToProperty_Property = Class(name="uml::15::to::20::associationEndToProperty::Property")
uml_15_to_20_associationEndToProperty_Operation = Class(name="uml::15::to::20::associationEndToProperty::Operation")
uml_15_to_20_associationEndToProperty_StructuralFeature = Class(name="uml::15::to::20::associationEndToProperty::StructuralFeature", is_abstract=True)
StructuralFeature = Class(name="StructuralFeature")

# uml_15_to_20_associationEndToProperty_Model class attributes and methods

# uml_15_to_20_associationEndToProperty_Class class attributes and methods

# uml_15_to_20_associationEndToProperty_Association class attributes and methods

# uml_15_to_20_associationEndToProperty_Property class attributes and methods

# uml_15_to_20_associationEndToProperty_Operation class attributes and methods

# uml_15_to_20_associationEndToProperty_StructuralFeature class attributes and methods
uml_15_to_20_associationEndToProperty_StructuralFeature_isStatic: Property = Property(name="isStatic", type=BooleanType)
uml_15_to_20_associationEndToProperty_StructuralFeature.attributes={uml_15_to_20_associationEndToProperty_StructuralFeature_isStatic}

# StructuralFeature class attributes and methods

# Relationships
association11: BinaryAssociation = BinaryAssociation(
    name="association11",
    ends={
        Property(name="Association", type=uml_15_to_20_associationEndToProperty_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="memberEnds", type=uml_15_to_20_associationEndToProperty_Association, multiplicity=Multiplicity(1, 1))
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
attributes3: BinaryAssociation = BinaryAssociation(
    name="attributes3",
    ends={
        Property(name="Property", type=uml_15_to_20_associationEndToProperty_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="class", type=uml_15_to_20_associationEndToProperty_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operations4: BinaryAssociation = BinaryAssociation(
    name="operations4",
    ends={
        Property(name="uml_15_to_20_associationEndToProperty_Operation", type=uml_15_to_20_associationEndToProperty_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_15_to_20_associationEndToProperty_Class5", type=uml_15_to_20_associationEndToProperty_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
memberEnds6: BinaryAssociation = BinaryAssociation(
    name="memberEnds6",
    ends={
        Property(name="Property7", type=uml_15_to_20_associationEndToProperty_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="association", type=uml_15_to_20_associationEndToProperty_Property, multiplicity=Multiplicity(2, 9999))
    }
)
navigableEnds8: BinaryAssociation = BinaryAssociation(
    name="navigableEnds8",
    ends={
        Property(name="uml_15_to_20_associationEndToProperty_Property", type=uml_15_to_20_associationEndToProperty_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_15_to_20_associationEndToProperty_Association9", type=uml_15_to_20_associationEndToProperty_Property, multiplicity=Multiplicity(0, 9999))
    }
)
class10: BinaryAssociation = BinaryAssociation(
    name="class10",
    ends={
        Property(name="Class", type=uml_15_to_20_associationEndToProperty_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="attributes", type=uml_15_to_20_associationEndToProperty_Class, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_uml_15_to_20_associationEndToProperty_Operation_StructuralFeature = Generalization(general=StructuralFeature, specific=uml_15_to_20_associationEndToProperty_Operation)
gen_uml_15_to_20_associationEndToProperty_Property_StructuralFeature = Generalization(general=StructuralFeature, specific=uml_15_to_20_associationEndToProperty_Property)

# Domain Model
domain_model = DomainModel(
    name="uml_15_to_20_associationEndToProperty",
    types={uml_15_to_20_associationEndToProperty_Model, uml_15_to_20_associationEndToProperty_Class, uml_15_to_20_associationEndToProperty_Association, uml_15_to_20_associationEndToProperty_Property, uml_15_to_20_associationEndToProperty_Operation, uml_15_to_20_associationEndToProperty_StructuralFeature, StructuralFeature, AggregationKind, ScopeKind},
    associations={association11, classes0, associations1, attributes3, operations4, memberEnds6, navigableEnds8, class10},
    generalizations={gen_uml_15_to_20_associationEndToProperty_Operation_StructuralFeature, gen_uml_15_to_20_associationEndToProperty_Property_StructuralFeature},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)