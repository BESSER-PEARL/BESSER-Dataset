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
BasicFlowTransformationType: Enumeration = Enumeration(
    name="BasicFlowTransformationType",
    literals={
            EnumerationLiteral(name="Decide"),
			EnumerationLiteral(name="EEnumLiteral0"),
			EnumerationLiteral(name="Transiform"),
			EnumerationLiteral(name="Check_Verify_Validate"),
			EnumerationLiteral(name="Control"),
			EnumerationLiteral(name="Measure"),
			EnumerationLiteral(name="Store"),
			EnumerationLiteral(name="Wait")
    }
)

RequirementOrigin: Enumeration = Enumeration(
    name="RequirementOrigin",
    literals={
            EnumerationLiteral(name="Derived"),
			EnumerationLiteral(name="Originating"),
			EnumerationLiteral(name="DesignChoise_induced")
    }
)

ComponentPosition: Enumeration = Enumeration(
    name="ComponentPosition",
    literals={
            EnumerationLiteral(name="Not_yet_defined"),
			EnumerationLiteral(name="Local"),
			EnumerationLiteral(name="Environmental_context")
    }
)

CategoryType: Enumeration = Enumeration(
    name="CategoryType",
    literals={
            EnumerationLiteral(name="Functional"),
			EnumerationLiteral(name="Non_Functional"),
			EnumerationLiteral(name="Operational"),
			EnumerationLiteral(name="VandV"),
			EnumerationLiteral(name="Interface"),
			EnumerationLiteral(name="Constraints")
    }
)

ComponentType: Enumeration = Enumeration(
    name="ComponentType",
    literals={
            EnumerationLiteral(name="Physical_component"),
			EnumerationLiteral(name="Logical_component"),
			EnumerationLiteral(name="System"),
			EnumerationLiteral(name="Operational_system"),
			EnumerationLiteral(name="Information_system"),
			EnumerationLiteral(name="Process"),
			EnumerationLiteral(name="Activity"),
			EnumerationLiteral(name="Serrvice"),
			EnumerationLiteral(name="Actor"),
			EnumerationLiteral(name="Organization_Unit"),
			EnumerationLiteral(name="Site"),
			EnumerationLiteral(name="Role"),
			EnumerationLiteral(name="Tool"),
			EnumerationLiteral(name="Not_yet_desighed"),
			EnumerationLiteral(name="Other")
    }
)

# Classes
kreq210_Bbbb = Class(name="kreq210::Bbbb")
kreq210_Cccc = Class(name="kreq210::Cccc")
kreq210_Gggg = Class(name="kreq210::Gggg")
kreq210_Hhhh = Class(name="kreq210::Hhhh")
kreq210_Mmmm = Class(name="kreq210::Mmmm")
kreq210_Ffff = Class(name="kreq210::Ffff")
kreq210_Llll = Class(name="kreq210::Llll")

# kreq210_Bbbb class attributes and methods

# kreq210_Cccc class attributes and methods
kreq210_Cccc_id: Property = Property(name="id", type=StringType)
kreq210_Cccc.attributes={kreq210_Cccc_id}

# kreq210_Gggg class attributes and methods
kreq210_Gggg_id: Property = Property(name="id", type=StringType)
kreq210_Gggg.attributes={kreq210_Gggg_id}

# kreq210_Hhhh class attributes and methods
kreq210_Hhhh_id: Property = Property(name="id", type=IntegerType)
kreq210_Hhhh.attributes={kreq210_Hhhh_id}

# kreq210_Mmmm class attributes and methods
kreq210_Mmmm_id: Property = Property(name="id", type=StringType)
kreq210_Mmmm.attributes={kreq210_Mmmm_id}

# kreq210_Ffff class attributes and methods
kreq210_Ffff_id: Property = Property(name="id", type=StringType)
kreq210_Ffff.attributes={kreq210_Ffff_id}

# kreq210_Llll class attributes and methods
kreq210_Llll_id: Property = Property(name="id", type=StringType)
kreq210_Llll.attributes={kreq210_Llll_id}

# Relationships
cs0: BinaryAssociation = BinaryAssociation(
    name="cs0",
    ends={
        Property(name="kreq210_Cccc", type=kreq210_Bbbb, multiplicity=Multiplicity(1, 1)),
        Property(name="kreq210_Bbbb", type=kreq210_Cccc, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
gs1: BinaryAssociation = BinaryAssociation(
    name="gs1",
    ends={
        Property(name="kreq210_Gggg", type=kreq210_Bbbb, multiplicity=Multiplicity(1, 1)),
        Property(name="kreq210_Bbbb2", type=kreq210_Gggg, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hs3: BinaryAssociation = BinaryAssociation(
    name="hs3",
    ends={
        Property(name="kreq210_Hhhh", type=kreq210_Bbbb, multiplicity=Multiplicity(1, 1)),
        Property(name="kreq210_Bbbb4", type=kreq210_Hhhh, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ms5: BinaryAssociation = BinaryAssociation(
    name="ms5",
    ends={
        Property(name="kreq210_Mmmm", type=kreq210_Bbbb, multiplicity=Multiplicity(1, 1)),
        Property(name="kreq210_Bbbb6", type=kreq210_Mmmm, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fs7: BinaryAssociation = BinaryAssociation(
    name="fs7",
    ends={
        Property(name="kreq210_Ffff", type=kreq210_Cccc, multiplicity=Multiplicity(1, 1)),
        Property(name="kreq210_Cccc8", type=kreq210_Ffff, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subFs10: BinaryAssociation = BinaryAssociation(
    name="subFs10",
    ends={
        Property(name="kreq210_Ffff11", type=kreq210_Ffff, multiplicity=Multiplicity(1, 1)),
        Property(name="kreq210_Ffff9", type=kreq210_Ffff, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ls12: BinaryAssociation = BinaryAssociation(
    name="ls12",
    ends={
        Property(name="kreq210_Llll", type=kreq210_Gggg, multiplicity=Multiplicity(1, 1)),
        Property(name="kreq210_Gggg13", type=kreq210_Llll, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lcs14: BinaryAssociation = BinaryAssociation(
    name="lcs14",
    ends={
        Property(name="kreq210_Cccc16", type=kreq210_Llll, multiplicity=Multiplicity(1, 1)),
        Property(name="kreq210_Llll15", type=kreq210_Cccc, multiplicity=Multiplicity(0, 1))
    }
)
e017: BinaryAssociation = BinaryAssociation(
    name="e017",
    ends={
        Property(name="kreq210_Hhhh19", type=kreq210_Llll, multiplicity=Multiplicity(1, 1)),
        Property(name="kreq210_Llll18", type=kreq210_Hhhh, multiplicity=Multiplicity(0, 1))
    }
)
ms20: BinaryAssociation = BinaryAssociation(
    name="ms20",
    ends={
        Property(name="kreq210_Mmmm22", type=kreq210_Llll, multiplicity=Multiplicity(1, 1)),
        Property(name="kreq210_Llll21", type=kreq210_Mmmm, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="kreq210",
    types={kreq210_Bbbb, kreq210_Cccc, kreq210_Gggg, kreq210_Hhhh, kreq210_Mmmm, kreq210_Ffff, kreq210_Llll, BasicFlowTransformationType, RequirementOrigin, ComponentPosition, CategoryType, ComponentType},
    associations={cs0, gs1, hs3, ms5, fs7, subFs10, ls12, lcs14, e017, ms20},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)