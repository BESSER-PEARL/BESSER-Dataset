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
picojava_TypeDecl = Class(name="picojava::TypeDecl", is_abstract=True)
picojava_UnknownDecl = Class(name="picojava::UnknownDecl")
picojava_PrimitiveDecl = Class(name="picojava::PrimitiveDecl")
picojava_Program = Class(name="picojava::Program")
picojava_Block = Class(name="picojava::Block")
picojava_Stmt = Class(name="picojava::Stmt", is_abstract=True)
BlockStmt = Class(name="BlockStmt")
picojava_BlockStmt = Class(name="picojava::BlockStmt", is_abstract=True)
picojava_Decl = Class(name="picojava::Decl", is_abstract=True)
Decl = Class(name="Decl")
picojava_VarDecl = Class(name="picojava::VarDecl")
picojava_AssignStmt = Class(name="picojava::AssignStmt")
Stmt = Class(name="Stmt")
picojava_Access = Class(name="picojava::Access", is_abstract=True)
picojava_ClassDecl = Class(name="picojava::ClassDecl")
TypeDecl = Class(name="TypeDecl")
picojava_IdUse = Class(name="picojava::IdUse", is_abstract=True)
picojava_Exp = Class(name="picojava::Exp", is_abstract=True)
picojava_WhileStmt = Class(name="picojava::WhileStmt")
picojava_Use = Class(name="picojava::Use")
IdUse = Class(name="IdUse")
picojava_Dot = Class(name="picojava::Dot")
Exp = Class(name="Exp")
Access = Class(name="Access")
picojava_BooleanLiteral = Class(name="picojava::BooleanLiteral")
picojava_TypeUse = Class(name="picojava::TypeUse")
picojava_VariableUse = Class(name="picojava::VariableUse")

# picojava_TypeDecl class attributes and methods
picojava_TypeDecl_isQualified: Property = Property(name="isQualified", type=BooleanType)
picojava_TypeDecl_m_lookup: Method = Method(name="lookup", parameters={Parameter(name='name')}, type=Decl)
picojava_TypeDecl_m_remoteLookup: Method = Method(name="remoteLookup", parameters={Parameter(name='name')}, type=Decl)
picojava_TypeDecl_m_isSubtypeOf: Method = Method(name="isSubtypeOf", parameters={Parameter(name='typeDecl')})
picojava_TypeDecl_m_isSuperTypeOf: Method = Method(name="isSuperTypeOf", parameters={Parameter(name='typeDecl')})
picojava_TypeDecl_m_isSuperTypeOfClassDecl: Method = Method(name="isSuperTypeOfClassDecl", parameters={Parameter(name='typeDecl')})
picojava_TypeDecl.attributes={picojava_TypeDecl_isQualified}
picojava_TypeDecl.methods={picojava_TypeDecl_m_isSuperTypeOf, picojava_TypeDecl_m_isSuperTypeOfClassDecl, picojava_TypeDecl_m_lookup, picojava_TypeDecl_m_isSubtypeOf, picojava_TypeDecl_m_remoteLookup}

# picojava_UnknownDecl class attributes and methods

# picojava_PrimitiveDecl class attributes and methods

# picojava_Program class attributes and methods
picojava_Program_m_localLookup: Method = Method(name="localLookup", parameters={Parameter(name='name')}, type=StringType)
picojava_Program.methods={picojava_Program_m_localLookup}

# picojava_Block class attributes and methods
picojava_Block_m_localLookup: Method = Method(name="localLookup", parameters={Parameter(name='name')}, type=StringType)
picojava_Block_m_lookup: Method = Method(name="lookup", parameters={Parameter(name='name')}, type=StringType)
picojava_Block.methods={picojava_Block_m_lookup, picojava_Block_m_localLookup}

# picojava_Stmt class attributes and methods

# BlockStmt class attributes and methods

# picojava_BlockStmt class attributes and methods
picojava_BlockStmt_m_declarationOf: Method = Method(name="declarationOf", parameters={Parameter(name='name')}, type=StringType)
picojava_BlockStmt.methods={picojava_BlockStmt_m_declarationOf}

