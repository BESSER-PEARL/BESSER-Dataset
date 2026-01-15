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
SeverityKind: Enumeration = Enumeration(
    name="SeverityKind",
    literals={
            EnumerationLiteral(name="error"),
			EnumerationLiteral(name="warning"),
			EnumerationLiteral(name="fatal")
    }
)

# Classes
ImperativeOCL_AltExp = Class(name="ImperativeOCL::AltExp")
ImperativeExpression = Class(name="ImperativeExpression")
ImperativeOCL_AssertExp = Class(name="ImperativeOCL::AssertExp")
ImperativeOCL_CatchExp = Class(name="ImperativeOCL::CatchExp")
ImperativeOCL_ComputeExp = Class(name="ImperativeOCL::ComputeExp")
LogExp = Class(name="LogExp")
ImperativeOCL_AssignExp = Class(name="ImperativeOCL::AssignExp")
ImperativeOCL_BlockExp = Class(name="ImperativeOCL::BlockExp")
ImperativeOCL_BreakExp = Class(name="ImperativeOCL::BreakExp")
ImperativeOCL_ImperativeLoopExp = Class(name="ImperativeOCL::ImperativeLoopExp", is_abstract=True)
ImperativeOCL_InstantiationExp = Class(name="ImperativeOCL::InstantiationExp")
ImperativeOCL_ContinueExp = Class(name="ImperativeOCL::ContinueExp")
ImperativeOCL_DictLiteralExp = Class(name="ImperativeOCL::DictLiteralExp")
DictLiteralPart = Class(name="DictLiteralPart")
ImperativeOCL_DictLiteralPart = Class(name="ImperativeOCL::DictLiteralPart")
ImperativeOCL_DictionaryType = Class(name="ImperativeOCL::DictionaryType")
ImperativeOCL_ForExp = Class(name="ImperativeOCL::ForExp")
ImperativeLoopExp = Class(name="ImperativeLoopExp")
ImperativeOCL_ImperativeExpression = Class(name="ImperativeOCL::ImperativeExpression", is_abstract=True)
ImperativeOCL_ImperativeIterateExp = Class(name="ImperativeOCL::ImperativeIterateExp")
ImperativeOCL_ReturnExp = Class(name="ImperativeOCL::ReturnExp")
ImperativeOCL_SwitchExp = Class(name="ImperativeOCL::SwitchExp")
AltExp = Class(name="AltExp")
ImperativeOCL_ListLiteralExp = Class(name="ImperativeOCL::ListLiteralExp")
ImperativeOCL_ListType = Class(name="ImperativeOCL::ListType")
ImperativeOCL_LogExp = Class(name="ImperativeOCL::LogExp")
ImperativeOCL_OrderedTupleLiteralExp = Class(name="ImperativeOCL::OrderedTupleLiteralExp")
OrderedTupleLiteralPart = Class(name="OrderedTupleLiteralPart")
ImperativeOCL_OrderedTupleLiteralPart = Class(name="ImperativeOCL::OrderedTupleLiteralPart")
ImperativeOCL_OrderedTupleType = Class(name="ImperativeOCL::OrderedTupleType")
ImperativeOCL_RaiseExp = Class(name="ImperativeOCL::RaiseExp")
ImperativeOCL_UnpackExp = Class(name="ImperativeOCL::UnpackExp")
ImperativeOCL_VariableInitExp = Class(name="ImperativeOCL::VariableInitExp")
ImperativeOCL_WhileExp = Class(name="ImperativeOCL::WhileExp")
ImperativeOCL_TryExp = Class(name="ImperativeOCL::TryExp")
CatchExp = Class(name="CatchExp")
ImperativeOCL_Typedef = Class(name="ImperativeOCL::Typedef")
ImperativeOCL_UnlinkExp = Class(name="ImperativeOCL::UnlinkExp")

# ImperativeOCL_AltExp class attributes and methods

# ImperativeExpression class attributes and methods

# ImperativeOCL_AssertExp class attributes and methods
ImperativeOCL_AssertExp_severity: Property = Property(name="severity", type=StringType)
ImperativeOCL_AssertExp.attributes={ImperativeOCL_AssertExp_severity}

