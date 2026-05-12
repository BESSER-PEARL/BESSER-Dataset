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
kbuild_Model = Class(name="kbuild_Model")
kbuild_Object_Y = Class(name="kbuild_Object_Y")
kbuild_Object_M = Class(name="kbuild_Object_M")
kbuild_Assign = Class(name="kbuild_Assign")
AssignExtra = Class(name="AssignExtra")
kbuild_Values = Class(name="kbuild_Values")
Assign = Class(name="Assign")
kbuild_Value = Class(name="kbuild_Value")
If = Class(name="If")
VarSlashSym = Class(name="VarSlashSym")
kbuild_ShellPart = Class(name="kbuild_ShellPart")
kbuild_VarSlashSym = Class(name="kbuild_VarSlashSym")
kbuild_BuildEntry = Class(name="kbuild_BuildEntry")
kbuild_EObject = Class(name="kbuild_EObject")
kbuild_Entry = Class(name="kbuild_Entry")
kbuild_Variable = Class(name="kbuild_Variable")
kbuild_AssignExtra = Class(name="kbuild_AssignExtra")
kbuild_If = Class(name="kbuild_If")
kbuild_ShellCmd = Class(name="kbuild_ShellCmd")
kbuild_Target = Class(name="kbuild_Target")
kbuild_MyVariable = Class(name="kbuild_MyVariable")
kbuild_Obj_y = Class(name="kbuild_Obj_y")
Object_Y = Class(name="Object_Y")
kbuild_Obj_m = Class(name="kbuild_Obj_m")
Object_M = Class(name="Object_M")
kbuild_ObjectFile = Class(name="kbuild_ObjectFile")
Value = Class(name="Value")
kbuild_IfEq = Class(name="kbuild_IfEq")
BuildEntry = Class(name="BuildEntry")
kbuild_IfNEq = Class(name="kbuild_IfNEq")
kbuild_Ifndef = Class(name="kbuild_Ifndef")
kbuild_HostProgram = Class(name="kbuild_HostProgram")
kbuild_Object = Class(name="kbuild_Object")
kbuild_ObjectSingleFile = Class(name="kbuild_ObjectSingleFile")
kbuild_ObjectVariable = Class(name="kbuild_ObjectVariable")
kbuild_ObjectShellCmd = Class(name="kbuild_ObjectShellCmd")
kbuild_ObjectString = Class(name="kbuild_ObjectString")
kbuild_ObjectShellChar = Class(name="kbuild_ObjectShellChar")
kbuild_ObjectDir = Class(name="kbuild_ObjectDir")
kbuild_Include = Class(name="kbuild_Include")
ShellCmd = Class(name="ShellCmd")

# kbuild_Model class attributes and methods

# kbuild_Object_Y class attributes and methods

# kbuild_Object_M class attributes and methods

# kbuild_Assign class attributes and methods

# AssignExtra class attributes and methods

# kbuild_Values class attributes and methods

# Assign class attributes and methods

# kbuild_Value class attributes and methods

# If class attributes and methods

# VarSlashSym class attributes and methods

# kbuild_ShellPart class attributes and methods

# kbuild_VarSlashSym class attributes and methods
kbuild_VarSlashSym_name: Property = Property(name="name", type=StringType)
kbuild_VarSlashSym.attributes={kbuild_VarSlashSym_name}

# kbuild_BuildEntry class attributes and methods

# kbuild_EObject class attributes and methods

# kbuild_Entry class attributes and methods

# kbuild_Variable class attributes and methods

# kbuild_AssignExtra class attributes and methods

# kbuild_If class attributes and methods

# kbuild_ShellCmd class attributes and methods
kbuild_ShellCmd_name: Property = Property(name="name", type=StringType)
kbuild_ShellCmd.attributes={kbuild_ShellCmd_name}

# kbuild_Target class attributes and methods

# kbuild_MyVariable class attributes and methods
kbuild_MyVariable_name: Property = Property(name="name", type=StringType)
kbuild_MyVariable.attributes={kbuild_MyVariable_name}

