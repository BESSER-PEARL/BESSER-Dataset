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
top_C = Class(name="top::C")
BChild = Class(name="BChild")
top_CChild = Class(name="top::CChild", is_abstract=True)
top_D = Class(name="top::D")
CChild = Class(name="CChild")
top_Expr = Class(name="top::Expr")
top_ExprChild = Class(name="top::ExprChild", is_abstract=True)
top_A = Class(name="top::A")
ExprChild = Class(name="ExprChild")
top_AChild = Class(name="top::AChild", is_abstract=True)
top_B = Class(name="top::B")
AChild = Class(name="AChild")
top_BChild = Class(name="top::BChild", is_abstract=True)
top_GChild = Class(name="top::GChild", is_abstract=True)
top_H = Class(name="top::H")
GChild = Class(name="GChild")
top_HChild = Class(name="top::HChild", is_abstract=True)
top_DChild = Class(name="top::DChild", is_abstract=True)
top_E = Class(name="top::E")
DChild = Class(name="DChild")
top_EChild = Class(name="top::EChild", is_abstract=True)
top_F = Class(name="top::F")
EChild = Class(name="EChild")
top_FChild = Class(name="top::FChild", is_abstract=True)
top_G = Class(name="top::G")
FChild = Class(name="FChild")
top_L = Class(name="top::L")
KChild = Class(name="KChild")
top_LChild = Class(name="top::LChild", is_abstract=True)
top_M = Class(name="top::M")
LChild = Class(name="LChild")
top_MChild = Class(name="top::MChild", is_abstract=True)
top_I = Class(name="top::I")
HChild = Class(name="HChild")
top_IChild = Class(name="top::IChild", is_abstract=True)
top_J = Class(name="top::J")
IChild = Class(name="IChild")
top_JChild = Class(name="top::JChild", is_abstract=True)
top_K = Class(name="top::K")
JChild = Class(name="JChild")
top_KChild = Class(name="top::KChild", is_abstract=True)
top_PChild = Class(name="top::PChild", is_abstract=True)
top_Q = Class(name="top::Q")
PChild = Class(name="PChild")
top_QChild = Class(name="top::QChild", is_abstract=True)
top_N = Class(name="top::N")
MChild = Class(name="MChild")
top_NChild = Class(name="top::NChild", is_abstract=True)
top_O = Class(name="top::O")
NChild = Class(name="NChild")
top_OChild = Class(name="top::OChild", is_abstract=True)
top_P = Class(name="top::P")
OChild = Class(name="OChild")
top_U = Class(name="top::U")
TChild = Class(name="TChild")
top_UChild = Class(name="top::UChild", is_abstract=True)
top_V = Class(name="top::V")
UChild = Class(name="UChild")
top_R = Class(name="top::R")
QChild = Class(name="QChild")
top_RChild = Class(name="top::RChild", is_abstract=True)
top_S = Class(name="top::S")
RChild = Class(name="RChild")
top_SChild = Class(name="top::SChild", is_abstract=True)
top_T = Class(name="top::T")
SChild = Class(name="SChild")
top_TChild = Class(name="top::TChild", is_abstract=True)
top_YChild = Class(name="top::YChild", is_abstract=True)
top_Z = Class(name="top::Z")
YChild = Class(name="YChild")
top_ZChild = Class(name="top::ZChild", is_abstract=True)
top_VChild = Class(name="top::VChild", is_abstract=True)
top_W = Class(name="top::W")
VChild = Class(name="VChild")
top_WChild = Class(name="top::WChild", is_abstract=True)
top_X = Class(name="top::X")
WChild = Class(name="WChild")
top_XChild = Class(name="top::XChild", is_abstract=True)
top_Y = Class(name="top::Y")
XChild = Class(name="XChild")
top_IntegerLiteral = Class(name="top::IntegerLiteral")
ZChild = Class(name="ZChild")

# top_C class attributes and methods

# BChild class attributes and methods

# top_CChild class attributes and methods

# top_D class attributes and methods

# CChild class attributes and methods

# top_Expr class attributes and methods

