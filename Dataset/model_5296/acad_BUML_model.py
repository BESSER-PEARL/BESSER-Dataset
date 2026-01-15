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
HardGoal = Class(name="HardGoal")
acad_G_CallTaking = Class(name="acad::G::CallTaking")
acad_G_GenDispatch = Class(name="acad::G::GenDispatch")
acad_T_DispDepArriv = Class(name="acad::T::DispDepArriv")
acad_T_ReplAmb = Class(name="acad::T::ReplAmb")
acad_D_DataUpd = Class(name="acad::D::DataUpd")
DomainAssumption = Class(name="DomainAssumption")
acad_G_ResourceId = Class(name="acad::G::ResourceId")
acad_G_ResourceMob = Class(name="acad::G::ResourceMob")
acad_G_ObtainMap = Class(name="acad::G::ObtainMap")
acad_G_IncidentUpd = Class(name="acad::G::IncidentUpd")
acad_D_MaxCalls = Class(name="acad::D::MaxCalls")
acad_G_RegCall = Class(name="acad::G::RegCall")
acad_T_ConfirmCall = Class(name="acad::T::ConfirmCall")
Task = Class(name="Task")
acad_G_AssignIncident = Class(name="acad::G::AssignIncident")
acad_T_SearchDuplic = Class(name="acad::T::SearchDuplic")
acad_T_CreateOrAssign = Class(name="acad::T::CreateOrAssign")
acad_T_InputInfo = Class(name="acad::T::InputInfo")
acad_T_DetectLoc = Class(name="acad::T::DetectLoc")
acad_T_SpecConfig = Class(name="acad::T::SpecConfig")
acad_T_ConfIncident = Class(name="acad::T::ConfIncident")
acad_T_DetBestAmb = Class(name="acad::T::DetBestAmb")
acad_T_InformStat = Class(name="acad::T::InformStat")
acad_G_RouteAssist = Class(name="acad::G::RouteAssist")
acad_D_DriverKnows = Class(name="acad::D::DriverKnows")
acad_T_AcadAssists = Class(name="acad::T::AcadAssists")
acad_T_StaffAssists = Class(name="acad::T::StaffAssists")
acad_T_Feedback = Class(name="acad::T::Feedback")
acad_D_GazetUpd = Class(name="acad::D::GazetUpd")
acad_G_ManualMap = Class(name="acad::G::ManualMap")
acad_T_CheckGazet = Class(name="acad::T::CheckGazet")
acad_T_CheckPaper = Class(name="acad::T::CheckPaper")
acad_G_DispExcept = Class(name="acad::G::DispExcept")
acad_G_MonitorRes = Class(name="acad::G::MonitorRes")
acad_G_UpdPosition = Class(name="acad::G::UpdPosition")
acad_D_MDTPos = Class(name="acad::D::MDTPos")
acad_T_RadioPos = Class(name="acad::T::RadioPos")
acad_D_MDTUse = Class(name="acad::D::MDTUse")
acad_T_MonitorStatus = Class(name="acad::T::MonitorStatus")
acad_T_DispStatus = Class(name="acad::T::DispStatus")
acad_T_Except = Class(name="acad::T::Except")
acad_T_ExceptQueue = Class(name="acad::T::ExceptQueue")
acad_T_CloseIncident = Class(name="acad::T::CloseIncident")
acad_S_FastDispatch = Class(name="acad::S::FastDispatch")
Softgoal = Class(name="Softgoal")
acad_Q_Dispatch = Class(name="acad::Q::Dispatch")
QualityConstraint = Class(name="QualityConstraint")
acad_S_FastAssist = Class(name="acad::S::FastAssist")
acad_Q_IncidResolv = Class(name="acad::Q::IncidResolv")
acad_S_FastArriv = Class(name="acad::S::FastArriv")
acad_Q_AmbArriv = Class(name="acad::Q::AmbArriv")
acad_S_LowCost = Class(name="acad::S::LowCost")
acad_Q_MaxCost = Class(name="acad::Q::MaxCost")
acad_S_UserFriendly = Class(name="acad::S::UserFriendly")
acad_Q_MaxTimeMsg = Class(name="acad::Q::MaxTimeMsg")
acad_AR1 = Class(name="acad::AR1")
EcaAwReq = Class(name="EcaAwReq")
acad_AR2 = Class(name="acad::AR2")
acad_AR3 = Class(name="acad::AR3")
acad_AR4 = Class(name="acad::AR4")
acad_AR5 = Class(name="acad::AR5")
acad_AR6 = Class(name="acad::AR6")
acad_AR7 = Class(name="acad::AR7")
acad_AR8 = Class(name="acad::AR8")
acad_AR9 = Class(name="acad::AR9")
acad_AR10 = Class(name="acad::AR10")
acad_AR11 = Class(name="acad::AR11")
acad_AR12 = Class(name="acad::AR12")
acad_AR13 = Class(name="acad::AR13")
acad_AR14 = Class(name="acad::AR14")
Parameter_ = Class(name="Parameter")
acad_AR15 = Class(name="acad::AR15")
acad_AcadGoalModel = Class(name="acad::AcadGoalModel")
GoalModel = Class(name="GoalModel")
acad_CV_MST = Class(name="acad::CV::MST")

