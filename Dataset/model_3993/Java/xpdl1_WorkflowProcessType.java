





import java.util.List;
import java.util.ArrayList;

public class xpdl1_WorkflowProcessType  {

    private String name;
    private String accessLevel;
    private String id;





    private xpdl1_ApplicationsType xpdl1_applicationstype;




    private xpdl1_ProcessHeaderType xpdl1_processheadertype;




    private xpdl1_ActivitiesType xpdl1_activitiestype;




    private xpdl1_RedefinableHeaderType xpdl1_redefinableheadertype;




    private xpdl1_FormalParametersType xpdl1_formalparameterstype;




    private xpdl1_DocumentRoot xpdl1_documentroot;




    private xpdl1_ParticipantsType xpdl1_participantstype;




    private xpdl1_ExtendedAttributesType xpdl1_extendedattributestype;




    private xpdl1_DataFieldsType xpdl1_datafieldstype;




    private xpdl1_ActivitySetsType xpdl1_activitysetstype;




    private xpdl1_TransitionsType xpdl1_transitionstype;


    public xpdl1_WorkflowProcessType(
        String name,        String accessLevel,        String id    ) {
        this.name = name;
        this.accessLevel = accessLevel;
        this.id = id;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAccesslevel() {
        return accessLevel;
    }

    public void setAccesslevel(String accessLevel) {
        this.accessLevel = accessLevel;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public xpdl1_ApplicationsType getXpdl1_applicationstype() {
        return xpdl1_applicationstype;
    }

    public void setXpdl1_applicationstype(xpdl1_ApplicationsType xpdl1_applicationstype) {
        this.xpdl1_applicationstype = xpdl1_applicationstype;
    }
    public xpdl1_ProcessHeaderType getXpdl1_processheadertype() {
        return xpdl1_processheadertype;
    }

    public void setXpdl1_processheadertype(xpdl1_ProcessHeaderType xpdl1_processheadertype) {
        this.xpdl1_processheadertype = xpdl1_processheadertype;
    }
    public xpdl1_ActivitiesType getXpdl1_activitiestype() {
        return xpdl1_activitiestype;
    }

    public void setXpdl1_activitiestype(xpdl1_ActivitiesType xpdl1_activitiestype) {
        this.xpdl1_activitiestype = xpdl1_activitiestype;
    }
    public xpdl1_RedefinableHeaderType getXpdl1_redefinableheadertype() {
        return xpdl1_redefinableheadertype;
    }

    public void setXpdl1_redefinableheadertype(xpdl1_RedefinableHeaderType xpdl1_redefinableheadertype) {
        this.xpdl1_redefinableheadertype = xpdl1_redefinableheadertype;
    }
    public xpdl1_FormalParametersType getXpdl1_formalparameterstype() {
        return xpdl1_formalparameterstype;
    }

    public void setXpdl1_formalparameterstype(xpdl1_FormalParametersType xpdl1_formalparameterstype) {
        this.xpdl1_formalparameterstype = xpdl1_formalparameterstype;
    }
    public xpdl1_DocumentRoot getXpdl1_documentroot() {
        return xpdl1_documentroot;
    }

    public void setXpdl1_documentroot(xpdl1_DocumentRoot xpdl1_documentroot) {
        this.xpdl1_documentroot = xpdl1_documentroot;
    }
    public xpdl1_ParticipantsType getXpdl1_participantstype() {
        return xpdl1_participantstype;
    }

    public void setXpdl1_participantstype(xpdl1_ParticipantsType xpdl1_participantstype) {
        this.xpdl1_participantstype = xpdl1_participantstype;
    }
    public xpdl1_ExtendedAttributesType getXpdl1_extendedattributestype() {
        return xpdl1_extendedattributestype;
    }

    public void setXpdl1_extendedattributestype(xpdl1_ExtendedAttributesType xpdl1_extendedattributestype) {
        this.xpdl1_extendedattributestype = xpdl1_extendedattributestype;
    }
    public xpdl1_DataFieldsType getXpdl1_datafieldstype() {
        return xpdl1_datafieldstype;
    }

    public void setXpdl1_datafieldstype(xpdl1_DataFieldsType xpdl1_datafieldstype) {
        this.xpdl1_datafieldstype = xpdl1_datafieldstype;
    }
    public xpdl1_ActivitySetsType getXpdl1_activitysetstype() {
        return xpdl1_activitysetstype;
    }

    public void setXpdl1_activitysetstype(xpdl1_ActivitySetsType xpdl1_activitysetstype) {
        this.xpdl1_activitysetstype = xpdl1_activitysetstype;
    }
    public xpdl1_TransitionsType getXpdl1_transitionstype() {
        return xpdl1_transitionstype;
    }

    public void setXpdl1_transitionstype(xpdl1_TransitionsType xpdl1_transitionstype) {
        this.xpdl1_transitionstype = xpdl1_transitionstype;
    }

}