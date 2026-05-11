





import java.util.List;
import java.util.ArrayList;

public class xpdl1_DocumentRoot  {

    private String mixed;
    private String costUnit;
    private String duration;
    private String waitingTime;
    private String workingTime;
    private String length;
    private String actualParameter;
    private String validTo;
    private String description;
    private String countrykey;
    private String version;
    private String priority;
    private String vendor;
    private String documentation;
    private String limit;
    private String cost;
    private String codepage;
    private String created;
    private String performer;
    private String priorityUnit;
    private String validFrom;
    private String author;
    private String xPDLVersion;
    private String initialValue;
    private String icon;
    private String responsible;





    private List<xpdl1_ExtendedAttributesType> xpdl1_extendedattributestypes;




    private List<xpdl1_TransitionRestrictionsType> xpdl1_transitionrestrictionstypes;




    private List<xpdl1_BlockActivityType> xpdl1_blockactivitytypes;




    private List<xpdl1_ActivitiesType> xpdl1_activitiestypes;




    private List<xpdl1_ApplicationsType> xpdl1_applicationstypes;




    private List<xpdl1_UnionTypeType> xpdl1_uniontypetypes;




    private List<xpdl1_ActivitySetType> xpdl1_activitysettypes;




    private List<xpdl1_StartModeType> xpdl1_startmodetypes;




    private List<xpdl1_DataFieldsType> xpdl1_datafieldstypes;




    private List<xpdl1_EnumerationTypeType> xpdl1_enumerationtypetypes;




    private List<xpdl1_TransitionsType> xpdl1_transitionstypes;




    private List<xpdl1_ArrayTypeType> xpdl1_arraytypetypes;




    private List<xpdl1_RouteType> xpdl1_routetypes;




    private List<xpdl1_ImplementationType> xpdl1_implementationtypes;




    private List<xpdl1_FinishModeType> xpdl1_finishmodetypes;




    private List<xpdl1_ConditionType> xpdl1_conditiontypes;




    private List<xpdl1_ApplicationType> xpdl1_applicationtypes;




    private List<xpdl1_RecordTypeType> xpdl1_recordtypetypes;




    private List<xpdl1_ActivitySetsType> xpdl1_activitysetstypes;




    private List<xpdl1_ExternalReferenceType> xpdl1_externalreferencetypes;




    private List<xpdl1_DeadlineType> xpdl1_deadlinetypes;




    private List<xpdl1_ListTypeType> xpdl1_listtypetypes;




    private List<xpdl1_XpressionType> xpdl1_xpressiontypes;




    private List<xpdl1_ConformanceClassType> xpdl1_conformanceclasstypes;




    private List<xpdl1_FormalParametersType> xpdl1_formalparameterstypes;




    private List<xpdl1_ActivityType> xpdl1_activitytypes;




    private List<xpdl1_SchemaTypeType> xpdl1_schematypetypes;




    private List<xpdl1_ActualParametersType> xpdl1_actualparameterstypes;




    private List<xpdl1_DeclaredTypeType> xpdl1_declaredtypetypes;




    private List<xpdl1_AutomaticType> xpdl1_automatictypes;




    private List<xpdl1_DataFieldType> xpdl1_datafieldtypes;




    private List<xpdl1_SimulationInformationType> xpdl1_simulationinformationtypes;




    private List<xpdl1_DataTypeType> xpdl1_datatypetypes;




    private List<xpdl1_BasicTypeType> xpdl1_basictypetypes;