# kbuild_Obj_y class attributes and methods

# Object_Y class attributes and methods

# kbuild_Obj_m class attributes and methods

# Object_M class attributes and methods

# kbuild_ObjectFile class attributes and methods

# Value class attributes and methods

# kbuild_IfEq class attributes and methods

# BuildEntry class attributes and methods

# kbuild_IfNEq class attributes and methods

# kbuild_Ifndef class attributes and methods
kbuild_Ifndef_name: Property = Property(name="name", type=StringType)
kbuild_Ifndef.attributes={kbuild_Ifndef_name}

# kbuild_HostProgram class attributes and methods
kbuild_HostProgram_name: Property = Property(name="name", type=StringType)
kbuild_HostProgram.attributes={kbuild_HostProgram_name}

# kbuild_Object class attributes and methods

# kbuild_ObjectSingleFile class attributes and methods
kbuild_ObjectSingleFile_name: Property = Property(name="name", type=StringType)
kbuild_ObjectSingleFile.attributes={kbuild_ObjectSingleFile_name}

# kbuild_ObjectVariable class attributes and methods
kbuild_ObjectVariable_additional: Property = Property(name="additional", type=StringType)
kbuild_ObjectVariable.attributes={kbuild_ObjectVariable_additional}

# kbuild_ObjectShellCmd class attributes and methods

# kbuild_ObjectString class attributes and methods

# kbuild_ObjectShellChar class attributes and methods
kbuild_ObjectShellChar_value: Property = Property(name="value", type=StringType)
kbuild_ObjectShellChar.attributes={kbuild_ObjectShellChar_value}

# kbuild_ObjectDir class attributes and methods

# kbuild_Include class attributes and methods

# ShellCmd class attributes and methods