# ImperativeOCL_CatchExp class attributes and methods

# ImperativeOCL_ComputeExp class attributes and methods

# LogExp class attributes and methods

# ImperativeOCL_AssignExp class attributes and methods
ImperativeOCL_AssignExp_isReset: Property = Property(name="isReset", type=StringType)
ImperativeOCL_AssignExp.attributes={ImperativeOCL_AssignExp_isReset}

# ImperativeOCL_BlockExp class attributes and methods

# ImperativeOCL_BreakExp class attributes and methods

# ImperativeOCL_ImperativeLoopExp class attributes and methods

# ImperativeOCL_InstantiationExp class attributes and methods

# ImperativeOCL_ContinueExp class attributes and methods

# ImperativeOCL_DictLiteralExp class attributes and methods

# DictLiteralPart class attributes and methods

# ImperativeOCL_DictLiteralPart class attributes and methods

# ImperativeOCL_DictionaryType class attributes and methods

# ImperativeOCL_ForExp class attributes and methods

# ImperativeLoopExp class attributes and methods

# ImperativeOCL_ImperativeExpression class attributes and methods

# ImperativeOCL_ImperativeIterateExp class attributes and methods

# ImperativeOCL_ReturnExp class attributes and methods

# ImperativeOCL_SwitchExp class attributes and methods

# AltExp class attributes and methods

# ImperativeOCL_ListLiteralExp class attributes and methods

# ImperativeOCL_ListType class attributes and methods

# ImperativeOCL_LogExp class attributes and methods

# ImperativeOCL_OrderedTupleLiteralExp class attributes and methods

# OrderedTupleLiteralPart class attributes and methods

# ImperativeOCL_OrderedTupleLiteralPart class attributes and methods

# ImperativeOCL_OrderedTupleType class attributes and methods

# ImperativeOCL_RaiseExp class attributes and methods

# ImperativeOCL_UnpackExp class attributes and methods

# ImperativeOCL_VariableInitExp class attributes and methods
ImperativeOCL_VariableInitExp_withResult: Property = Property(name="withResult", type=StringType)
ImperativeOCL_VariableInitExp.attributes={ImperativeOCL_VariableInitExp_withResult}

# ImperativeOCL_WhileExp class attributes and methods

# ImperativeOCL_TryExp class attributes and methods

# CatchExp class attributes and methods

# ImperativeOCL_Typedef class attributes and methods

# ImperativeOCL_UnlinkExp class attributes and methods

# Relationships
log0: BinaryAssociation = BinaryAssociation(
    name="log0",
    ends={
        Property(name="LogExp", type=ImperativeOCL_AssertExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_AssertExp", type=LogExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
part1: BinaryAssociation = BinaryAssociation(
    name="part1",
    ends={
        Property(name="DictLiteralPart", type=ImperativeOCL_DictLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_DictLiteralExp", type=DictLiteralPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
alternativePart3: BinaryAssociation = BinaryAssociation(
    name="alternativePart3",
    ends={
        Property(name="AltExp", type=ImperativeOCL_SwitchExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_SwitchExp", type=AltExp, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
part2: BinaryAssociation = BinaryAssociation(
    name="part2",
    ends={
        Property(name="OrderedTupleLiteralPart", type=ImperativeOCL_OrderedTupleLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_OrderedTupleLiteralExp", type=OrderedTupleLiteralPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exceptClause4: BinaryAssociation = BinaryAssociation(
    name="exceptClause4",
    ends={
        Property(name="CatchExp", type=ImperativeOCL_TryExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_TryExp", type=CatchExp, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_ImperativeOCL_AltExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_AltExp)
gen_ImperativeOCL_AssertExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_AssertExp)
gen_ImperativeOCL_BreakExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_BreakExp)
gen_ImperativeOCL_CatchExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_CatchExp)
gen_ImperativeOCL_ComputeExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_ComputeExp)
gen_ImperativeOCL_AssignExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_AssignExp)
gen_ImperativeOCL_BlockExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_BlockExp)
gen_ImperativeOCL_InstantiationExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_InstantiationExp)
gen_ImperativeOCL_ContinueExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_ContinueExp)
gen_ImperativeOCL_ForExp_ImperativeLoopExp = Generalization(general=ImperativeLoopExp, specific=ImperativeOCL_ForExp)
gen_ImperativeOCL_ImperativeIterateExp_ImperativeLoopExp = Generalization(general=ImperativeLoopExp, specific=ImperativeOCL_ImperativeIterateExp)
gen_ImperativeOCL_RaiseExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_RaiseExp)
gen_ImperativeOCL_ReturnExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_ReturnExp)
gen_ImperativeOCL_SwitchExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_SwitchExp)
gen_ImperativeOCL_UnpackExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_UnpackExp)
gen_ImperativeOCL_VariableInitExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_VariableInitExp)
gen_ImperativeOCL_WhileExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_WhileExp)
gen_ImperativeOCL_TryExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_TryExp)
gen_ImperativeOCL_UnlinkExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_UnlinkExp)