# HardGoal class attributes and methods

# acad_G_CallTaking class attributes and methods

# acad_G_GenDispatch class attributes and methods

# acad_T_DispDepArriv class attributes and methods

# acad_T_ReplAmb class attributes and methods

# acad_D_DataUpd class attributes and methods

# DomainAssumption class attributes and methods

# acad_G_ResourceId class attributes and methods

# acad_G_ResourceMob class attributes and methods

# acad_G_ObtainMap class attributes and methods

# acad_G_IncidentUpd class attributes and methods

# acad_D_MaxCalls class attributes and methods

# acad_G_RegCall class attributes and methods

# acad_T_ConfirmCall class attributes and methods

# Task class attributes and methods

# acad_G_AssignIncident class attributes and methods

# acad_T_SearchDuplic class attributes and methods

# acad_T_CreateOrAssign class attributes and methods

# acad_T_InputInfo class attributes and methods

# acad_T_DetectLoc class attributes and methods

# acad_T_SpecConfig class attributes and methods

# acad_T_ConfIncident class attributes and methods

# acad_T_DetBestAmb class attributes and methods

# acad_T_InformStat class attributes and methods

# acad_G_RouteAssist class attributes and methods

# acad_D_DriverKnows class attributes and methods

# acad_T_AcadAssists class attributes and methods

# acad_T_StaffAssists class attributes and methods

# acad_T_Feedback class attributes and methods

# acad_D_GazetUpd class attributes and methods

# acad_G_ManualMap class attributes and methods

# acad_T_CheckGazet class attributes and methods

# acad_T_CheckPaper class attributes and methods

# acad_G_DispExcept class attributes and methods

# acad_G_MonitorRes class attributes and methods

# acad_G_UpdPosition class attributes and methods

# acad_D_MDTPos class attributes and methods

# acad_T_RadioPos class attributes and methods

# acad_D_MDTUse class attributes and methods

# acad_T_MonitorStatus class attributes and methods

# acad_T_DispStatus class attributes and methods

# acad_T_Except class attributes and methods

# acad_T_ExceptQueue class attributes and methods

# acad_T_CloseIncident class attributes and methods

# acad_S_FastDispatch class attributes and methods

# Softgoal class attributes and methods

# acad_Q_Dispatch class attributes and methods

# QualityConstraint class attributes and methods

# acad_S_FastAssist class attributes and methods

# acad_Q_IncidResolv class attributes and methods

# acad_S_FastArriv class attributes and methods

# acad_Q_AmbArriv class attributes and methods

# acad_S_LowCost class attributes and methods

# acad_Q_MaxCost class attributes and methods

# acad_S_UserFriendly class attributes and methods

# acad_Q_MaxTimeMsg class attributes and methods

# acad_AR1 class attributes and methods

# EcaAwReq class attributes and methods

# acad_AR2 class attributes and methods

# acad_AR3 class attributes and methods

# acad_AR4 class attributes and methods

# acad_AR5 class attributes and methods

# acad_AR6 class attributes and methods

# acad_AR7 class attributes and methods

# acad_AR8 class attributes and methods

# acad_AR9 class attributes and methods

# acad_AR10 class attributes and methods

# acad_AR11 class attributes and methods

# acad_AR12 class attributes and methods

# acad_AR13 class attributes and methods

# acad_AR14 class attributes and methods

# Parameter class attributes and methods

# acad_AR15 class attributes and methods

# acad_AcadGoalModel class attributes and methods

# GoalModel class attributes and methods

# acad_CV_MST class attributes and methods