# top_ExprChild class attributes and methods

# top_A class attributes and methods

# ExprChild class attributes and methods

# top_AChild class attributes and methods

# top_B class attributes and methods

# AChild class attributes and methods

# top_BChild class attributes and methods

# top_GChild class attributes and methods

# top_H class attributes and methods

# GChild class attributes and methods

# top_HChild class attributes and methods

# top_DChild class attributes and methods

# top_E class attributes and methods

# DChild class attributes and methods

# top_EChild class attributes and methods

# top_F class attributes and methods

# EChild class attributes and methods

# top_FChild class attributes and methods

# top_G class attributes and methods

# FChild class attributes and methods

# top_L class attributes and methods

# KChild class attributes and methods

# top_LChild class attributes and methods

# top_M class attributes and methods

# LChild class attributes and methods

# top_MChild class attributes and methods

# top_I class attributes and methods

# HChild class attributes and methods

# top_IChild class attributes and methods

# top_J class attributes and methods

# IChild class attributes and methods

# top_JChild class attributes and methods

# top_K class attributes and methods

# JChild class attributes and methods

# top_KChild class attributes and methods

# top_PChild class attributes and methods

# top_Q class attributes and methods

# PChild class attributes and methods

# top_QChild class attributes and methods

# top_N class attributes and methods

# MChild class attributes and methods

# top_NChild class attributes and methods

# top_O class attributes and methods

# NChild class attributes and methods

# top_OChild class attributes and methods

# top_P class attributes and methods

# OChild class attributes and methods

# top_U class attributes and methods

# TChild class attributes and methods

# top_UChild class attributes and methods

# top_V class attributes and methods

# UChild class attributes and methods

# top_R class attributes and methods

# QChild class attributes and methods

# top_RChild class attributes and methods

# top_S class attributes and methods

# RChild class attributes and methods

# top_SChild class attributes and methods

# top_T class attributes and methods

# SChild class attributes and methods

# top_TChild class attributes and methods

# top_YChild class attributes and methods

# top_Z class attributes and methods

# YChild class attributes and methods

# top_ZChild class attributes and methods

# top_VChild class attributes and methods

# top_W class attributes and methods

# VChild class attributes and methods

# top_WChild class attributes and methods

# top_X class attributes and methods

# WChild class attributes and methods

# top_XChild class attributes and methods

# top_Y class attributes and methods

# XChild class attributes and methods

# top_IntegerLiteral class attributes and methods
top_IntegerLiteral_value: Property = Property(name="value", type=IntegerType)
top_IntegerLiteral.attributes={top_IntegerLiteral_value}

# ZChild class attributes and methods

