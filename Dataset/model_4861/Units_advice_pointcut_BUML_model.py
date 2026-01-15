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
units_av_pc_BaseUnit = Class(name="units::av::pc::BaseUnit")
units_av_pc_UnitRepository = Class(name="units::av::pc::UnitRepository")
units_av_pc_UnitMultiplication = Class(name="units::av::pc::UnitMultiplication")
Unit = Class(name="Unit")
units_av_pc_UnitPower = Class(name="units::av::pc::UnitPower")
units_av_pc_UnitLiteral = Class(name="units::av::pc::UnitLiteral")
units_av_pc_Advice = Class(name="units::av::pc::Advice")
units_av_pc_UnitCarryingElement = Class(name="units::av::pc::UnitCarryingElement")
units_av_pc_Unit = Class(name="units::av::pc::Unit")
units_av_pc_EObject = Class(name="units::av::pc::EObject")
units_av_pc_GlobalScope = Class(name="units::av::pc::GlobalScope")
units_av_pc_PerJoinPointScope = Class(name="units::av::pc::PerJoinPointScope")
units_av_pc_Pointcut = Class(name="units::av::pc::Pointcut")

# units_av_pc_BaseUnit class attributes and methods
units_av_pc_BaseUnit_name: Property = Property(name="name", type=StringType)
units_av_pc_BaseUnit.attributes={units_av_pc_BaseUnit_name}

# units_av_pc_UnitRepository class attributes and methods

# units_av_pc_UnitMultiplication class attributes and methods

# Unit class attributes and methods

# units_av_pc_UnitPower class attributes and methods
units_av_pc_UnitPower_exponent: Property = Property(name="exponent", type=IntegerType)
units_av_pc_UnitPower.attributes={units_av_pc_UnitPower_exponent}

# units_av_pc_UnitLiteral class attributes and methods

# units_av_pc_Advice class attributes and methods

# units_av_pc_UnitCarryingElement class attributes and methods
units_av_pc_UnitCarryingElement_unitSpecification: Property = Property(name="unitSpecification", type=StringType)
units_av_pc_UnitCarryingElement.attributes={units_av_pc_UnitCarryingElement_unitSpecification}

# units_av_pc_Unit class attributes and methods

# units_av_pc_EObject class attributes and methods

# units_av_pc_GlobalScope class attributes and methods

# units_av_pc_PerJoinPointScope class attributes and methods

# units_av_pc_Pointcut class attributes and methods

# Relationships
units1: BinaryAssociation = BinaryAssociation(
    name="units1",
    ends={
        Property(name="units_av_pc_BaseUnit", type=units_av_pc_UnitRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="units_av_pc_UnitRepository", type=units_av_pc_BaseUnit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
units2: BinaryAssociation = BinaryAssociation(
    name="units2",
    ends={
        Property(name="units_av_pc_Unit3", type=units_av_pc_UnitMultiplication, multiplicity=Multiplicity(1, 1)),
        Property(name="units_av_pc_UnitMultiplication", type=units_av_pc_Unit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
unit4: BinaryAssociation = BinaryAssociation(
    name="unit4",
    ends={
        Property(name="units_av_pc_Unit5", type=units_av_pc_UnitPower, multiplicity=Multiplicity(1, 1)),
        Property(name="units_av_pc_UnitPower", type=units_av_pc_Unit, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
baseUnit6: BinaryAssociation = BinaryAssociation(
    name="baseUnit6",
    ends={
        Property(name="units_av_pc_BaseUnit7", type=units_av_pc_UnitLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="units_av_pc_UnitLiteral", type=units_av_pc_BaseUnit, multiplicity=Multiplicity(0, 1))
    }
)
unit0: BinaryAssociation = BinaryAssociation(
    name="unit0",
    ends={
        Property(name="units_av_pc_Unit", type=units_av_pc_UnitCarryingElement, multiplicity=Multiplicity(1, 1)),
        Property(name="units_av_pc_UnitCarryingElement", type=units_av_pc_Unit, multiplicity=Multiplicity(0, 1))
    }
)
children8: BinaryAssociation = BinaryAssociation(
    name="children8",
    ends={
        Property(name="units_av_pc_EObject", type=units_av_pc_Advice, multiplicity=Multiplicity(1, 1)),
        Property(name="units_av_pc_Advice", type=units_av_pc_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
scopedObject9: BinaryAssociation = BinaryAssociation(
    name="scopedObject9",
    ends={
        Property(name="units_av_pc_EObject10", type=units_av_pc_GlobalScope, multiplicity=Multiplicity(1, 1)),
        Property(name="units_av_pc_GlobalScope", type=units_av_pc_EObject, multiplicity=Multiplicity(0, 1))
    }
)
scopedObject11: BinaryAssociation = BinaryAssociation(
    name="scopedObject11",
    ends={
        Property(name="units_av_pc_EObject12", type=units_av_pc_PerJoinPointScope, multiplicity=Multiplicity(1, 1)),
        Property(name="units_av_pc_PerJoinPointScope", type=units_av_pc_EObject, multiplicity=Multiplicity(0, 1))
    }
)
children13: BinaryAssociation = BinaryAssociation(
    name="children13",
    ends={
        Property(name="units_av_pc_EObject14", type=units_av_pc_Pointcut, multiplicity=Multiplicity(1, 1)),
        Property(name="units_av_pc_Pointcut", type=units_av_pc_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_units_av_pc_UnitMultiplication_Unit = Generalization(general=Unit, specific=units_av_pc_UnitMultiplication)
gen_units_av_pc_UnitPower_Unit = Generalization(general=Unit, specific=units_av_pc_UnitPower)
gen_units_av_pc_UnitLiteral_Unit = Generalization(general=Unit, specific=units_av_pc_UnitLiteral)

# Domain Model
domain_model = DomainModel(
    name="units_av_pc",
    types={units_av_pc_BaseUnit, units_av_pc_UnitRepository, units_av_pc_UnitMultiplication, Unit, units_av_pc_UnitPower, units_av_pc_UnitLiteral, units_av_pc_Advice, units_av_pc_UnitCarryingElement, units_av_pc_Unit, units_av_pc_EObject, units_av_pc_GlobalScope, units_av_pc_PerJoinPointScope, units_av_pc_Pointcut},
    associations={units1, units2, unit4, baseUnit6, unit0, children8, scopedObject9, scopedObject11, children13},
    generalizations={gen_units_av_pc_UnitMultiplication_Unit, gen_units_av_pc_UnitPower_Unit, gen_units_av_pc_UnitLiteral_Unit},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)