# Generalizations
gen_acad_G_GenDispatch_HardGoal = Generalization(general=HardGoal, specific=acad_G_GenDispatch)
gen_acad_G_CallTaking_HardGoal = Generalization(general=HardGoal, specific=acad_G_CallTaking)
gen_acad_T_DispStatus_Task = Generalization(general=Task, specific=acad_T_DispStatus)
gen_acad_T_DispDepArriv_Task = Generalization(general=Task, specific=acad_T_DispDepArriv)
gen_acad_T_ReplAmb_Task = Generalization(general=Task, specific=acad_T_ReplAmb)
gen_acad_D_DataUpd_DomainAssumption = Generalization(general=DomainAssumption, specific=acad_D_DataUpd)
gen_acad_G_ResourceId_HardGoal = Generalization(general=HardGoal, specific=acad_G_ResourceId)
gen_acad_G_ResourceMob_HardGoal = Generalization(general=HardGoal, specific=acad_G_ResourceMob)
gen_acad_G_ObtainMap_HardGoal = Generalization(general=HardGoal, specific=acad_G_ObtainMap)
gen_acad_G_IncidentUpd_HardGoal = Generalization(general=HardGoal, specific=acad_G_IncidentUpd)
gen_acad_D_MaxCalls_DomainAssumption = Generalization(general=DomainAssumption, specific=acad_D_MaxCalls)
gen_acad_G_RegCall_HardGoal = Generalization(general=HardGoal, specific=acad_G_RegCall)
gen_acad_T_ConfirmCall_Task = Generalization(general=Task, specific=acad_T_ConfirmCall)
gen_acad_G_AssignIncident_HardGoal = Generalization(general=HardGoal, specific=acad_G_AssignIncident)
gen_acad_T_SearchDuplic_Task = Generalization(general=Task, specific=acad_T_SearchDuplic)
gen_acad_T_CreateOrAssign_Task = Generalization(general=Task, specific=acad_T_CreateOrAssign)
gen_acad_T_InputInfo_Task = Generalization(general=Task, specific=acad_T_InputInfo)
gen_acad_T_DetectLoc_Task = Generalization(general=Task, specific=acad_T_DetectLoc)
gen_acad_T_SpecConfig_Task = Generalization(general=Task, specific=acad_T_SpecConfig)
gen_acad_T_ConfIncident_Task = Generalization(general=Task, specific=acad_T_ConfIncident)
gen_acad_T_DetBestAmb_Task = Generalization(general=Task, specific=acad_T_DetBestAmb)
gen_acad_T_InformStat_Task = Generalization(general=Task, specific=acad_T_InformStat)
gen_acad_G_RouteAssist_HardGoal = Generalization(general=HardGoal, specific=acad_G_RouteAssist)
gen_acad_D_DriverKnows_DomainAssumption = Generalization(general=DomainAssumption, specific=acad_D_DriverKnows)
gen_acad_T_AcadAssists_Task = Generalization(general=Task, specific=acad_T_AcadAssists)
gen_acad_T_StaffAssists_Task = Generalization(general=Task, specific=acad_T_StaffAssists)
gen_acad_T_Feedback_Task = Generalization(general=Task, specific=acad_T_Feedback)
gen_acad_D_GazetUpd_DomainAssumption = Generalization(general=DomainAssumption, specific=acad_D_GazetUpd)
gen_acad_G_ManualMap_HardGoal = Generalization(general=HardGoal, specific=acad_G_ManualMap)
gen_acad_T_CheckGazet_Task = Generalization(general=Task, specific=acad_T_CheckGazet)
gen_acad_T_CheckPaper_Task = Generalization(general=Task, specific=acad_T_CheckPaper)
gen_acad_G_DispExcept_HardGoal = Generalization(general=HardGoal, specific=acad_G_DispExcept)
gen_acad_G_MonitorRes_HardGoal = Generalization(general=HardGoal, specific=acad_G_MonitorRes)
gen_acad_G_UpdPosition_HardGoal = Generalization(general=HardGoal, specific=acad_G_UpdPosition)
gen_acad_D_MDTPos_DomainAssumption = Generalization(general=DomainAssumption, specific=acad_D_MDTPos)
gen_acad_T_RadioPos_Task = Generalization(general=Task, specific=acad_T_RadioPos)
gen_acad_D_MDTUse_DomainAssumption = Generalization(general=DomainAssumption, specific=acad_D_MDTUse)
gen_acad_T_MonitorStatus_Task = Generalization(general=Task, specific=acad_T_MonitorStatus)
gen_acad_T_Except_Task = Generalization(general=Task, specific=acad_T_Except)
gen_acad_T_ExceptQueue_Task = Generalization(general=Task, specific=acad_T_ExceptQueue)
gen_acad_T_CloseIncident_Task = Generalization(general=Task, specific=acad_T_CloseIncident)
gen_acad_S_FastDispatch_Softgoal = Generalization(general=Softgoal, specific=acad_S_FastDispatch)
gen_acad_Q_Dispatch_QualityConstraint = Generalization(general=QualityConstraint, specific=acad_Q_Dispatch)
gen_acad_S_FastAssist_Softgoal = Generalization(general=Softgoal, specific=acad_S_FastAssist)
gen_acad_Q_IncidResolv_QualityConstraint = Generalization(general=QualityConstraint, specific=acad_Q_IncidResolv)
gen_acad_S_FastArriv_Softgoal = Generalization(general=Softgoal, specific=acad_S_FastArriv)
gen_acad_Q_AmbArriv_QualityConstraint = Generalization(general=QualityConstraint, specific=acad_Q_AmbArriv)
gen_acad_S_LowCost_Softgoal = Generalization(general=Softgoal, specific=acad_S_LowCost)
gen_acad_Q_MaxCost_QualityConstraint = Generalization(general=QualityConstraint, specific=acad_Q_MaxCost)
gen_acad_S_UserFriendly_Softgoal = Generalization(general=Softgoal, specific=acad_S_UserFriendly)
gen_acad_Q_MaxTimeMsg_QualityConstraint = Generalization(general=QualityConstraint, specific=acad_Q_MaxTimeMsg)
gen_acad_AR1_EcaAwReq = Generalization(general=EcaAwReq, specific=acad_AR1)
gen_acad_AR2_EcaAwReq = Generalization(general=EcaAwReq, specific=acad_AR2)
gen_acad_AR3_EcaAwReq = Generalization(general=EcaAwReq, specific=acad_AR3)
gen_acad_AR4_EcaAwReq = Generalization(general=EcaAwReq, specific=acad_AR4)
gen_acad_AR5_EcaAwReq = Generalization(general=EcaAwReq, specific=acad_AR5)
gen_acad_AR6_EcaAwReq = Generalization(general=EcaAwReq, specific=acad_AR6)
gen_acad_AR7_EcaAwReq = Generalization(general=EcaAwReq, specific=acad_AR7)
gen_acad_AR8_EcaAwReq = Generalization(general=EcaAwReq, specific=acad_AR8)
gen_acad_AR9_EcaAwReq = Generalization(general=EcaAwReq, specific=acad_AR9)
gen_acad_AR10_EcaAwReq = Generalization(general=EcaAwReq, specific=acad_AR10)
gen_acad_AR11_EcaAwReq = Generalization(general=EcaAwReq, specific=acad_AR11)
gen_acad_AR12_EcaAwReq = Generalization(general=EcaAwReq, specific=acad_AR12)
gen_acad_AR13_EcaAwReq = Generalization(general=EcaAwReq, specific=acad_AR13)
gen_acad_AR14_EcaAwReq = Generalization(general=EcaAwReq, specific=acad_AR14)
gen_acad_AR15_EcaAwReq = Generalization(general=EcaAwReq, specific=acad_AR15)
gen_acad_CV_MST_Parameter = Generalization(general=Parameter_, specific=acad_CV_MST)
gen_acad_AcadGoalModel_GoalModel = Generalization(general=GoalModel, specific=acad_AcadGoalModel)