# Relationships
child3: BinaryAssociation = BinaryAssociation(
    name="child3",
    ends={
        Property(name="top_CChild", type=top_C, multiplicity=Multiplicity(1, 1)),
        Property(name="top_C", type=top_CChild, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
child0: BinaryAssociation = BinaryAssociation(
    name="child0",
    ends={
        Property(name="top_ExprChild", type=top_Expr, multiplicity=Multiplicity(1, 1)),
        Property(name="top_Expr", type=top_ExprChild, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
child1: BinaryAssociation = BinaryAssociation(
    name="child1",
    ends={
        Property(name="top_AChild", type=top_A, multiplicity=Multiplicity(1, 1)),
        Property(name="top_A", type=top_AChild, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
child2: BinaryAssociation = BinaryAssociation(
    name="child2",
    ends={
        Property(name="top_BChild", type=top_B, multiplicity=Multiplicity(1, 1)),
        Property(name="top_B", type=top_BChild, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
child7: BinaryAssociation = BinaryAssociation(
    name="child7",
    ends={
        Property(name="top_GChild", type=top_G, multiplicity=Multiplicity(1, 1)),
        Property(name="top_G", type=top_GChild, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
child8: BinaryAssociation = BinaryAssociation(
    name="child8",
    ends={
        Property(name="top_HChild", type=top_H, multiplicity=Multiplicity(1, 1)),
        Property(name="top_H", type=top_HChild, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
child4: BinaryAssociation = BinaryAssociation(
    name="child4",
    ends={
        Property(name="top_DChild", type=top_D, multiplicity=Multiplicity(1, 1)),
        Property(name="top_D", type=top_DChild, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
child5: BinaryAssociation = BinaryAssociation(
    name="child5",
    ends={
        Property(name="top_EChild", type=top_E, multiplicity=Multiplicity(1, 1)),
        Property(name="top_E", type=top_EChild, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
child6: BinaryAssociation = BinaryAssociation(
    name="child6",
    ends={
        Property(name="top_FChild", type=top_F, multiplicity=Multiplicity(1, 1)),
        Property(name="top_F", type=top_FChild, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
child12: BinaryAssociation = BinaryAssociation(
    name="child12",
    ends={
        Property(name="top_LChild", type=top_L, multiplicity=Multiplicity(1, 1)),
        Property(name="top_L", type=top_LChild, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
child9: BinaryAssociation = BinaryAssociation(
    name="child9",
    ends={
        Property(name="top_IChild", type=top_I, multiplicity=Multiplicity(1, 1)),
        Property(name="top_I", type=top_IChild, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
child10: BinaryAssociation = BinaryAssociation(
    name="child10",
    ends={
        Property(name="top_JChild", type=top_J, multiplicity=Multiplicity(1, 1)),
        Property(name="top_J", type=top_JChild, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
child11: BinaryAssociation = BinaryAssociation(
    name="child11",
    ends={
        Property(name="top_KChild", type=top_K, multiplicity=Multiplicity(1, 1)),
        Property(name="top_K", type=top_KChild, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
child16: BinaryAssociation = BinaryAssociation(
    name="child16",
    ends={
        Property(name="top_PChild", type=top_P, multiplicity=Multiplicity(1, 1)),
        Property(name="top_P", type=top_PChild, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
child17: BinaryAssociation = BinaryAssociation(
    name="child17",
    ends={
        Property(name="top_QChild", type=top_Q, multiplicity=Multiplicity(1, 1)),
        Property(name="top_Q", type=top_QChild, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
child13: BinaryAssociation = BinaryAssociation(
    name="child13",
    ends={
        Property(name="top_MChild", type=top_M, multiplicity=Multiplicity(1, 1)),
        Property(name="top_M", type=top_MChild, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
child14: BinaryAssociation = BinaryAssociation(
    name="child14",
    ends={
        Property(name="top_NChild", type=top_N, multiplicity=Multiplicity(1, 1)),
        Property(name="top_N", type=top_NChild, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
child15: BinaryAssociation = BinaryAssociation(
    name="child15",
    ends={
        Property(name="top_OChild", type=top_O, multiplicity=Multiplicity(1, 1)),
        Property(name="top_O", type=top_OChild, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
child21: BinaryAssociation = BinaryAssociation(
    name="child21",
    ends={
        Property(name="top_UChild", type=top_U, multiplicity=Multiplicity(1, 1)),
        Property(name="top_U", type=top_UChild, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
child18: BinaryAssociation = BinaryAssociation(
    name="child18",
    ends={
        Property(name="top_RChild", type=top_R, multiplicity=Multiplicity(1, 1)),
        Property(name="top_R", type=top_RChild, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
child19: BinaryAssociation = BinaryAssociation(
    name="child19",
    ends={
        Property(name="top_SChild", type=top_S, multiplicity=Multiplicity(1, 1)),
        Property(name="top_S", type=top_SChild, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
child20: BinaryAssociation = BinaryAssociation(
    name="child20",
    ends={
        Property(name="top_TChild", type=top_T, multiplicity=Multiplicity(1, 1)),
        Property(name="top_T", type=top_TChild, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
child25: BinaryAssociation = BinaryAssociation(
    name="child25",
    ends={
        Property(name="top_YChild", type=top_Y, multiplicity=Multiplicity(1, 1)),
        Property(name="top_Y", type=top_YChild, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
child26: BinaryAssociation = BinaryAssociation(
    name="child26",
    ends={
        Property(name="top_ZChild", type=top_Z, multiplicity=Multiplicity(1, 1)),
        Property(name="top_Z", type=top_ZChild, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
child22: BinaryAssociation = BinaryAssociation(
    name="child22",
    ends={
        Property(name="top_VChild", type=top_V, multiplicity=Multiplicity(1, 1)),
        Property(name="top_V", type=top_VChild, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
child23: BinaryAssociation = BinaryAssociation(
    name="child23",
    ends={
        Property(name="top_WChild", type=top_W, multiplicity=Multiplicity(1, 1)),
        Property(name="top_W", type=top_WChild, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
child24: BinaryAssociation = BinaryAssociation(
    name="child24",
    ends={
        Property(name="top_XChild", type=top_X, multiplicity=Multiplicity(1, 1)),
        Property(name="top_X", type=top_XChild, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)

# Generalizations
gen_top_BChild_AChild = Generalization(general=AChild, specific=top_BChild)
gen_top_C_BChild = Generalization(general=BChild, specific=top_C)
gen_top_CChild_BChild = Generalization(general=BChild, specific=top_CChild)
gen_top_D_CChild = Generalization(general=CChild, specific=top_D)
gen_top_A_ExprChild = Generalization(general=ExprChild, specific=top_A)
gen_top_AChild_ExprChild = Generalization(general=ExprChild, specific=top_AChild)
gen_top_B_AChild = Generalization(general=AChild, specific=top_B)
gen_top_GChild_FChild = Generalization(general=FChild, specific=top_GChild)
gen_top_H_GChild = Generalization(general=GChild, specific=top_H)
gen_top_HChild_GChild = Generalization(general=GChild, specific=top_HChild)
gen_top_DChild_CChild = Generalization(general=CChild, specific=top_DChild)
gen_top_E_DChild = Generalization(general=DChild, specific=top_E)
gen_top_EChild_DChild = Generalization(general=DChild, specific=top_EChild)
gen_top_F_EChild = Generalization(general=EChild, specific=top_F)
gen_top_FChild_EChild = Generalization(general=EChild, specific=top_FChild)
gen_top_G_FChild = Generalization(general=FChild, specific=top_G)
gen_top_L_KChild = Generalization(general=KChild, specific=top_L)
gen_top_LChild_KChild = Generalization(general=KChild, specific=top_LChild)
gen_top_M_LChild = Generalization(general=LChild, specific=top_M)
gen_top_I_HChild = Generalization(general=HChild, specific=top_I)
gen_top_IChild_HChild = Generalization(general=HChild, specific=top_IChild)
gen_top_J_IChild = Generalization(general=IChild, specific=top_J)
gen_top_JChild_IChild = Generalization(general=IChild, specific=top_JChild)
gen_top_K_JChild = Generalization(general=JChild, specific=top_K)
gen_top_KChild_JChild = Generalization(general=JChild, specific=top_KChild)
gen_top_PChild_OChild = Generalization(general=OChild, specific=top_PChild)
gen_top_Q_PChild = Generalization(general=PChild, specific=top_Q)
gen_top_MChild_LChild = Generalization(general=LChild, specific=top_MChild)
gen_top_N_MChild = Generalization(general=MChild, specific=top_N)
gen_top_NChild_MChild = Generalization(general=MChild, specific=top_NChild)
gen_top_O_NChild = Generalization(general=NChild, specific=top_O)
gen_top_OChild_NChild = Generalization(general=NChild, specific=top_OChild)
gen_top_P_OChild = Generalization(general=OChild, specific=top_P)
gen_top_TChild_SChild = Generalization(general=SChild, specific=top_TChild)
gen_top_U_TChild = Generalization(general=TChild, specific=top_U)
gen_top_UChild_TChild = Generalization(general=TChild, specific=top_UChild)
gen_top_QChild_PChild = Generalization(general=PChild, specific=top_QChild)
gen_top_V_UChild = Generalization(general=UChild, specific=top_V)
gen_top_R_QChild = Generalization(general=QChild, specific=top_R)
gen_top_RChild_QChild = Generalization(general=QChild, specific=top_RChild)
gen_top_S_RChild = Generalization(general=RChild, specific=top_S)
gen_top_SChild_RChild = Generalization(general=RChild, specific=top_SChild)
gen_top_T_SChild = Generalization(general=SChild, specific=top_T)
gen_top_YChild_XChild = Generalization(general=XChild, specific=top_YChild)
gen_top_Z_YChild = Generalization(general=YChild, specific=top_Z)
gen_top_VChild_UChild = Generalization(general=UChild, specific=top_VChild)
gen_top_W_VChild = Generalization(general=VChild, specific=top_W)
gen_top_WChild_VChild = Generalization(general=VChild, specific=top_WChild)
gen_top_X_WChild = Generalization(general=WChild, specific=top_X)
gen_top_XChild_WChild = Generalization(general=WChild, specific=top_XChild)
gen_top_Y_XChild = Generalization(general=XChild, specific=top_Y)
gen_top_ZChild_YChild = Generalization(general=YChild, specific=top_ZChild)
gen_top_IntegerLiteral_ZChild = Generalization(general=ZChild, specific=top_IntegerLiteral)

# Domain Model
domain_model = DomainModel(
    name="top",
    types={top_C, BChild, top_CChild, top_D, CChild, top_Expr, top_ExprChild, top_A, ExprChild, top_AChild, top_B, AChild, top_BChild, top_GChild, top_H, GChild, top_HChild, top_DChild, top_E, DChild, top_EChild, top_F, EChild, top_FChild, top_G, FChild, top_L, KChild, top_LChild, top_M, LChild, top_MChild, top_I, HChild, top_IChild, top_J, IChild, top_JChild, top_K, JChild, top_KChild, top_PChild, top_Q, PChild, top_QChild, top_N, MChild, top_NChild, top_O, NChild, top_OChild, top_P, OChild, top_U, TChild, top_UChild, top_V, UChild, top_R, QChild, top_RChild, top_S, RChild, top_SChild, top_T, SChild, top_TChild, top_YChild, top_Z, YChild, top_ZChild, top_VChild, top_W, VChild, top_WChild, top_X, WChild, top_XChild, top_Y, XChild, top_IntegerLiteral, ZChild},
    associations={child3, child0, child1, child2, child7, child8, child4, child5, child6, child12, child9, child10, child11, child16, child17, child13, child14, child15, child21, child18, child19, child20, child25, child26, child22, child23, child24},
    generalizations={gen_top_BChild_AChild, gen_top_C_BChild, gen_top_CChild_BChild, gen_top_D_CChild, gen_top_A_ExprChild, gen_top_AChild_ExprChild, gen_top_B_AChild, gen_top_GChild_FChild, gen_top_H_GChild, gen_top_HChild_GChild, gen_top_DChild_CChild, gen_top_E_DChild, gen_top_EChild_DChild, gen_top_F_EChild, gen_top_FChild_EChild, gen_top_G_FChild, gen_top_L_KChild, gen_top_LChild_KChild, gen_top_M_LChild, gen_top_I_HChild, gen_top_IChild_HChild, gen_top_J_IChild, gen_top_JChild_IChild, gen_top_K_JChild, gen_top_KChild_JChild, gen_top_PChild_OChild, gen_top_Q_PChild, gen_top_MChild_LChild, gen_top_N_MChild, gen_top_NChild_MChild, gen_top_O_NChild, gen_top_OChild_NChild, gen_top_P_OChild, gen_top_TChild_SChild, gen_top_U_TChild, gen_top_UChild_TChild, gen_top_QChild_PChild, gen_top_V_UChild, gen_top_R_QChild, gen_top_RChild_QChild, gen_top_S_RChild, gen_top_SChild_RChild, gen_top_T_SChild, gen_top_YChild_XChild, gen_top_Z_YChild, gen_top_VChild_UChild, gen_top_W_VChild, gen_top_WChild_VChild, gen_top_X_WChild, gen_top_XChild_WChild, gen_top_Y_XChild, gen_top_ZChild_YChild, gen_top_IntegerLiteral_ZChild},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)