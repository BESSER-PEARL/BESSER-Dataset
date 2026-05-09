





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_Activity extends Behavior {

    private String language;
    private boolean isSingleExecution;
    private String body;
    private boolean isReadOnly;





    private UML2WithID_ActivityNode uml2withid_activitynode;




    private UML2WithID_State uml2withid_state;




    private UML2WithID_State uml2withid_state;




    private List<UML2WithID_ActivityNode> uml2withid_activitynodes;




    private UML2WithID_Transition uml2withid_transition;




    private List<UML2WithID_ActivityGroup> uml2withid_activitygroups;




    private UML2WithID_ActivityEdge uml2withid_activityedge;




    private List<UML2WithID_ActivityEdge> uml2withid_activityedges;




    private List<UML2WithID_StructuredActivityNode> uml2withid_structuredactivitynodes;




    private UML2WithID_State uml2withid_state;




    private UML2WithID_ActivityGroup uml2withid_activitygroup;


    public UML2WithID_Activity(
        String language,        boolean isSingleExecution,        String body,        boolean isReadOnly    ) {
        super(
        );
        this.language = language;
        this.isSingleExecution = isSingleExecution;
        this.body = body;
        this.isReadOnly = isReadOnly;
        this.uml2withid_activitynodes = new ArrayList<>();
        this.uml2withid_activitygroups = new ArrayList<>();
        this.uml2withid_activityedges = new ArrayList<>();
        this.uml2withid_structuredactivitynodes = new ArrayList<>();
    }

    public UML2WithID_Activity(
        String language,        boolean isSingleExecution,        String body,        boolean isReadOnly        ArrayList<UML2WithID_ActivityNode> uml2withid_activitynodes,        ArrayList<UML2WithID_ActivityGroup> uml2withid_activitygroups,        ArrayList<UML2WithID_ActivityEdge> uml2withid_activityedges,        ArrayList<UML2WithID_StructuredActivityNode> uml2withid_structuredactivitynodes    ) {
        this.language = language;
        this.isSingleExecution = isSingleExecution;
        this.body = body;
        this.isReadOnly = isReadOnly;
        this.uml2withid_activitynodes = uml2withid_activitynodes;
        this.uml2withid_activitygroups = uml2withid_activitygroups;
        this.uml2withid_activityedges = uml2withid_activityedges;
        this.uml2withid_structuredactivitynodes = uml2withid_structuredactivitynodes;
    }

    public String getLanguage() {
        return language;
    }

    public void setLanguage(String language) {
        this.language = language;
    }
    public boolean getIssingleexecution() {
        return isSingleExecution;
    }

    public void setIssingleexecution(boolean isSingleExecution) {
        this.isSingleExecution = isSingleExecution;
    }
    public String getBody() {
        return body;
    }

    public void setBody(String body) {
        this.body = body;
    }
    public boolean getIsreadonly() {
        return isReadOnly;
    }

    public void setIsreadonly(boolean isReadOnly) {
        this.isReadOnly = isReadOnly;
    }

    public UML2WithID_ActivityNode getUml2withid_activitynode() {
        return uml2withid_activitynode;
    }

    public void setUml2withid_activitynode(UML2WithID_ActivityNode uml2withid_activitynode) {
        this.uml2withid_activitynode = uml2withid_activitynode;
    }
    public UML2WithID_State getUml2withid_state() {
        return uml2withid_state;
    }

    public void setUml2withid_state(UML2WithID_State uml2withid_state) {
        this.uml2withid_state = uml2withid_state;
    }
    public UML2WithID_State getUml2withid_state() {
        return uml2withid_state;
    }

    public void setUml2withid_state(UML2WithID_State uml2withid_state) {
        this.uml2withid_state = uml2withid_state;
    }
    public List<UML2WithID_ActivityNode> getUml2withid_activitynodes() {
        return uml2withid_activitynodes;
    }

    public void addUml2withid_activitynode(Uml2withid_activitynode uml2withid_activitynode) {
        this.uml2withid_activitynodes.add(uml2withid_activitynode);
    }
    public UML2WithID_Transition getUml2withid_transition() {
        return uml2withid_transition;
    }

    public void setUml2withid_transition(UML2WithID_Transition uml2withid_transition) {
        this.uml2withid_transition = uml2withid_transition;
    }
    public List<UML2WithID_ActivityGroup> getUml2withid_activitygroups() {
        return uml2withid_activitygroups;
    }

    public void addUml2withid_activitygroup(Uml2withid_activitygroup uml2withid_activitygroup) {
        this.uml2withid_activitygroups.add(uml2withid_activitygroup);
    }
    public UML2WithID_ActivityEdge getUml2withid_activityedge() {
        return uml2withid_activityedge;
    }

    public void setUml2withid_activityedge(UML2WithID_ActivityEdge uml2withid_activityedge) {
        this.uml2withid_activityedge = uml2withid_activityedge;
    }
    public List<UML2WithID_ActivityEdge> getUml2withid_activityedges() {
        return uml2withid_activityedges;
    }

    public void addUml2withid_activityedge(Uml2withid_activityedge uml2withid_activityedge) {
        this.uml2withid_activityedges.add(uml2withid_activityedge);
    }
    public List<UML2WithID_StructuredActivityNode> getUml2withid_structuredactivitynodes() {
        return uml2withid_structuredactivitynodes;
    }

    public void addUml2withid_structuredactivitynode(Uml2withid_structuredactivitynode uml2withid_structuredactivitynode) {
        this.uml2withid_structuredactivitynodes.add(uml2withid_structuredactivitynode);
    }
    public UML2WithID_State getUml2withid_state() {
        return uml2withid_state;
    }

    public void setUml2withid_state(UML2WithID_State uml2withid_state) {
        this.uml2withid_state = uml2withid_state;
    }
    public UML2WithID_ActivityGroup getUml2withid_activitygroup() {
        return uml2withid_activitygroup;
    }

    public void setUml2withid_activitygroup(UML2WithID_ActivityGroup uml2withid_activitygroup) {
        this.uml2withid_activitygroup = uml2withid_activitygroup;
    }

}