# Domain Model
domain_model = DomainModel(
    name="ImperativeOCL",
    types={ImperativeOCL_AltExp, ImperativeExpression, ImperativeOCL_AssertExp, ImperativeOCL_CatchExp, ImperativeOCL_ComputeExp, LogExp, ImperativeOCL_AssignExp, ImperativeOCL_BlockExp, ImperativeOCL_BreakExp, ImperativeOCL_ImperativeLoopExp, ImperativeOCL_InstantiationExp, ImperativeOCL_ContinueExp, ImperativeOCL_DictLiteralExp, DictLiteralPart, ImperativeOCL_DictLiteralPart, ImperativeOCL_DictionaryType, ImperativeOCL_ForExp, ImperativeLoopExp, ImperativeOCL_ImperativeExpression, ImperativeOCL_ImperativeIterateExp, ImperativeOCL_ReturnExp, ImperativeOCL_SwitchExp, AltExp, ImperativeOCL_ListLiteralExp, ImperativeOCL_ListType, ImperativeOCL_LogExp, ImperativeOCL_OrderedTupleLiteralExp, OrderedTupleLiteralPart, ImperativeOCL_OrderedTupleLiteralPart, ImperativeOCL_OrderedTupleType, ImperativeOCL_RaiseExp, ImperativeOCL_UnpackExp, ImperativeOCL_VariableInitExp, ImperativeOCL_WhileExp, ImperativeOCL_TryExp, CatchExp, ImperativeOCL_Typedef, ImperativeOCL_UnlinkExp, SeverityKind},
    associations={log0, part1, alternativePart3, part2, exceptClause4},
    generalizations={gen_ImperativeOCL_AltExp_ImperativeExpression, gen_ImperativeOCL_AssertExp_ImperativeExpression, gen_ImperativeOCL_BreakExp_ImperativeExpression, gen_ImperativeOCL_CatchExp_ImperativeExpression, gen_ImperativeOCL_ComputeExp_ImperativeExpression, gen_ImperativeOCL_AssignExp_ImperativeExpression, gen_ImperativeOCL_BlockExp_ImperativeExpression, gen_ImperativeOCL_InstantiationExp_ImperativeExpression, gen_ImperativeOCL_ContinueExp_ImperativeExpression, gen_ImperativeOCL_ForExp_ImperativeLoopExp, gen_ImperativeOCL_ImperativeIterateExp_ImperativeLoopExp, gen_ImperativeOCL_RaiseExp_ImperativeExpression, gen_ImperativeOCL_ReturnExp_ImperativeExpression, gen_ImperativeOCL_SwitchExp_ImperativeExpression, gen_ImperativeOCL_UnpackExp_ImperativeExpression, gen_ImperativeOCL_VariableInitExp_ImperativeExpression, gen_ImperativeOCL_WhileExp_ImperativeExpression, gen_ImperativeOCL_TryExp_ImperativeExpression, gen_ImperativeOCL_UnlinkExp_ImperativeExpression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)