# picojava_Decl class attributes and methods
picojava_Decl_Name: Property = Property(name="Name", type=StringType)
picojava_Decl_isUnknown: Property = Property(name="isUnknown", type=BooleanType)
picojava_Decl.attributes={picojava_Decl_isUnknown, picojava_Decl_Name}

# Decl class attributes and methods

# picojava_VarDecl class attributes and methods

# picojava_AssignStmt class attributes and methods

# Stmt class attributes and methods

# picojava_Access class attributes and methods

# picojava_ClassDecl class attributes and methods
picojava_ClassDecl_hasCycleOnSuperclassChain: Property = Property(name="hasCycleOnSuperclassChain", type=BooleanType)
picojava_ClassDecl.attributes={picojava_ClassDecl_hasCycleOnSuperclassChain}

# TypeDecl class attributes and methods

# picojava_IdUse class attributes and methods
picojava_IdUse_Name: Property = Property(name="Name", type=StringType)
picojava_IdUse_isQualified: Property = Property(name="isQualified", type=BooleanType)
picojava_IdUse_m_lookup: Method = Method(name="lookup", parameters={Parameter(name='name')}, type=Decl)
picojava_IdUse.attributes={picojava_IdUse_isQualified, picojava_IdUse_Name}
picojava_IdUse.methods={picojava_IdUse_m_lookup}

# picojava_Exp class attributes and methods
picojava_Exp_isValue: Property = Property(name="isValue", type=BooleanType)
picojava_Exp.attributes={picojava_Exp_isValue}

# picojava_WhileStmt class attributes and methods

# picojava_Use class attributes and methods

# IdUse class attributes and methods

# picojava_Dot class attributes and methods

# Exp class attributes and methods

# Access class attributes and methods

# picojava_BooleanLiteral class attributes and methods
picojava_BooleanLiteral_Value: Property = Property(name="Value", type=StringType)
picojava_BooleanLiteral.attributes={picojava_BooleanLiteral_Value}

# picojava_TypeUse class attributes and methods

# picojava_VariableUse class attributes and methods