    public xpdl1_DocumentRoot(
        String mixed,        String costUnit,        String duration,        String waitingTime,        String workingTime,        String length,        String actualParameter,        String validTo,        String description,        String countrykey,        String version,        String priority,        String vendor,        String documentation,        String limit,        String cost,        String codepage,        String created,        String performer,        String priorityUnit,        String validFrom,        String author,        String xPDLVersion,        String initialValue,        String icon,        String responsible    ) {
        this.mixed = mixed;
        this.costUnit = costUnit;
        this.duration = duration;
        this.waitingTime = waitingTime;
        this.workingTime = workingTime;
        this.length = length;
        this.actualParameter = actualParameter;
        this.validTo = validTo;
        this.description = description;
        this.countrykey = countrykey;
        this.version = version;
        this.priority = priority;
        this.vendor = vendor;
        this.documentation = documentation;
        this.limit = limit;
        this.cost = cost;
        this.codepage = codepage;
        this.created = created;
        this.performer = performer;
        this.priorityUnit = priorityUnit;
        this.validFrom = validFrom;
        this.author = author;
        this.xPDLVersion = xPDLVersion;
        this.initialValue = initialValue;
        this.icon = icon;
        this.responsible = responsible;
        this.xpdl1_extendedattributestypes = new ArrayList<>();
        this.xpdl1_transitionrestrictionstypes = new ArrayList<>();
        this.xpdl1_blockactivitytypes = new ArrayList<>();
        this.xpdl1_activitiestypes = new ArrayList<>();
        this.xpdl1_applicationstypes = new ArrayList<>();
        this.xpdl1_uniontypetypes = new ArrayList<>();
        this.xpdl1_activitysettypes = new ArrayList<>();
        this.xpdl1_startmodetypes = new ArrayList<>();
        this.xpdl1_datafieldstypes = new ArrayList<>();
        this.xpdl1_enumerationtypetypes = new ArrayList<>();
        this.xpdl1_transitionstypes = new ArrayList<>();
        this.xpdl1_arraytypetypes = new ArrayList<>();
        this.xpdl1_routetypes = new ArrayList<>();
        this.xpdl1_implementationtypes = new ArrayList<>();
        this.xpdl1_finishmodetypes = new ArrayList<>();
        this.xpdl1_conditiontypes = new ArrayList<>();
        this.xpdl1_applicationtypes = new ArrayList<>();
        this.xpdl1_recordtypetypes = new ArrayList<>();
        this.xpdl1_activitysetstypes = new ArrayList<>();
        this.xpdl1_externalreferencetypes = new ArrayList<>();
        this.xpdl1_deadlinetypes = new ArrayList<>();
        this.xpdl1_listtypetypes = new ArrayList<>();
        this.xpdl1_xpressiontypes = new ArrayList<>();
        this.xpdl1_conformanceclasstypes = new ArrayList<>();
        this.xpdl1_formalparameterstypes = new ArrayList<>();
        this.xpdl1_activitytypes = new ArrayList<>();
        this.xpdl1_schematypetypes = new ArrayList<>();
        this.xpdl1_actualparameterstypes = new ArrayList<>();
        this.xpdl1_declaredtypetypes = new ArrayList<>();
        this.xpdl1_automatictypes = new ArrayList<>();
        this.xpdl1_datafieldtypes = new ArrayList<>();
        this.xpdl1_simulationinformationtypes = new ArrayList<>();
        this.xpdl1_datatypetypes = new ArrayList<>();
        this.xpdl1_basictypetypes = new ArrayList<>();
    }

