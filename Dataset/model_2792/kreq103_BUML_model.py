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
            EnumerationLiteral(name="EEnumLiteral0"),
			EnumerationLiteral(name="Transiform"),
			EnumerationLiteral(name="Check_Verify_Validate"),
			EnumerationLiteral(name="Control"),
			EnumerationLiteral(name="Decide"),
			EnumerationLiteral(name="Measure"),
			EnumerationLiteral(name="Store"),
			EnumerationLiteral(name="Wait")
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

RequirementOrigin: Enumeration = Enumeration(
    name="RequirementOrigin",
    literals={
            EnumerationLiteral(name="DesignChoise_induced"),
			EnumerationLiteral(name="Derived"),
			EnumerationLiteral(name="Originating")
    }
)

ComponentType: Enumeration = Enumeration(
    name="ComponentType",
    literals={
            EnumerationLiteral(name="Process"),
			EnumerationLiteral(name="Activity"),
			EnumerationLiteral(name="Serrvice"),
			EnumerationLiteral(name="Actor"),
			EnumerationLiteral(name="Organization_Unit"),
			EnumerationLiteral(name="Site"),
			EnumerationLiteral(name="Role"),
			EnumerationLiteral(name="Physical_component"),
			EnumerationLiteral(name="Logical_component"),
			EnumerationLiteral(name="System"),
			EnumerationLiteral(name="Operational_system"),
			EnumerationLiteral(name="Information_system"),
			EnumerationLiteral(name="Tool"),
			EnumerationLiteral(name="Not_yet_desighed"),
			EnumerationLiteral(name="Other")
    }
)

# Classes
kreq103_Gggg = Class(name="kreq103::Gggg")
kreq103_Bbbb = Class(name="kreq103::Bbbb")
kreq103_Cccc = Class(name="kreq103::Cccc")
kreq103_Ffff = Class(name="kreq103::Ffff")

# kreq103_Gggg class attributes and methods
kreq103_Gggg_id: Property = Property(name="id", type=StringType)
kreq103_Gggg.attributes={kreq103_Gggg_id}

# kreq103_Bbbb class attributes and methods

# kreq103_Cccc class attributes and methods
kreq103_Cccc_id: Property = Property(name="id", type=StringType)
kreq103_Cccc.attributes={kreq103_Cccc_id}

# kreq103_Ffff class attributes and methods
kreq103_Ffff_id: Property = Property(name="id", type=StringType)
kreq103_Ffff.attributes={kreq103_Ffff_id}

# Relationships
cs0: BinaryAssociation = BinaryAssociation(
    name="cs0",
    ends={
        Property(name="kreq103_Bbbb", type=kreq103_Cccc, multiplicity=Multiplicity(1, 9999), is_composite=True),
        Property(name="kreq103_Cccc", type=kreq103_Bbbb, multiplicity=Multiplicity(1, 1))
    }
)
gs1: BinaryAssociation = BinaryAssociation(
    name="gs1",
    ends={
        Property(name="kreq103_Gggg", type=kreq103_Bbbb, multiplicity=Multiplicity(1, 1)),
        Property(name="kreq103_Bbbb2", type=kreq103_Gggg, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subFs6: BinaryAssociation = BinaryAssociation(
    name="subFs6",
    ends={
        Property(name="kreq103_Ffff7", type=kreq103_Ffff, multiplicity=Multiplicity(1, 1)),
        Property(name="kreq103_Ffff5", type=kreq103_Ffff, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fs3: BinaryAssociation = BinaryAssociation(
    name="fs3",
    ends={
        Property(name="kreq103_Ffff", type=kreq103_Cccc, multiplicity=Multiplicity(1, 1)),
        Property(name="kreq103_Cccc4", type=kreq103_Ffff, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="kreq103",
    types={kreq103_Gggg, kreq103_Bbbb, kreq103_Cccc, kreq103_Ffff, BasicFlowTransformationType, ComponentPosition, CategoryType, RequirementOrigin, ComponentType},
    associations={cs0, gs1, subFs6, fs3},
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