# Relationships
items13: BinaryAssociation = BinaryAssociation(
    name="items13",
    ends={
        Property(name="kbuild_Value", type=kbuild_Values, multiplicity=Multiplicity(1, 1)),
        Property(name="kbuild_Values", type=kbuild_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
shellPart14: BinaryAssociation = BinaryAssociation(
    name="shellPart14",
    ends={
        Property(name="kbuild_ShellPart", type=kbuild_ShellCmd, multiplicity=Multiplicity(1, 1)),
        Property(name="kbuild_ShellCmd15", type=kbuild_ShellPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
val16: BinaryAssociation = BinaryAssociation(
    name="val16",
    ends={
        Property(name="kbuild_VarSlashSym", type=kbuild_ShellPart, multiplicity=Multiplicity(1, 1)),
        Property(name="kbuild_ShellPart17", type=kbuild_VarSlashSym, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
buildEntry0: BinaryAssociation = BinaryAssociation(
    name="buildEntry0",
    ends={
        Property(name="kbuild_BuildEntry", type=kbuild_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="kbuild_Model", type=kbuild_BuildEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value1: BinaryAssociation = BinaryAssociation(
    name="value1",
    ends={
        Property(name="kbuild_EObject", type=kbuild_BuildEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="kbuild_BuildEntry2", type=kbuild_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable3: BinaryAssociation = BinaryAssociation(
    name="variable3",
    ends={
        Property(name="kbuild_Variable", type=kbuild_Entry, multiplicity=Multiplicity(1, 1)),
        Property(name="kbuild_Entry", type=kbuild_Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value4: BinaryAssociation = BinaryAssociation(
    name="value4",
    ends={
        Property(name="kbuild_AssignExtra", type=kbuild_Entry, multiplicity=Multiplicity(1, 1)),
        Property(name="kbuild_Entry5", type=kbuild_AssignExtra, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
shell6: BinaryAssociation = BinaryAssociation(
    name="shell6",
    ends={
        Property(name="kbuild_ShellCmd", type=kbuild_If, multiplicity=Multiplicity(1, 1)),
        Property(name="kbuild_If", type=kbuild_ShellCmd, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value7: BinaryAssociation = BinaryAssociation(
    name="value7",
    ends={
        Property(name="kbuild_EObject9", type=kbuild_If, multiplicity=Multiplicity(1, 1)),
        Property(name="kbuild_If8", type=kbuild_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elsevalue10: BinaryAssociation = BinaryAssociation(
    name="elsevalue10",
    ends={
        Property(name="kbuild_EObject12", type=kbuild_If, multiplicity=Multiplicity(1, 1)),
        Property(name="kbuild_If11", type=kbuild_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target25: BinaryAssociation = BinaryAssociation(
    name="target25",
    ends={
        Property(name="kbuild_Values26", type=kbuild_Target, multiplicity=Multiplicity(1, 1)),
        Property(name="kbuild_Target", type=kbuild_Values, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
values27: BinaryAssociation = BinaryAssociation(
    name="values27",
    ends={
        Property(name="kbuild_Values29", type=kbuild_Target, multiplicity=Multiplicity(1, 1)),
        Property(name="kbuild_Target28", type=kbuild_Values, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable30: BinaryAssociation = BinaryAssociation(
    name="variable30",
    ends={
        Property(name="kbuild_Variable31", type=kbuild_MyVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="kbuild_MyVariable", type=kbuild_Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value32: BinaryAssociation = BinaryAssociation(
    name="value32",
    ends={
        Property(name="kbuild_AssignExtra33", type=kbuild_Obj_y, multiplicity=Multiplicity(1, 1)),
        Property(name="kbuild_Obj_y", type=kbuild_AssignExtra, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value34: BinaryAssociation = BinaryAssociation(
    name="value34",
    ends={
        Property(name="kbuild_AssignExtra35", type=kbuild_Obj_m, multiplicity=Multiplicity(1, 1)),
        Property(name="kbuild_Obj_m", type=kbuild_AssignExtra, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cmd18: BinaryAssociation = BinaryAssociation(
    name="cmd18",
    ends={
        Property(name="kbuild_ShellCmd20", type=kbuild_ShellPart, multiplicity=Multiplicity(1, 1)),
        Property(name="kbuild_ShellPart19", type=kbuild_ShellCmd, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable21: BinaryAssociation = BinaryAssociation(
    name="variable21",
    ends={
        Property(name="kbuild_Variable22", type=kbuild_HostProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="kbuild_HostProgram", type=kbuild_Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
inner23: BinaryAssociation = BinaryAssociation(
    name="inner23",
    ends={
        Property(name="kbuild_Assign", type=kbuild_HostProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="kbuild_HostProgram24", type=kbuild_Assign, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value36: BinaryAssociation = BinaryAssociation(
    name="value36",
    ends={
        Property(name="kbuild_Variable37", type=kbuild_ObjectVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="kbuild_ObjectVariable", type=kbuild_Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value38: BinaryAssociation = BinaryAssociation(
    name="value38",
    ends={
        Property(name="kbuild_ShellCmd39", type=kbuild_ObjectShellCmd, multiplicity=Multiplicity(1, 1)),
        Property(name="kbuild_ObjectShellCmd", type=kbuild_ShellCmd, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_kbuild_Assign_AssignExtra = Generalization(general=AssignExtra, specific=kbuild_Assign)
gen_kbuild_Values_Assign = Generalization(general=Assign, specific=kbuild_Values)
gen_kbuild_Variable_If = Generalization(general=If, specific=kbuild_Variable)
gen_kbuild_Variable_VarSlashSym = Generalization(general=VarSlashSym, specific=kbuild_Variable)
gen_kbuild_Target_BuildEntry = Generalization(general=BuildEntry, specific=kbuild_Target)
gen_kbuild_MyVariable_BuildEntry = Generalization(general=BuildEntry, specific=kbuild_MyVariable)
gen_kbuild_Obj_y_Object_Y = Generalization(general=Object_Y, specific=kbuild_Obj_y)
gen_kbuild_Obj_m_Object_M = Generalization(general=Object_M, specific=kbuild_Obj_m)
gen_kbuild_ObjectFile_Value = Generalization(general=Value, specific=kbuild_ObjectFile)
gen_kbuild_IfEq_BuildEntry = Generalization(general=BuildEntry, specific=kbuild_IfEq)
gen_kbuild_IfNEq_BuildEntry = Generalization(general=BuildEntry, specific=kbuild_IfNEq)
gen_kbuild_Ifndef_BuildEntry = Generalization(general=BuildEntry, specific=kbuild_Ifndef)
gen_kbuild_HostProgram_BuildEntry = Generalization(general=BuildEntry, specific=kbuild_HostProgram)
gen_kbuild_Object_BuildEntry = Generalization(general=BuildEntry, specific=kbuild_Object)
gen_kbuild_ObjectSingleFile_Value = Generalization(general=Value, specific=kbuild_ObjectSingleFile)
gen_kbuild_ObjectVariable_Value = Generalization(general=Value, specific=kbuild_ObjectVariable)
gen_kbuild_ObjectShellCmd_Value = Generalization(general=Value, specific=kbuild_ObjectShellCmd)
gen_kbuild_ObjectString_Value = Generalization(general=Value, specific=kbuild_ObjectString)
gen_kbuild_ObjectShellChar_Value = Generalization(general=Value, specific=kbuild_ObjectShellChar)
gen_kbuild_ObjectDir_Value = Generalization(general=Value, specific=kbuild_ObjectDir)
gen_kbuild_Include_ShellCmd = Generalization(general=ShellCmd, specific=kbuild_Include)

# Domain Model
domain_model = DomainModel(
    name="kbuild",
    types={kbuild_Model, kbuild_Object_Y, kbuild_Object_M, kbuild_Assign, AssignExtra, kbuild_Values, Assign, kbuild_Value, If, VarSlashSym, kbuild_ShellPart, kbuild_VarSlashSym, kbuild_BuildEntry, kbuild_EObject, kbuild_Entry, kbuild_Variable, kbuild_AssignExtra, kbuild_If, kbuild_ShellCmd, kbuild_Target, kbuild_MyVariable, kbuild_Obj_y, Object_Y, kbuild_Obj_m, Object_M, kbuild_ObjectFile, Value, kbuild_IfEq, BuildEntry, kbuild_IfNEq, kbuild_Ifndef, kbuild_HostProgram, kbuild_Object, kbuild_ObjectSingleFile, kbuild_ObjectVariable, kbuild_ObjectShellCmd, kbuild_ObjectString, kbuild_ObjectShellChar, kbuild_ObjectDir, kbuild_Include, ShellCmd},
    associations={items13, shellPart14, val16, buildEntry0, value1, variable3, value4, shell6, value7, elsevalue10, target25, values27, variable30, value32, value34, cmd18, variable21, inner23, value36, value38},
    generalizations={gen_kbuild_Assign_AssignExtra, gen_kbuild_Values_Assign, gen_kbuild_Variable_If, gen_kbuild_Variable_VarSlashSym, gen_kbuild_Target_BuildEntry, gen_kbuild_MyVariable_BuildEntry, gen_kbuild_Obj_y_Object_Y, gen_kbuild_Obj_m_Object_M, gen_kbuild_ObjectFile_Value, gen_kbuild_IfEq_BuildEntry, gen_kbuild_IfNEq_BuildEntry, gen_kbuild_Ifndef_BuildEntry, gen_kbuild_HostProgram_BuildEntry, gen_kbuild_Object_BuildEntry, gen_kbuild_ObjectSingleFile_Value, gen_kbuild_ObjectVariable_Value, gen_kbuild_ObjectShellCmd_Value, gen_kbuild_ObjectString_Value, gen_kbuild_ObjectShellChar_Value, gen_kbuild_ObjectDir_Value, gen_kbuild_Include_ShellCmd},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)