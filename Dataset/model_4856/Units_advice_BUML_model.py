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
units_av_UnitCarryingElement = Class(name="units::av::UnitCarryingElement")
units_av_Unit = Class(name="units::av::Unit")
units_av_UnitPower = Class(name="units::av::UnitPower")
units_av_UnitLiteral = Class(name="units::av::UnitLiteral")
units_av_Advice = Class(name="units::av::Advice")
units_av_EObject = Class(name="units::av::EObject")
units_av_GlobalScope = Class(name="units::av::GlobalScope")
units_av_PerJoinPointScope = Class(name="units::av::PerJoinPointScope")
units_av_BaseUnit = Class(name="units::av::BaseUnit")
units_av_UnitRepository = Class(name="units::av::UnitRepository")
units_av_UnitMultiplication = Class(name="units::av::UnitMultiplication")
Unit = Class(name="Unit")

# units_av_UnitCarryingElement class attributes and methods
units_av_UnitCarryingElement_unitSpecification: Property = Property(name="unitSpecification", type=StringType)
units_av_UnitCarryingElement.attributes={units_av_UnitCarryingElement_unitSpecification}

# units_av_Unit class attributes and methods

# units_av_UnitPower class attributes and methods
units_av_UnitPower_exponent: Property = Property(name="exponent", type=IntegerType)
units_av_UnitPower.attributes={units_av_UnitPower_exponent}

# units_av_UnitLiteral class attributes and methods

# units_av_Advice class attributes and methods

# units_av_EObject class attributes and methods

# units_av_GlobalScope class attributes and methods

# units_av_PerJoinPointScope class attributes and methods

# units_av_BaseUnit class attributes and methods
units_av_BaseUnit_name: Property = Property(name="name", type=StringType)
units_av_BaseUnit.attributes={units_av_BaseUnit_name}

# units_av_UnitRepository class attributes and methods

# units_av_UnitMultiplication class attributes and methods

# Unit class attributes and methods

# Relationships
unit0: BinaryAssociation = BinaryAssociation(
    name="unit0",
    ends={
        Property(name="units_av_Unit", type=units_av_UnitCarryingElement, multiplicity=Multiplicity(1, 1)),
        Property(name="units_av_UnitCarryingElement", type=units_av_Unit, multiplicity=Multiplicity(0, 1))
    }
)
units2: BinaryAssociation = BinaryAssociation(
    name="units2",
    ends={
        Property(name="units_av_Unit3", type=units_av_UnitMultiplication, multiplicity=Multiplicity(1, 1)),
        Property(name="units_av_UnitMultiplication", type=units_av_Unit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
unit4: BinaryAssociation = BinaryAssociation(
    name="unit4",
    ends={
        Property(name="units_av_Unit5", type=units_av_UnitPower, multiplicity=Multiplicity(1, 1)),
        Property(name="units_av_UnitPower", type=units_av_Unit, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
baseUnit6: BinaryAssociation = BinaryAssociation(
    name="baseUnit6",
    ends={
        Property(name="units_av_BaseUnit7", type=units_av_UnitLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="units_av_UnitLiteral", type=units_av_BaseUnit, multiplicity=Multiplicity(0, 1))
    }
)
children8: BinaryAssociation = BinaryAssociation(
    name="children8",
    ends={
        Property(name="units_av_EObject", type=units_av_Advice, multiplicity=Multiplicity(1, 1)),
        Property(name="units_av_Advice", type=units_av_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
scopedObject9: BinaryAssociation = BinaryAssociation(
    name="scopedObject9",
    ends={
        Property(name="units_av_EObject10", type=units_av_GlobalScope, multiplicity=Multiplicity(1, 1)),
        Property(name="units_av_GlobalScope", type=units_av_EObject, multiplicity=Multiplicity(1, 1))
    }
)
scopedObject11: BinaryAssociation = BinaryAssociation(
    name="scopedObject11",
    ends={
        Property(name="units_av_EObject12", type=units_av_PerJoinPointScope, multiplicity=Multiplicity(1, 1)),
        Property(name="units_av_PerJoinPointScope", type=units_av_EObject, multiplicity=Multiplicity(1, 1))
    }
)
units1: BinaryAssociation = BinaryAssociation(
    name="units1",
    ends={
        Property(name="units_av_BaseUnit", type=units_av_UnitRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="units_av_UnitRepository", type=units_av_BaseUnit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_units_av_UnitPower_Unit = Generalization(general=Unit, specific=units_av_UnitPower)
gen_units_av_UnitLiteral_Unit = Generalization(general=Unit, specific=units_av_UnitLiteral)
gen_units_av_UnitMultiplication_Unit = Generalization(general=Unit, specific=units_av_UnitMultiplication)

# Domain Model
domain_model = DomainModel(
    name="units_av",
    types={units_av_UnitCarryingElement, units_av_Unit, units_av_UnitPower, units_av_UnitLiteral, units_av_Advice, units_av_EObject, units_av_GlobalScope, units_av_PerJoinPointScope, units_av_BaseUnit, units_av_UnitRepository, units_av_UnitMultiplication, Unit},
    associations={unit0, units2, unit4, baseUnit6, children8, scopedObject9, scopedObject11, units1},
    generalizations={gen_units_av_UnitPower_Unit, gen_units_av_UnitLiteral_Unit, gen_units_av_UnitMultiplication_Unit},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)