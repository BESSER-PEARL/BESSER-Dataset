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
EnforcementMode: Enumeration = Enumeration(
    name="EnforcementMode",
    literals={
            EnumerationLiteral(name="Creation"),
			EnumerationLiteral(name="Deletion")
    }
)

# Classes
qvtcorebase_AbstractMapping = Class(name="qvtcorebase_AbstractMapping", is_abstract=True)
Rule = Class(name="Rule")
Area = Class(name="Area")
qvtcorebase_Area = Class(name="qvtcorebase_Area", is_abstract=True)
Element = Class(name="Element")
qvtcorebase_GuardPattern = Class(name="qvtcorebase_GuardPattern")
qvtcorebase_Assignment = Class(name="qvtcorebase_Assignment", is_abstract=True)
qvtcorebase_OCLExpression = Class(name="qvtcorebase_OCLExpression")
CorePattern = Class(name="CorePattern")
qvtcorebase_EnforcementOperation = Class(name="qvtcorebase_EnforcementOperation")
qvtcorebase_RealizedVariable = Class(name="qvtcorebase_RealizedVariable")
qvtcorebase_BottomPattern = Class(name="qvtcorebase_BottomPattern")
qvtcorebase_CorePattern = Class(name="qvtcorebase_CorePattern")
Pattern = Class(name="Pattern")
qvtcorebase_Variable = Class(name="qvtcorebase_Variable")
qvtcorebase_OperationCallExp = Class(name="qvtcorebase_OperationCallExp")
qvtcorebase_PropertyAssignment = Class(name="qvtcorebase_PropertyAssignment")
Assignment = Class(name="Assignment")
qvtcorebase_CoreDomain = Class(name="qvtcorebase_CoreDomain")
Domain = Class(name="Domain")
Variable = Class(name="Variable")
qvtcorebase_VariableAssignment = Class(name="qvtcorebase_VariableAssignment")
qvtcorebase_Property = Class(name="qvtcorebase_Property")

# qvtcorebase_AbstractMapping class attributes and methods
qvtcorebase_AbstractMapping_m_getContext: Method = Method(name="getContext", parameters={}, type=StringType)
qvtcorebase_AbstractMapping_m_getRefinement: Method = Method(name="getRefinement", parameters={}, type=StringType)
qvtcorebase_AbstractMapping.methods={qvtcorebase_AbstractMapping_m_getContext, qvtcorebase_AbstractMapping_m_getRefinement}

# Rule class attributes and methods

# Area class attributes and methods

# qvtcorebase_Area class attributes and methods
qvtcorebase_Area_m_getAllVariables: Method = Method(name="getAllVariables", parameters={}, type=StringType)
qvtcorebase_Area.methods={qvtcorebase_Area_m_getAllVariables}

# Element class attributes and methods

# qvtcorebase_GuardPattern class attributes and methods

# qvtcorebase_Assignment class attributes and methods
qvtcorebase_Assignment_isDefault: Property = Property(name="isDefault", type=StringType)
qvtcorebase_Assignment.attributes={qvtcorebase_Assignment_isDefault}

# qvtcorebase_OCLExpression class attributes and methods

# CorePattern class attributes and methods

# qvtcorebase_EnforcementOperation class attributes and methods
qvtcorebase_EnforcementOperation_enforcementMode: Property = Property(name="enforcementMode", type=StringType)
qvtcorebase_EnforcementOperation.attributes={qvtcorebase_EnforcementOperation_enforcementMode}

# qvtcorebase_RealizedVariable class attributes and methods

# qvtcorebase_BottomPattern class attributes and methods

# qvtcorebase_CorePattern class attributes and methods
qvtcorebase_CorePattern_m_getAllVariables: Method = Method(name="getAllVariables", parameters={}, type=StringType)
qvtcorebase_CorePattern_m_getArea: Method = Method(name="getArea", parameters={}, type=Area)
qvtcorebase_CorePattern.methods={qvtcorebase_CorePattern_m_getAllVariables, qvtcorebase_CorePattern_m_getArea}