    public xpdl1_DocumentRoot(
        String mixed,        String costUnit,        String duration,        String waitingTime,        String workingTime,        String length,        String actualParameter,        String validTo,        String description,        String countrykey,        String version,        String priority,        String vendor,        String documentation,        String limit,        String cost,        String codepage,        String created,        String performer,        String priorityUnit,        String validFrom,        String author,        String xPDLVersion,        String initialValue,        String icon,        String responsible        ArrayList<xpdl1_ExtendedAttributesType> xpdl1_extendedattributestypes,        ArrayList<xpdl1_TransitionRestrictionsType> xpdl1_transitionrestrictionstypes,        ArrayList<xpdl1_BlockActivityType> xpdl1_blockactivitytypes,        ArrayList<xpdl1_ActivitiesType> xpdl1_activitiestypes,        ArrayList<xpdl1_ApplicationsType> xpdl1_applicationstypes,        ArrayList<xpdl1_UnionTypeType> xpdl1_uniontypetypes,        ArrayList<xpdl1_ActivitySetType> xpdl1_activitysettypes,        ArrayList<xpdl1_StartModeType> xpdl1_startmodetypes,        ArrayList<xpdl1_DataFieldsType> xpdl1_datafieldstypes,        ArrayList<xpdl1_EnumerationTypeType> xpdl1_enumerationtypetypes,        ArrayList<xpdl1_TransitionsType> xpdl1_transitionstypes,        ArrayList<xpdl1_ArrayTypeType> xpdl1_arraytypetypes,        ArrayList<xpdl1_RouteType> xpdl1_routetypes,        ArrayList<xpdl1_ImplementationType> xpdl1_implementationtypes,        ArrayList<xpdl1_FinishModeType> xpdl1_finishmodetypes,        ArrayList<xpdl1_ConditionType> xpdl1_conditiontypes,        ArrayList<xpdl1_ApplicationType> xpdl1_applicationtypes,        ArrayList<xpdl1_RecordTypeType> xpdl1_recordtypetypes,        ArrayList<xpdl1_ActivitySetsType> xpdl1_activitysetstypes,        ArrayList<xpdl1_ExternalReferenceType> xpdl1_externalreferencetypes,        ArrayList<xpdl1_DeadlineType> xpdl1_deadlinetypes,        ArrayList<xpdl1_ListTypeType> xpdl1_listtypetypes,        ArrayList<xpdl1_XpressionType> xpdl1_xpressiontypes,        ArrayList<xpdl1_ConformanceClassType> xpdl1_conformanceclasstypes,        ArrayList<xpdl1_FormalParametersType> xpdl1_formalparameterstypes,        ArrayList<xpdl1_ActivityType> xpdl1_activitytypes,        ArrayList<xpdl1_SchemaTypeType> xpdl1_schematypetypes,        ArrayList<xpdl1_ActualParametersType> xpdl1_actualparameterstypes,        ArrayList<xpdl1_DeclaredTypeType> xpdl1_declaredtypetypes,        ArrayList<xpdl1_AutomaticType> xpdl1_automatictypes,        ArrayList<xpdl1_DataFieldType> xpdl1_datafieldtypes,        ArrayList<xpdl1_SimulationInformationType> xpdl1_simulationinformationtypes,        ArrayList<xpdl1_DataTypeType> xpdl1_datatypetypes,        ArrayList<xpdl1_BasicTypeType> xpdl1_basictypetypes    ) {
        this.mixed = mixed;
        this.costUnit = costUnit;
        this.duration = duration;
        this.waitingTime = waitingTime;
        this.workingTime = workingTime;
        this.length = length;
        this.actualParameter = actualParameter;
        this.validTo = validTo;
        this.description = description;
        this.countrykey = countrykey;
        this.version = version;
        this.priority = priority;
        this.vendor = vendor;
        this.documentation = documentation;
        this.limit = limit;
        this.cost = cost;
        this.codepage = codepage;
        this.created = created;
        this.performer = performer;
        this.priorityUnit = priorityUnit;
        this.validFrom = validFrom;
        this.author = author;
        this.xPDLVersion = xPDLVersion;
        this.initialValue = initialValue;
        this.icon = icon;
        this.responsible = responsible;
        this.xpdl1_extendedattributestypes = xpdl1_extendedattributestypes;
        this.xpdl1_transitionrestrictionstypes = xpdl1_transitionrestrictionstypes;
        this.xpdl1_blockactivitytypes = xpdl1_blockactivitytypes;
        this.xpdl1_activitiestypes = xpdl1_activitiestypes;
        this.xpdl1_applicationstypes = xpdl1_applicationstypes;
        this.xpdl1_uniontypetypes = xpdl1_uniontypetypes;
        this.xpdl1_activitysettypes = xpdl1_activitysettypes;
        this.xpdl1_startmodetypes = xpdl1_startmodetypes;
        this.xpdl1_datafieldstypes = xpdl1_datafieldstypes;
        this.xpdl1_enumerationtypetypes = xpdl1_enumerationtypetypes;
        this.xpdl1_transitionstypes = xpdl1_transitionstypes;
        this.xpdl1_arraytypetypes = xpdl1_arraytypetypes;
        this.xpdl1_routetypes = xpdl1_routetypes;
        this.xpdl1_implementationtypes = xpdl1_implementationtypes;
        this.xpdl1_finishmodetypes = xpdl1_finishmodetypes;
        this.xpdl1_conditiontypes = xpdl1_conditiontypes;
        this.xpdl1_applicationtypes = xpdl1_applicationtypes;
        this.xpdl1_recordtypetypes = xpdl1_recordtypetypes;
        this.xpdl1_activitysetstypes = xpdl1_activitysetstypes;
        this.xpdl1_externalreferencetypes = xpdl1_externalreferencetypes;
        this.xpdl1_deadlinetypes = xpdl1_deadlinetypes;
        this.xpdl1_listtypetypes = xpdl1_listtypetypes;
        this.xpdl1_xpressiontypes = xpdl1_xpressiontypes;
        this.xpdl1_conformanceclasstypes = xpdl1_conformanceclasstypes;
        this.xpdl1_formalparameterstypes = xpdl1_formalparameterstypes;
        this.xpdl1_activitytypes = xpdl1_activitytypes;
        this.xpdl1_schematypetypes = xpdl1_schematypetypes;
        this.xpdl1_actualparameterstypes = xpdl1_actualparameterstypes;
        this.xpdl1_declaredtypetypes = xpdl1_declaredtypetypes;
        this.xpdl1_automatictypes = xpdl1_automatictypes;
        this.xpdl1_datafieldtypes = xpdl1_datafieldtypes;
        this.xpdl1_simulationinformationtypes = xpdl1_simulationinformationtypes;
        this.xpdl1_datatypetypes = xpdl1_datatypetypes;
        this.xpdl1_basictypetypes = xpdl1_basictypetypes;
    }

    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }
    public String getCostunit() {
        return costUnit;
    }

    public void setCostunit(String costUnit) {
        this.costUnit = costUnit;
    }
    public String getDuration() {
        return duration;
    }

    public void setDuration(String duration) {
        this.duration = duration;
    }
    public String getWaitingtime() {
        return waitingTime;
    }

    public void setWaitingtime(String waitingTime) {
        this.waitingTime = waitingTime;
    }
    public String getWorkingtime() {
        return workingTime;
    }

    public void setWorkingtime(String workingTime) {
        this.workingTime = workingTime;
    }
    public String getLength() {
        return length;
    }

    public void setLength(String length) {
        this.length = length;
    }
    public String getActualparameter() {
        return actualParameter;
    }

    public void setActualparameter(String actualParameter) {
        this.actualParameter = actualParameter;
    }
    public String getValidto() {
        return validTo;
    }

    public void setValidto(String validTo) {
        this.validTo = validTo;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getCountrykey() {
        return countrykey;
    }

    public void setCountrykey(String countrykey) {
        this.countrykey = countrykey;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getPriority() {
        return priority;
    }

    public void setPriority(String priority) {
        this.priority = priority;
    }
    public String getVendor() {
        return vendor;
    }

    public void setVendor(String vendor) {
        this.vendor = vendor;
    }
    public String getDocumentation() {
        return documentation;
    }

    public void setDocumentation(String documentation) {
        this.documentation = documentation;
    }
    public String getLimit() {
        return limit;
    }

    public void setLimit(String limit) {
        this.limit = limit;
    }
    public String getCost() {
        return cost;
    }

    public void setCost(String cost) {
        this.cost = cost;
    }
    public String getCodepage() {
        return codepage;
    }

    public void setCodepage(String codepage) {
        this.codepage = codepage;
    }
    public String getCreated() {
        return created;
    }

    public void setCreated(String created) {
        this.created = created;
    }
    public String getPerformer() {
        return performer;
    }

    public void setPerformer(String performer) {
        this.performer = performer;
    }
    public String getPriorityunit() {
        return priorityUnit;
    }

    public void setPriorityunit(String priorityUnit) {
        this.priorityUnit = priorityUnit;
    }
    public String getValidfrom() {
        return validFrom;
    }

    public void setValidfrom(String validFrom) {
        this.validFrom = validFrom;
    }
    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }
    public String getXpdlversion() {
        return xPDLVersion;
    }

    public void setXpdlversion(String xPDLVersion) {
        this.xPDLVersion = xPDLVersion;
    }
    public String getInitialvalue() {
        return initialValue;
    }

    public void setInitialvalue(String initialValue) {
        this.initialValue = initialValue;
    }
    public String getIcon() {
        return icon;
    }

    public void setIcon(String icon) {
        this.icon = icon;
    }
    public String getResponsible() {
        return responsible;
    }

    public void setResponsible(String responsible) {
        this.responsible = responsible;
    }

    public List<xpdl1_ExtendedAttributesType> getXpdl1_extendedattributestypes() {
        return xpdl1_extendedattributestypes;
    }

    public void addXpdl1_extendedattributestype(Xpdl1_extendedattributestype xpdl1_extendedattributestype) {
        this.xpdl1_extendedattributestypes.add(xpdl1_extendedattributestype);
    }
    public List<xpdl1_TransitionRestrictionsType> getXpdl1_transitionrestrictionstypes() {
        return xpdl1_transitionrestrictionstypes;
    }

    public void addXpdl1_transitionrestrictionstype(Xpdl1_transitionrestrictionstype xpdl1_transitionrestrictionstype) {
        this.xpdl1_transitionrestrictionstypes.add(xpdl1_transitionrestrictionstype);
    }
    public List<xpdl1_BlockActivityType> getXpdl1_blockactivitytypes() {
        return xpdl1_blockactivitytypes;
    }

    public void addXpdl1_blockactivitytype(Xpdl1_blockactivitytype xpdl1_blockactivitytype) {
        this.xpdl1_blockactivitytypes.add(xpdl1_blockactivitytype);
    }
    public List<xpdl1_ActivitiesType> getXpdl1_activitiestypes() {
        return xpdl1_activitiestypes;
    }

    public void addXpdl1_activitiestype(Xpdl1_activitiestype xpdl1_activitiestype) {
        this.xpdl1_activitiestypes.add(xpdl1_activitiestype);
    }
    public List<xpdl1_ApplicationsType> getXpdl1_applicationstypes() {
        return xpdl1_applicationstypes;
    }

    public void addXpdl1_applicationstype(Xpdl1_applicationstype xpdl1_applicationstype) {
        this.xpdl1_applicationstypes.add(xpdl1_applicationstype);
    }
    public List<xpdl1_UnionTypeType> getXpdl1_uniontypetypes() {
        return xpdl1_uniontypetypes;
    }

    public void addXpdl1_uniontypetype(Xpdl1_uniontypetype xpdl1_uniontypetype) {
        this.xpdl1_uniontypetypes.add(xpdl1_uniontypetype);
    }
    public List<xpdl1_ActivitySetType> getXpdl1_activitysettypes() {
        return xpdl1_activitysettypes;
    }

    public void addXpdl1_activitysettype(Xpdl1_activitysettype xpdl1_activitysettype) {
        this.xpdl1_activitysettypes.add(xpdl1_activitysettype);
    }
    public List<xpdl1_StartModeType> getXpdl1_startmodetypes() {
        return xpdl1_startmodetypes;
    }

    public void addXpdl1_startmodetype(Xpdl1_startmodetype xpdl1_startmodetype) {
        this.xpdl1_startmodetypes.add(xpdl1_startmodetype);
    }
    public List<xpdl1_DataFieldsType> getXpdl1_datafieldstypes() {
        return xpdl1_datafieldstypes;
    }

    public void addXpdl1_datafieldstype(Xpdl1_datafieldstype xpdl1_datafieldstype) {
        this.xpdl1_datafieldstypes.add(xpdl1_datafieldstype);
    }
    public List<xpdl1_EnumerationTypeType> getXpdl1_enumerationtypetypes() {
        return xpdl1_enumerationtypetypes;
    }

    public void addXpdl1_enumerationtypetype(Xpdl1_enumerationtypetype xpdl1_enumerationtypetype) {
        this.xpdl1_enumerationtypetypes.add(xpdl1_enumerationtypetype);
    }
    public List<xpdl1_TransitionsType> getXpdl1_transitionstypes() {
        return xpdl1_transitionstypes;
    }

    public void addXpdl1_transitionstype(Xpdl1_transitionstype xpdl1_transitionstype) {
        this.xpdl1_transitionstypes.add(xpdl1_transitionstype);
    }
    public List<xpdl1_ArrayTypeType> getXpdl1_arraytypetypes() {
        return xpdl1_arraytypetypes;
    }

    public void addXpdl1_arraytypetype(Xpdl1_arraytypetype xpdl1_arraytypetype) {
        this.xpdl1_arraytypetypes.add(xpdl1_arraytypetype);
    }
    public List<xpdl1_RouteType> getXpdl1_routetypes() {
        return xpdl1_routetypes;
    }

    public void addXpdl1_routetype(Xpdl1_routetype xpdl1_routetype) {
        this.xpdl1_routetypes.add(xpdl1_routetype);
    }
    public List<xpdl1_ImplementationType> getXpdl1_implementationtypes() {
        return xpdl1_implementationtypes;
    }

    public void addXpdl1_implementationtype(Xpdl1_implementationtype xpdl1_implementationtype) {
        this.xpdl1_implementationtypes.add(xpdl1_implementationtype);
    }
    public List<xpdl1_FinishModeType> getXpdl1_finishmodetypes() {
        return xpdl1_finishmodetypes;
    }

    public void addXpdl1_finishmodetype(Xpdl1_finishmodetype xpdl1_finishmodetype) {
        this.xpdl1_finishmodetypes.add(xpdl1_finishmodetype);
    }
    public List<xpdl1_ConditionType> getXpdl1_conditiontypes() {
        return xpdl1_conditiontypes;
    }

    public void addXpdl1_conditiontype(Xpdl1_conditiontype xpdl1_conditiontype) {
        this.xpdl1_conditiontypes.add(xpdl1_conditiontype);
    }
    public List<xpdl1_ApplicationType> getXpdl1_applicationtypes() {
        return xpdl1_applicationtypes;
    }

    public void addXpdl1_applicationtype(Xpdl1_applicationtype xpdl1_applicationtype) {
        this.xpdl1_applicationtypes.add(xpdl1_applicationtype);
    }
    public List<xpdl1_RecordTypeType> getXpdl1_recordtypetypes() {
        return xpdl1_recordtypetypes;
    }

    public void addXpdl1_recordtypetype(Xpdl1_recordtypetype xpdl1_recordtypetype) {
        this.xpdl1_recordtypetypes.add(xpdl1_recordtypetype);
    }
    public List<xpdl1_ActivitySetsType> getXpdl1_activitysetstypes() {
        return xpdl1_activitysetstypes;
    }

    public void addXpdl1_activitysetstype(Xpdl1_activitysetstype xpdl1_activitysetstype) {
        this.xpdl1_activitysetstypes.add(xpdl1_activitysetstype);
    }
    public List<xpdl1_ExternalReferenceType> getXpdl1_externalreferencetypes() {
        return xpdl1_externalreferencetypes;
    }

    public void addXpdl1_externalreferencetype(Xpdl1_externalreferencetype xpdl1_externalreferencetype) {
        this.xpdl1_externalreferencetypes.add(xpdl1_externalreferencetype);
    }
    public List<xpdl1_DeadlineType> getXpdl1_deadlinetypes() {
        return xpdl1_deadlinetypes;
    }

    public void addXpdl1_deadlinetype(Xpdl1_deadlinetype xpdl1_deadlinetype) {
        this.xpdl1_deadlinetypes.add(xpdl1_deadlinetype);
    }
    public List<xpdl1_ListTypeType> getXpdl1_listtypetypes() {
        return xpdl1_listtypetypes;
    }

    public void addXpdl1_listtypetype(Xpdl1_listtypetype xpdl1_listtypetype) {
        this.xpdl1_listtypetypes.add(xpdl1_listtypetype);
    }
    public List<xpdl1_XpressionType> getXpdl1_xpressiontypes() {
        return xpdl1_xpressiontypes;
    }

    public void addXpdl1_xpressiontype(Xpdl1_xpressiontype xpdl1_xpressiontype) {
        this.xpdl1_xpressiontypes.add(xpdl1_xpressiontype);
    }
    public List<xpdl1_ConformanceClassType> getXpdl1_conformanceclasstypes() {
        return xpdl1_conformanceclasstypes;
    }

    public void addXpdl1_conformanceclasstype(Xpdl1_conformanceclasstype xpdl1_conformanceclasstype) {
        this.xpdl1_conformanceclasstypes.add(xpdl1_conformanceclasstype);
    }
    public List<xpdl1_FormalParametersType> getXpdl1_formalparameterstypes() {
        return xpdl1_formalparameterstypes;
    }

    public void addXpdl1_formalparameterstype(Xpdl1_formalparameterstype xpdl1_formalparameterstype) {
        this.xpdl1_formalparameterstypes.add(xpdl1_formalparameterstype);
    }
    public List<xpdl1_ActivityType> getXpdl1_activitytypes() {
        return xpdl1_activitytypes;
    }

    public void addXpdl1_activitytype(Xpdl1_activitytype xpdl1_activitytype) {
        this.xpdl1_activitytypes.add(xpdl1_activitytype);
    }
    public List<xpdl1_SchemaTypeType> getXpdl1_schematypetypes() {
        return xpdl1_schematypetypes;
    }

    public void addXpdl1_schematypetype(Xpdl1_schematypetype xpdl1_schematypetype) {
        this.xpdl1_schematypetypes.add(xpdl1_schematypetype);
    }
    public List<xpdl1_ActualParametersType> getXpdl1_actualparameterstypes() {
        return xpdl1_actualparameterstypes;
    }

    public void addXpdl1_actualparameterstype(Xpdl1_actualparameterstype xpdl1_actualparameterstype) {
        this.xpdl1_actualparameterstypes.add(xpdl1_actualparameterstype);
    }
    public List<xpdl1_DeclaredTypeType> getXpdl1_declaredtypetypes() {
        return xpdl1_declaredtypetypes;
    }

    public void addXpdl1_declaredtypetype(Xpdl1_declaredtypetype xpdl1_declaredtypetype) {
        this.xpdl1_declaredtypetypes.add(xpdl1_declaredtypetype);
    }
    public List<xpdl1_AutomaticType> getXpdl1_automatictypes() {
        return xpdl1_automatictypes;
    }

    public void addXpdl1_automatictype(Xpdl1_automatictype xpdl1_automatictype) {
        this.xpdl1_automatictypes.add(xpdl1_automatictype);
    }
    public List<xpdl1_DataFieldType> getXpdl1_datafieldtypes() {
        return xpdl1_datafieldtypes;
    }

    public void addXpdl1_datafieldtype(Xpdl1_datafieldtype xpdl1_datafieldtype) {
        this.xpdl1_datafieldtypes.add(xpdl1_datafieldtype);
    }
    public List<xpdl1_SimulationInformationType> getXpdl1_simulationinformationtypes() {
        return xpdl1_simulationinformationtypes;
    }

    public void addXpdl1_simulationinformationtype(Xpdl1_simulationinformationtype xpdl1_simulationinformationtype) {
        this.xpdl1_simulationinformationtypes.add(xpdl1_simulationinformationtype);
    }
    public List<xpdl1_DataTypeType> getXpdl1_datatypetypes() {
        return xpdl1_datatypetypes;
    }

    public void addXpdl1_datatypetype(Xpdl1_datatypetype xpdl1_datatypetype) {
        this.xpdl1_datatypetypes.add(xpdl1_datatypetype);
    }
    public List<xpdl1_BasicTypeType> getXpdl1_basictypetypes() {
        return xpdl1_basictypetypes;
    }

    public void addXpdl1_basictypetype(Xpdl1_basictypetype xpdl1_basictypetype) {
        this.xpdl1_basictypetypes.add(xpdl1_basictypetype);
    }

}