# Relationships
PredefinedType1: BinaryAssociation = BinaryAssociation(
    name="PredefinedType1",
    ends={
        Property(name="picojava_TypeDecl", type=picojava_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="picojava_Program2", type=picojava_TypeDecl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
unknownDecl3: BinaryAssociation = BinaryAssociation(
    name="unknownDecl3",
    ends={
        Property(name="picojava_UnknownDecl", type=picojava_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="picojava_Program4", type=picojava_UnknownDecl, multiplicity=Multiplicity(0, 1))
    }
)
booleanType5: BinaryAssociation = BinaryAssociation(
    name="booleanType5",
    ends={
        Property(name="picojava_PrimitiveDecl", type=picojava_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="picojava_Program6", type=picojava_PrimitiveDecl, multiplicity=Multiplicity(0, 1))
    }
)
Block0: BinaryAssociation = BinaryAssociation(
    name="Block0",
    ends={
        Property(name="picojava_Block", type=picojava_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="picojava_Program", type=picojava_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type11: BinaryAssociation = BinaryAssociation(
    name="type11",
    ends={
        Property(name="picojava_TypeDecl13", type=picojava_Decl, multiplicity=Multiplicity(1, 1)),
        Property(name="picojava_Decl12", type=picojava_TypeDecl, multiplicity=Multiplicity(0, 1))
    }
)
BlockStmt7: BinaryAssociation = BinaryAssociation(
    name="BlockStmt7",
    ends={
        Property(name="picojava_BlockStmt", type=picojava_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="picojava_Block8", type=picojava_BlockStmt, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
unknownDecl9: BinaryAssociation = BinaryAssociation(
    name="unknownDecl9",
    ends={
        Property(name="picojava_Decl", type=picojava_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="picojava_Block10", type=picojava_Decl, multiplicity=Multiplicity(0, 1))
    }
)
booleanType14: BinaryAssociation = BinaryAssociation(
    name="booleanType14",
    ends={
        Property(name="picojava_PrimitiveDecl16", type=picojava_Decl, multiplicity=Multiplicity(1, 1)),
        Property(name="picojava_Decl15", type=picojava_PrimitiveDecl, multiplicity=Multiplicity(0, 1))
    }
)
superClass27: BinaryAssociation = BinaryAssociation(
    name="superClass27",
    ends={
        Property(name="picojava_ClassDecl26", type=picojava_ClassDecl, multiplicity=Multiplicity(0, 1)),
        Property(name="picojava_ClassDecl28", type=picojava_ClassDecl, multiplicity=Multiplicity(1, 1))
    }
)
Type29: BinaryAssociation = BinaryAssociation(
    name="Type29",
    ends={
        Property(name="picojava_Access30", type=picojava_VarDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="picojava_VarDecl", type=picojava_Access, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
Variable31: BinaryAssociation = BinaryAssociation(
    name="Variable31",
    ends={
        Property(name="picojava_Access32", type=picojava_AssignStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="picojava_AssignStmt", type=picojava_Access, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
qualifier17: BinaryAssociation = BinaryAssociation(
    name="qualifier17",
    ends={
        Property(name="picojava_Access", type=picojava_TypeDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="picojava_TypeDecl18", type=picojava_Access, multiplicity=Multiplicity(0, 1))
    }
)
unknownDecl19: BinaryAssociation = BinaryAssociation(
    name="unknownDecl19",
    ends={
        Property(name="picojava_Decl21", type=picojava_TypeDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="picojava_TypeDecl20", type=picojava_Decl, multiplicity=Multiplicity(0, 1))
    }
)
Superclass22: BinaryAssociation = BinaryAssociation(
    name="Superclass22",
    ends={
        Property(name="picojava_IdUse", type=picojava_ClassDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="picojava_ClassDecl", type=picojava_IdUse, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Body23: BinaryAssociation = BinaryAssociation(
    name="Body23",
    ends={
        Property(name="picojava_Block25", type=picojava_ClassDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="picojava_ClassDecl24", type=picojava_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type42: BinaryAssociation = BinaryAssociation(
    name="type42",
    ends={
        Property(name="picojava_TypeDecl44", type=picojava_Exp, multiplicity=Multiplicity(1, 1)),
        Property(name="picojava_Exp43", type=picojava_TypeDecl, multiplicity=Multiplicity(0, 1))
    }
)
Value33: BinaryAssociation = BinaryAssociation(
    name="Value33",
    ends={
        Property(name="picojava_Exp", type=picojava_AssignStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="picojava_AssignStmt34", type=picojava_Exp, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
Condition35: BinaryAssociation = BinaryAssociation(
    name="Condition35",
    ends={
        Property(name="picojava_Exp36", type=picojava_WhileStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="picojava_WhileStmt", type=picojava_Exp, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
Body37: BinaryAssociation = BinaryAssociation(
    name="Body37",
    ends={
        Property(name="picojava_Stmt", type=picojava_WhileStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="picojava_WhileStmt38", type=picojava_Stmt, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
booleanType39: BinaryAssociation = BinaryAssociation(
    name="booleanType39",
    ends={
        Property(name="picojava_PrimitiveDecl41", type=picojava_WhileStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="picojava_WhileStmt40", type=picojava_PrimitiveDecl, multiplicity=Multiplicity(0, 1))
    }
)
qualifier48: BinaryAssociation = BinaryAssociation(
    name="qualifier48",
    ends={
        Property(name="picojava_Access50", type=picojava_IdUse, multiplicity=Multiplicity(1, 1)),
        Property(name="picojava_IdUse49", type=picojava_Access, multiplicity=Multiplicity(0, 1))
    }
)
decl45: BinaryAssociation = BinaryAssociation(
    name="decl45",
    ends={
        Property(name="picojava_Decl47", type=picojava_Access, multiplicity=Multiplicity(1, 1)),
        Property(name="picojava_Access46", type=picojava_Decl, multiplicity=Multiplicity(0, 1))
    }
)
ObjectReference51: BinaryAssociation = BinaryAssociation(
    name="ObjectReference51",
    ends={
        Property(name="picojava_Access52", type=picojava_Dot, multiplicity=Multiplicity(1, 1)),
        Property(name="picojava_Dot", type=picojava_Access, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
IdUse53: BinaryAssociation = BinaryAssociation(
    name="IdUse53",
    ends={
        Property(name="picojava_IdUse55", type=picojava_Dot, multiplicity=Multiplicity(1, 1)),
        Property(name="picojava_Dot54", type=picojava_IdUse, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
booleanType56: BinaryAssociation = BinaryAssociation(
    name="booleanType56",
    ends={
        Property(name="picojava_PrimitiveDecl57", type=picojava_BooleanLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="picojava_BooleanLiteral", type=picojava_PrimitiveDecl, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_picojava_Stmt_BlockStmt = Generalization(general=BlockStmt, specific=picojava_Stmt)
gen_picojava_Decl_BlockStmt = Generalization(general=BlockStmt, specific=picojava_Decl)
gen_picojava_TypeDecl_Decl = Generalization(general=Decl, specific=picojava_TypeDecl)
gen_picojava_VarDecl_Decl = Generalization(general=Decl, specific=picojava_VarDecl)
gen_picojava_AssignStmt_Stmt = Generalization(general=Stmt, specific=picojava_AssignStmt)
gen_picojava_ClassDecl_TypeDecl = Generalization(general=TypeDecl, specific=picojava_ClassDecl)
gen_picojava_WhileStmt_Stmt = Generalization(general=Stmt, specific=picojava_WhileStmt)
gen_picojava_Use_IdUse = Generalization(general=IdUse, specific=picojava_Use)
gen_picojava_Dot_Access = Generalization(general=Access, specific=picojava_Dot)
gen_picojava_Access_Exp = Generalization(general=Exp, specific=picojava_Access)
gen_picojava_IdUse_Access = Generalization(general=Access, specific=picojava_IdUse)
gen_picojava_BooleanLiteral_Exp = Generalization(general=Exp, specific=picojava_BooleanLiteral)
gen_picojava_PrimitiveDecl_TypeDecl = Generalization(general=TypeDecl, specific=picojava_PrimitiveDecl)
gen_picojava_UnknownDecl_TypeDecl = Generalization(general=TypeDecl, specific=picojava_UnknownDecl)
gen_picojava_TypeUse_IdUse = Generalization(general=IdUse, specific=picojava_TypeUse)
gen_picojava_VariableUse_IdUse = Generalization(general=IdUse, specific=picojava_VariableUse)

# Domain Model
domain_model = DomainModel(
    name="picojava",
    types={picojava_TypeDecl, picojava_UnknownDecl, picojava_PrimitiveDecl, picojava_Program, picojava_Block, picojava_Stmt, BlockStmt, picojava_BlockStmt, picojava_Decl, Decl, picojava_VarDecl, picojava_AssignStmt, Stmt, picojava_Access, picojava_ClassDecl, TypeDecl, picojava_IdUse, picojava_Exp, picojava_WhileStmt, picojava_Use, IdUse, picojava_Dot, Exp, Access, picojava_BooleanLiteral, picojava_TypeUse, picojava_VariableUse},
    associations={PredefinedType1, unknownDecl3, booleanType5, Block0, type11, BlockStmt7, unknownDecl9, booleanType14, superClass27, Type29, Variable31, qualifier17, unknownDecl19, Superclass22, Body23, type42, Value33, Condition35, Body37, booleanType39, qualifier48, decl45, ObjectReference51, IdUse53, booleanType56},
    generalizations={gen_picojava_Stmt_BlockStmt, gen_picojava_Decl_BlockStmt, gen_picojava_TypeDecl_Decl, gen_picojava_VarDecl_Decl, gen_picojava_AssignStmt_Stmt, gen_picojava_ClassDecl_TypeDecl, gen_picojava_WhileStmt_Stmt, gen_picojava_Use_IdUse, gen_picojava_Dot_Access, gen_picojava_Access_Exp, gen_picojava_IdUse_Access, gen_picojava_BooleanLiteral_Exp, gen_picojava_PrimitiveDecl_TypeDecl, gen_picojava_UnknownDecl_TypeDecl, gen_picojava_TypeUse_IdUse, gen_picojava_VariableUse_IdUse},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)