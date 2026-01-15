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
OccursMode: Enumeration = Enumeration(
    name="OccursMode",
    literals={
            EnumerationLiteral(name="DAILY"),
			EnumerationLiteral(name="WEEKLY"),
			EnumerationLiteral(name="MONTHLY")
    }
)

Day: Enumeration = Enumeration(
    name="Day",
    literals={
            EnumerationLiteral(name="SUNDAY"),
			EnumerationLiteral(name="MONDAY"),
			EnumerationLiteral(name="TUESDAY"),
			EnumerationLiteral(name="WEDNESDAY"),
			EnumerationLiteral(name="THURSDAY"),
			EnumerationLiteral(name="FRIDAY"),
			EnumerationLiteral(name="SATURDAY")
    }
)

DayOccurrence: Enumeration = Enumeration(
    name="DayOccurrence",
    literals={
            EnumerationLiteral(name="FIRST"),
			EnumerationLiteral(name="SECOND"),
			EnumerationLiteral(name="THIRD"),
			EnumerationLiteral(name="FOURTH"),
			EnumerationLiteral(name="LAST")
    }
)

# Classes
timeBasedRouting_TimeBasedRouting = Class(name="timeBasedRouting::TimeBasedRouting")
ActionStep = Class(name="ActionStep")
DynamicValue = Class(name="DynamicValue")
timeBasedRouting_TimeItem = Class(name="timeBasedRouting::TimeItem")
CaseItem = Class(name="CaseItem")
timeBasedRouting_OccursModel = Class(name="timeBasedRouting::OccursModel")
timeBasedRouting_WeeklyOccursModel = Class(name="timeBasedRouting::WeeklyOccursModel")
timeBasedRouting_MonthlyOccursModel = Class(name="timeBasedRouting::MonthlyOccursModel")
timeBasedRouting_TimeRange = Class(name="timeBasedRouting::TimeRange")
timeBasedRouting_DailyOccursModel = Class(name="timeBasedRouting::DailyOccursModel")
OccursModel = Class(name="OccursModel")

# timeBasedRouting_TimeBasedRouting class attributes and methods

# ActionStep class attributes and methods

# DynamicValue class attributes and methods

# timeBasedRouting_TimeItem class attributes and methods
timeBasedRouting_TimeItem_description: Property = Property(name="description", type=StringType)
timeBasedRouting_TimeItem.attributes={timeBasedRouting_TimeItem_description}

# CaseItem class attributes and methods

# timeBasedRouting_OccursModel class attributes and methods
timeBasedRouting_OccursModel_mode: Property = Property(name="mode", type=StringType)
timeBasedRouting_OccursModel_description: Property = Property(name="description", type=StringType)
timeBasedRouting_OccursModel_m_isMatch: Method = Method(name="isMatch", parameters={Parameter(name='date')}, type=BooleanType)
timeBasedRouting_OccursModel.attributes={timeBasedRouting_OccursModel_mode, timeBasedRouting_OccursModel_description}
timeBasedRouting_OccursModel.methods={timeBasedRouting_OccursModel_m_isMatch}

# timeBasedRouting_WeeklyOccursModel class attributes and methods
timeBasedRouting_WeeklyOccursModel_skipWeeks: Property = Property(name="skipWeeks", type=IntegerType)
timeBasedRouting_WeeklyOccursModel_days: Property = Property(name="days", type=StringType)
timeBasedRouting_WeeklyOccursModel_startDate: Property = Property(name="startDate", type=DateType)
timeBasedRouting_WeeklyOccursModel.attributes={timeBasedRouting_WeeklyOccursModel_days, timeBasedRouting_WeeklyOccursModel_startDate, timeBasedRouting_WeeklyOccursModel_skipWeeks}

# timeBasedRouting_MonthlyOccursModel class attributes and methods
timeBasedRouting_MonthlyOccursModel_byIndex: Property = Property(name="byIndex", type=BooleanType)
timeBasedRouting_MonthlyOccursModel_skipMonths: Property = Property(name="skipMonths", type=IntegerType)
timeBasedRouting_MonthlyOccursModel_dayIndex: Property = Property(name="dayIndex", type=IntegerType)
timeBasedRouting_MonthlyOccursModel_dayOccurence: Property = Property(name="dayOccurence", type=StringType)
timeBasedRouting_MonthlyOccursModel_day: Property = Property(name="day", type=StringType)
timeBasedRouting_MonthlyOccursModel_startDate: Property = Property(name="startDate", type=DateType)
timeBasedRouting_MonthlyOccursModel.attributes={timeBasedRouting_MonthlyOccursModel_dayOccurence, timeBasedRouting_MonthlyOccursModel_dayIndex, timeBasedRouting_MonthlyOccursModel_skipMonths, timeBasedRouting_MonthlyOccursModel_byIndex, timeBasedRouting_MonthlyOccursModel_day, timeBasedRouting_MonthlyOccursModel_startDate}

