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
units_av_av_UnitPower = Class(name="units::av::av::UnitPower")
units_av_av_UnitCarryingElement = Class(name="units::av::av::UnitCarryingElement")
units_av_av_Unit = Class(name="units::av::av::Unit")
units_av_av_BaseUnit = Class(name="units::av::av::BaseUnit")
units_av_av_UnitRepository = Class(name="units::av::av::UnitRepository")
units_av_av_UnitMultiplication = Class(name="units::av::av::UnitMultiplication")
Unit = Class(name="Unit")
units_av_av_UnitLiteral = Class(name="units::av::av::UnitLiteral")
units_av_av_AdviceAdvice = Class(name="units::av::av::AdviceAdvice")
units_av_av_EObject = Class(name="units::av::av::EObject")
units_av_av_GlobalScopeGlobalScope = Class(name="units::av::av::GlobalScopeGlobalScope")
units_av_av_PerJoinPointScopePerJoinPointScope = Class(name="units::av::av::PerJoinPointScopePerJoinPointScope")
units_av_av_Advice = Class(name="units::av::av::Advice")
units_av_av_GlobalScope = Class(name="units::av::av::GlobalScope")
units_av_av_PerJoinPointScope = Class(name="units::av::av::PerJoinPointScope")

# units_av_av_UnitPower class attributes and methods
units_av_av_UnitPower_exponent: Property = Property(name="exponent", type=IntegerType)
units_av_av_UnitPower.attributes={units_av_av_UnitPower_exponent}

# units_av_av_UnitCarryingElement class attributes and methods
units_av_av_UnitCarryingElement_unitSpecification: Property = Property(name="unitSpecification", type=StringType)
units_av_av_UnitCarryingElement.attributes={units_av_av_UnitCarryingElement_unitSpecification}

# units_av_av_Unit class attributes and methods

# units_av_av_BaseUnit class attributes and methods
units_av_av_BaseUnit_name: Property = Property(name="name", type=StringType)
units_av_av_BaseUnit.attributes={units_av_av_BaseUnit_name}

# units_av_av_UnitRepository class attributes and methods

# units_av_av_UnitMultiplication class attributes and methods

# Unit class attributes and methods

# units_av_av_UnitLiteral class attributes and methods

# units_av_av_AdviceAdvice class attributes and methods

# units_av_av_EObject class attributes and methods

# units_av_av_GlobalScopeGlobalScope class attributes and methods

# units_av_av_PerJoinPointScopePerJoinPointScope class attributes and methods

# units_av_av_Advice class attributes and methods

# units_av_av_GlobalScope class attributes and methods

# units_av_av_PerJoinPointScope class attributes and methods

# Relationships
unit4: BinaryAssociation = BinaryAssociation(
    name="unit4",
    ends={
        Property(name="units_av_av_Unit5", type=units_av_av_UnitPower, multiplicity=Multiplicity(1, 1)),
        Property(name="units_av_av_UnitPower", type=units_av_av_Unit, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
unit0: BinaryAssociation = BinaryAssociation(
    name="unit0",
    ends={
        Property(name="units_av_av_Unit", type=units_av_av_UnitCarryingElement, multiplicity=Multiplicity(1, 1)),
        Property(name="units_av_av_UnitCarryingElement", type=units_av_av_Unit, multiplicity=Multiplicity(0, 1))
    }
)
units1: BinaryAssociation = BinaryAssociation(
    name="units1",
    ends={
        Property(name="units_av_av_BaseUnit", type=units_av_av_UnitRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="units_av_av_UnitRepository", type=units_av_av_BaseUnit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
units2: BinaryAssociation = BinaryAssociation(
    name="units2",
    ends={
        Property(name="units_av_av_Unit3", type=units_av_av_UnitMultiplication, multiplicity=Multiplicity(1, 1)),
        Property(name="units_av_av_UnitMultiplication", type=units_av_av_Unit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
baseUnit6: BinaryAssociation = BinaryAssociation(
    name="baseUnit6",
    ends={
        Property(name="units_av_av_BaseUnit7", type=units_av_av_UnitLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="units_av_av_UnitLiteral", type=units_av_av_BaseUnit, multiplicity=Multiplicity(0, 1))
    }
)
children8: BinaryAssociation = BinaryAssociation(
    name="children8",
    ends={
        Property(name="units_av_av_EObject", type=units_av_av_AdviceAdvice, multiplicity=Multiplicity(1, 1)),
        Property(name="units_av_av_AdviceAdvice", type=units_av_av_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
scopedObject9: BinaryAssociation = BinaryAssociation(
    name="scopedObject9",
    ends={
        Property(name="units_av_av_EObject10", type=units_av_av_GlobalScopeGlobalScope, multiplicity=Multiplicity(1, 1)),
        Property(name="units_av_av_GlobalScopeGlobalScope", type=units_av_av_EObject, multiplicity=Multiplicity(0, 1))
    }
)
scopedObject11: BinaryAssociation = BinaryAssociation(
    name="scopedObject11",
    ends={
        Property(name="units_av_av_EObject12", type=units_av_av_PerJoinPointScopePerJoinPointScope, multiplicity=Multiplicity(1, 1)),
        Property(name="units_av_av_PerJoinPointScopePerJoinPointScope", type=units_av_av_EObject, multiplicity=Multiplicity(0, 1))
    }
)
children13: BinaryAssociation = BinaryAssociation(
    name="children13",
    ends={
        Property(name="units_av_av_EObject14", type=units_av_av_Advice, multiplicity=Multiplicity(1, 1)),
        Property(name="units_av_av_Advice", type=units_av_av_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
scopedObject15: BinaryAssociation = BinaryAssociation(
    name="scopedObject15",
    ends={
        Property(name="units_av_av_EObject16", type=units_av_av_GlobalScope, multiplicity=Multiplicity(1, 1)),
        Property(name="units_av_av_GlobalScope", type=units_av_av_EObject, multiplicity=Multiplicity(1, 1))
    }
)
scopedObject17: BinaryAssociation = BinaryAssociation(
    name="scopedObject17",
    ends={
        Property(name="units_av_av_EObject18", type=units_av_av_PerJoinPointScope, multiplicity=Multiplicity(1, 1)),
        Property(name="units_av_av_PerJoinPointScope", type=units_av_av_EObject, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_units_av_av_UnitPower_Unit = Generalization(general=Unit, specific=units_av_av_UnitPower)
gen_units_av_av_UnitMultiplication_Unit = Generalization(general=Unit, specific=units_av_av_UnitMultiplication)
gen_units_av_av_UnitLiteral_Unit = Generalization(general=Unit, specific=units_av_av_UnitLiteral)

# Domain Model
domain_model = DomainModel(
    name="units_av_av",
    types={units_av_av_UnitPower, units_av_av_UnitCarryingElement, units_av_av_Unit, units_av_av_BaseUnit, units_av_av_UnitRepository, units_av_av_UnitMultiplication, Unit, units_av_av_UnitLiteral, units_av_av_AdviceAdvice, units_av_av_EObject, units_av_av_GlobalScopeGlobalScope, units_av_av_PerJoinPointScopePerJoinPointScope, units_av_av_Advice, units_av_av_GlobalScope, units_av_av_PerJoinPointScope},
    associations={unit4, unit0, units1, units2, baseUnit6, children8, scopedObject9, scopedObject11, children13, scopedObject15, scopedObject17},
    generalizations={gen_units_av_av_UnitPower_Unit, gen_units_av_av_UnitMultiplication_Unit, gen_units_av_av_UnitLiteral_Unit},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)