# Domain Model
domain_model = DomainModel(
    name="acad",
    types={HardGoal, acad_G_CallTaking, acad_G_GenDispatch, acad_T_DispDepArriv, acad_T_ReplAmb, acad_D_DataUpd, DomainAssumption, acad_G_ResourceId, acad_G_ResourceMob, acad_G_ObtainMap, acad_G_IncidentUpd, acad_D_MaxCalls, acad_G_RegCall, acad_T_ConfirmCall, Task, acad_G_AssignIncident, acad_T_SearchDuplic, acad_T_CreateOrAssign, acad_T_InputInfo, acad_T_DetectLoc, acad_T_SpecConfig, acad_T_ConfIncident, acad_T_DetBestAmb, acad_T_InformStat, acad_G_RouteAssist, acad_D_DriverKnows, acad_T_AcadAssists, acad_T_StaffAssists, acad_T_Feedback, acad_D_GazetUpd, acad_G_ManualMap, acad_T_CheckGazet, acad_T_CheckPaper, acad_G_DispExcept, acad_G_MonitorRes, acad_G_UpdPosition, acad_D_MDTPos, acad_T_RadioPos, acad_D_MDTUse, acad_T_MonitorStatus, acad_T_DispStatus, acad_T_Except, acad_T_ExceptQueue, acad_T_CloseIncident, acad_S_FastDispatch, Softgoal, acad_Q_Dispatch, QualityConstraint, acad_S_FastAssist, acad_Q_IncidResolv, acad_S_FastArriv, acad_Q_AmbArriv, acad_S_LowCost, acad_Q_MaxCost, acad_S_UserFriendly, acad_Q_MaxTimeMsg, acad_AR1, EcaAwReq, acad_AR2, acad_AR3, acad_AR4, acad_AR5, acad_AR6, acad_AR7, acad_AR8, acad_AR9, acad_AR10, acad_AR11, acad_AR12, acad_AR13, acad_AR14, Parameter_, acad_AR15, acad_AcadGoalModel, GoalModel, acad_CV_MST},
    associations={},
    generalizations={gen_acad_G_GenDispatch_HardGoal, gen_acad_G_CallTaking_HardGoal, gen_acad_T_DispStatus_Task, gen_acad_T_DispDepArriv_Task, gen_acad_T_ReplAmb_Task, gen_acad_D_DataUpd_DomainAssumption, gen_acad_G_ResourceId_HardGoal, gen_acad_G_ResourceMob_HardGoal, gen_acad_G_ObtainMap_HardGoal, gen_acad_G_IncidentUpd_HardGoal, gen_acad_D_MaxCalls_DomainAssumption, gen_acad_G_RegCall_HardGoal, gen_acad_T_ConfirmCall_Task, gen_acad_G_AssignIncident_HardGoal, gen_acad_T_SearchDuplic_Task, gen_acad_T_CreateOrAssign_Task, gen_acad_T_InputInfo_Task, gen_acad_T_DetectLoc_Task, gen_acad_T_SpecConfig_Task, gen_acad_T_ConfIncident_Task, gen_acad_T_DetBestAmb_Task, gen_acad_T_InformStat_Task, gen_acad_G_RouteAssist_HardGoal, gen_acad_D_DriverKnows_DomainAssumption, gen_acad_T_AcadAssists_Task, gen_acad_T_StaffAssists_Task, gen_acad_T_Feedback_Task, gen_acad_D_GazetUpd_DomainAssumption, gen_acad_G_ManualMap_HardGoal, gen_acad_T_CheckGazet_Task, gen_acad_T_CheckPaper_Task, gen_acad_G_DispExcept_HardGoal, gen_acad_G_MonitorRes_HardGoal, gen_acad_G_UpdPosition_HardGoal, gen_acad_D_MDTPos_DomainAssumption, gen_acad_T_RadioPos_Task, gen_acad_D_MDTUse_DomainAssumption, gen_acad_T_MonitorStatus_Task, gen_acad_T_Except_Task, gen_acad_T_ExceptQueue_Task, gen_acad_T_CloseIncident_Task, gen_acad_S_FastDispatch_Softgoal, gen_acad_Q_Dispatch_QualityConstraint, gen_acad_S_FastAssist_Softgoal, gen_acad_Q_IncidResolv_QualityConstraint, gen_acad_S_FastArriv_Softgoal, gen_acad_Q_AmbArriv_QualityConstraint, gen_acad_S_LowCost_Softgoal, gen_acad_Q_MaxCost_QualityConstraint, gen_acad_S_UserFriendly_Softgoal, gen_acad_Q_MaxTimeMsg_QualityConstraint, gen_acad_AR1_EcaAwReq, gen_acad_AR2_EcaAwReq, gen_acad_AR3_EcaAwReq, gen_acad_AR4_EcaAwReq, gen_acad_AR5_EcaAwReq, gen_acad_AR6_EcaAwReq, gen_acad_AR7_EcaAwReq, gen_acad_AR8_EcaAwReq, gen_acad_AR9_EcaAwReq, gen_acad_AR10_EcaAwReq, gen_acad_AR11_EcaAwReq, gen_acad_AR12_EcaAwReq, gen_acad_AR13_EcaAwReq, gen_acad_AR14_EcaAwReq, gen_acad_AR15_EcaAwReq, gen_acad_CV_MST_Parameter, gen_acad_AcadGoalModel_GoalModel},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)