# timeBasedRouting_TimeRange class attributes and methods
timeBasedRouting_TimeRange_endRange: Property = Property(name="endRange", type=DateType)
timeBasedRouting_TimeRange_name: Property = Property(name="name", type=StringType)
timeBasedRouting_TimeRange_startRange: Property = Property(name="startRange", type=DateType)
timeBasedRouting_TimeRange_m_isMatch: Method = Method(name="isMatch", parameters={Parameter(name='date')}, type=BooleanType)
timeBasedRouting_TimeRange.attributes={timeBasedRouting_TimeRange_startRange, timeBasedRouting_TimeRange_endRange, timeBasedRouting_TimeRange_name}
timeBasedRouting_TimeRange.methods={timeBasedRouting_TimeRange_m_isMatch}

# timeBasedRouting_DailyOccursModel class attributes and methods
timeBasedRouting_DailyOccursModel_skipDays: Property = Property(name="skipDays", type=IntegerType)
timeBasedRouting_DailyOccursModel_startDate: Property = Property(name="startDate", type=DateType)
timeBasedRouting_DailyOccursModel.attributes={timeBasedRouting_DailyOccursModel_skipDays, timeBasedRouting_DailyOccursModel_startDate}

# OccursModel class attributes and methods

# Relationships
value0: BinaryAssociation = BinaryAssociation(
    name="value0",
    ends={
        Property(name="DynamicValue", type=timeBasedRouting_TimeBasedRouting, multiplicity=Multiplicity(1, 1)),
        Property(name="timeBasedRouting_TimeBasedRouting", type=DynamicValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
times1: BinaryAssociation = BinaryAssociation(
    name="times1",
    ends={
        Property(name="timeBasedRouting_TimeItem", type=timeBasedRouting_TimeBasedRouting, multiplicity=Multiplicity(1, 1)),
        Property(name="timeBasedRouting_TimeBasedRouting2", type=timeBasedRouting_TimeItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
occursModel3: BinaryAssociation = BinaryAssociation(
    name="occursModel3",
    ends={
        Property(name="timeBasedRouting_OccursModel", type=timeBasedRouting_TimeRange, multiplicity=Multiplicity(1, 1)),
        Property(name="timeBasedRouting_TimeRange", type=timeBasedRouting_OccursModel, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_timeBasedRouting_TimeBasedRouting_ActionStep = Generalization(general=ActionStep, specific=timeBasedRouting_TimeBasedRouting)
gen_timeBasedRouting_TimeItem_CaseItem = Generalization(general=CaseItem, specific=timeBasedRouting_TimeItem)
gen_timeBasedRouting_WeeklyOccursModel_OccursModel = Generalization(general=OccursModel, specific=timeBasedRouting_WeeklyOccursModel)
gen_timeBasedRouting_MonthlyOccursModel_OccursModel = Generalization(general=OccursModel, specific=timeBasedRouting_MonthlyOccursModel)
gen_timeBasedRouting_DailyOccursModel_OccursModel = Generalization(general=OccursModel, specific=timeBasedRouting_DailyOccursModel)

# Domain Model
domain_model = DomainModel(
    name="timeBasedRouting",
    types={timeBasedRouting_TimeBasedRouting, ActionStep, DynamicValue, timeBasedRouting_TimeItem, CaseItem, timeBasedRouting_OccursModel, timeBasedRouting_WeeklyOccursModel, timeBasedRouting_MonthlyOccursModel, timeBasedRouting_TimeRange, timeBasedRouting_DailyOccursModel, OccursModel, OccursMode, Day, DayOccurrence},
    associations={value0, times1, occursModel3},
    generalizations={gen_timeBasedRouting_TimeBasedRouting_ActionStep, gen_timeBasedRouting_TimeItem_CaseItem, gen_timeBasedRouting_WeeklyOccursModel_OccursModel, gen_timeBasedRouting_MonthlyOccursModel_OccursModel, gen_timeBasedRouting_DailyOccursModel_OccursModel},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)