# Pattern class attributes and methods

# qvtcorebase_Variable class attributes and methods

# qvtcorebase_OperationCallExp class attributes and methods

# qvtcorebase_PropertyAssignment class attributes and methods

# Assignment class attributes and methods

# qvtcorebase_CoreDomain class attributes and methods

# Domain class attributes and methods

# Variable class attributes and methods

# qvtcorebase_VariableAssignment class attributes and methods

# qvtcorebase_Property class attributes and methods

# Relationships
guardPattern0: BinaryAssociation = BinaryAssociation(
    name="guardPattern0",
    ends={
        Property(name="GuardPattern", type=qvtcorebase_Area, multiplicity=Multiplicity(1, 1)),
        Property(name="area", type=qvtcorebase_GuardPattern, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
bottomPattern1: BinaryAssociation = BinaryAssociation(
    name="bottomPattern1",
    ends={
        Property(name="area2", type=qvtcorebase_BottomPattern, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="BottomPattern", type=qvtcorebase_Area, multiplicity=Multiplicity(1, 1))
    }
)
bottomPattern3: BinaryAssociation = BinaryAssociation(
    name="bottomPattern3",
    ends={
        Property(name="BottomPattern4", type=qvtcorebase_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="assignment", type=qvtcorebase_BottomPattern, multiplicity=Multiplicity(1, 1))
    }
)
value5: BinaryAssociation = BinaryAssociation(
    name="value5",
    ends={
        Property(name="qvtcorebase_OCLExpression", type=qvtcorebase_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtcorebase_Assignment", type=qvtcorebase_OCLExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
area6: BinaryAssociation = BinaryAssociation(
    name="area6",
    ends={
        Property(name="Area", type=qvtcorebase_BottomPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="bottomPattern", type=qvtcorebase_Area, multiplicity=Multiplicity(1, 1))
    }
)
assignment7: BinaryAssociation = BinaryAssociation(
    name="assignment7",
    ends={
        Property(name="Assignment", type=qvtcorebase_BottomPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="bottomPattern8", type=qvtcorebase_Assignment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enforcementOperation9: BinaryAssociation = BinaryAssociation(
    name="enforcementOperation9",
    ends={
        Property(name="EnforcementOperation", type=qvtcorebase_BottomPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="bottomPattern10", type=qvtcorebase_EnforcementOperation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
realizedVariable11: BinaryAssociation = BinaryAssociation(
    name="realizedVariable11",
    ends={
        Property(name="qvtcorebase_RealizedVariable", type=qvtcorebase_BottomPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtcorebase_BottomPattern", type=qvtcorebase_RealizedVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable12: BinaryAssociation = BinaryAssociation(
    name="variable12",
    ends={
        Property(name="qvtcorebase_Variable", type=qvtcorebase_CorePattern, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtcorebase_CorePattern", type=qvtcorebase_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bottomPattern13: BinaryAssociation = BinaryAssociation(
    name="bottomPattern13",
    ends={
        Property(name="BottomPattern14", type=qvtcorebase_EnforcementOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="enforcementOperation", type=qvtcorebase_BottomPattern, multiplicity=Multiplicity(0, 1))
    }
)
operationCallExp15: BinaryAssociation = BinaryAssociation(
    name="operationCallExp15",
    ends={
        Property(name="qvtcorebase_OperationCallExp", type=qvtcorebase_EnforcementOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtcorebase_EnforcementOperation", type=qvtcorebase_OperationCallExp, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
area16: BinaryAssociation = BinaryAssociation(
    name="area16",
    ends={
        Property(name="Area17", type=qvtcorebase_GuardPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="guardPattern", type=qvtcorebase_Area, multiplicity=Multiplicity(1, 1))
    }
)
slotExpression18: BinaryAssociation = BinaryAssociation(
    name="slotExpression18",
    ends={
        Property(name="qvtcorebase_OCLExpression19", type=qvtcorebase_PropertyAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtcorebase_PropertyAssignment", type=qvtcorebase_OCLExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
targetVariable22: BinaryAssociation = BinaryAssociation(
    name="targetVariable22",
    ends={
        Property(name="qvtcorebase_Variable23", type=qvtcorebase_VariableAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtcorebase_VariableAssignment", type=qvtcorebase_Variable, multiplicity=Multiplicity(1, 1))
    }
)
targetProperty20: BinaryAssociation = BinaryAssociation(
    name="targetProperty20",
    ends={
        Property(name="qvtcorebase_Property", type=qvtcorebase_PropertyAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtcorebase_PropertyAssignment21", type=qvtcorebase_Property, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_qvtcorebase_AbstractMapping_Rule = Generalization(general=Rule, specific=qvtcorebase_AbstractMapping)
gen_qvtcorebase_AbstractMapping_Area = Generalization(general=Area, specific=qvtcorebase_AbstractMapping)
gen_qvtcorebase_Area_Element = Generalization(general=Element, specific=qvtcorebase_Area)
gen_qvtcorebase_Assignment_Element = Generalization(general=Element, specific=qvtcorebase_Assignment)
gen_qvtcorebase_BottomPattern_CorePattern = Generalization(general=CorePattern, specific=qvtcorebase_BottomPattern)
gen_qvtcorebase_CorePattern_Pattern = Generalization(general=Pattern, specific=qvtcorebase_CorePattern)
gen_qvtcorebase_EnforcementOperation_Element = Generalization(general=Element, specific=qvtcorebase_EnforcementOperation)
gen_qvtcorebase_GuardPattern_CorePattern = Generalization(general=CorePattern, specific=qvtcorebase_GuardPattern)
gen_qvtcorebase_PropertyAssignment_Assignment = Generalization(general=Assignment, specific=qvtcorebase_PropertyAssignment)
gen_qvtcorebase_CoreDomain_Domain = Generalization(general=Domain, specific=qvtcorebase_CoreDomain)
gen_qvtcorebase_CoreDomain_Area = Generalization(general=Area, specific=qvtcorebase_CoreDomain)
gen_qvtcorebase_RealizedVariable_Variable = Generalization(general=Variable, specific=qvtcorebase_RealizedVariable)
gen_qvtcorebase_VariableAssignment_Assignment = Generalization(general=Assignment, specific=qvtcorebase_VariableAssignment)

# Domain Model
domain_model = DomainModel(
    name="qvtcorebase",
    types={qvtcorebase_AbstractMapping, Rule, Area, qvtcorebase_Area, Element, qvtcorebase_GuardPattern, qvtcorebase_Assignment, qvtcorebase_OCLExpression, CorePattern, qvtcorebase_EnforcementOperation, qvtcorebase_RealizedVariable, qvtcorebase_BottomPattern, qvtcorebase_CorePattern, Pattern, qvtcorebase_Variable, qvtcorebase_OperationCallExp, qvtcorebase_PropertyAssignment, Assignment, qvtcorebase_CoreDomain, Domain, Variable, qvtcorebase_VariableAssignment, qvtcorebase_Property, EnforcementMode},
    associations={guardPattern0, bottomPattern1, bottomPattern3, value5, area6, assignment7, enforcementOperation9, realizedVariable11, variable12, bottomPattern13, operationCallExp15, area16, slotExpression18, targetVariable22, targetProperty20},
    generalizations={gen_qvtcorebase_AbstractMapping_Rule, gen_qvtcorebase_AbstractMapping_Area, gen_qvtcorebase_Area_Element, gen_qvtcorebase_Assignment_Element, gen_qvtcorebase_BottomPattern_CorePattern, gen_qvtcorebase_CorePattern_Pattern, gen_qvtcorebase_EnforcementOperation_Element, gen_qvtcorebase_GuardPattern_CorePattern, gen_qvtcorebase_PropertyAssignment_Assignment, gen_qvtcorebase_CoreDomain_Domain, gen_qvtcorebase_CoreDomain_Area, gen_qvtcorebase_RealizedVariable_Variable, gen_qvtcorebase_VariableAssignment_Assignment},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)