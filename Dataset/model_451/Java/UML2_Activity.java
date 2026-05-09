





import java.util.List;
import java.util.ArrayList;

public class UML2_Activity extends Behavior {

    private String language;
    private boolean isReadOnly;
    private String body;
    private boolean isSingleExecution;





    private UML2_State uml2_state;




    private UML2_State uml2_state;




    private List<UML2_ActivityNode> uml2_activitynodes;




    private List<UML2_StructuredActivityNode> uml2_structuredactivitynodes;




    private UML2_Transition uml2_transition;




    private List<UML2_ActivityGroup> uml2_activitygroups;




    private UML2_ActivityGroup uml2_activitygroup;




    private List<UML2_Action> uml2_actions;




    private UML2_ActivityNode uml2_activitynode;




    private List<UML2_ActivityEdge> uml2_activityedges;




    private UML2_State uml2_state;




    private UML2_ActivityEdge uml2_activityedge;


    public UML2_Activity(
        String language,        boolean isReadOnly,        String body,        boolean isSingleExecution    ) {
        super(
        );
        this.language = language;
        this.isReadOnly = isReadOnly;
        this.body = body;
        this.isSingleExecution = isSingleExecution;
        this.uml2_activitynodes = new ArrayList<>();
        this.uml2_structuredactivitynodes = new ArrayList<>();
        this.uml2_activitygroups = new ArrayList<>();
        this.uml2_actions = new ArrayList<>();
        this.uml2_activityedges = new ArrayList<>();
    }

    public UML2_Activity(
        String language,        boolean isReadOnly,        String body,        boolean isSingleExecution        ArrayList<UML2_ActivityNode> uml2_activitynodes,        ArrayList<UML2_StructuredActivityNode> uml2_structuredactivitynodes,        ArrayList<UML2_ActivityGroup> uml2_activitygroups,        ArrayList<UML2_Action> uml2_actions,        ArrayList<UML2_ActivityEdge> uml2_activityedges    ) {
        this.language = language;
        this.isReadOnly = isReadOnly;
        this.body = body;
        this.isSingleExecution = isSingleExecution;
        this.uml2_activitynodes = uml2_activitynodes;
        this.uml2_structuredactivitynodes = uml2_structuredactivitynodes;
        this.uml2_activitygroups = uml2_activitygroups;
        this.uml2_actions = uml2_actions;
        this.uml2_activityedges = uml2_activityedges;
    }

    public String getLanguage() {
        return language;
    }

    public void setLanguage(String language) {
        this.language = language;
    }
    public boolean getIsreadonly() {
        return isReadOnly;
    }

    public void setIsreadonly(boolean isReadOnly) {
        this.isReadOnly = isReadOnly;
    }
    public String getBody() {
        return body;
    }

    public void setBody(String body) {
        this.body = body;
    }
    public boolean getIssingleexecution() {
        return isSingleExecution;
    }

    public void setIssingleexecution(boolean isSingleExecution) {
        this.isSingleExecution = isSingleExecution;
    }

    public UML2_State getUml2_state() {
        return uml2_state;
    }

    public void setUml2_state(UML2_State uml2_state) {
        this.uml2_state = uml2_state;
    }
    public UML2_State getUml2_state() {
        return uml2_state;
    }

    public void setUml2_state(UML2_State uml2_state) {
        this.uml2_state = uml2_state;
    }
    public List<UML2_ActivityNode> getUml2_activitynodes() {
        return uml2_activitynodes;
    }

    public void addUml2_activitynode(Uml2_activitynode uml2_activitynode) {
        this.uml2_activitynodes.add(uml2_activitynode);
    }
    public List<UML2_StructuredActivityNode> getUml2_structuredactivitynodes() {
        return uml2_structuredactivitynodes;
    }

    public void addUml2_structuredactivitynode(Uml2_structuredactivitynode uml2_structuredactivitynode) {
        this.uml2_structuredactivitynodes.add(uml2_structuredactivitynode);
    }
    public UML2_Transition getUml2_transition() {
        return uml2_transition;
    }

    public void setUml2_transition(UML2_Transition uml2_transition) {
        this.uml2_transition = uml2_transition;
    }
    public List<UML2_ActivityGroup> getUml2_activitygroups() {
        return uml2_activitygroups;
    }

    public void addUml2_activitygroup(Uml2_activitygroup uml2_activitygroup) {
        this.uml2_activitygroups.add(uml2_activitygroup);
    }
    public UML2_ActivityGroup getUml2_activitygroup() {
        return uml2_activitygroup;
    }

    public void setUml2_activitygroup(UML2_ActivityGroup uml2_activitygroup) {
        this.uml2_activitygroup = uml2_activitygroup;
    }
    public List<UML2_Action> getUml2_actions() {
        return uml2_actions;
    }

    public void addUml2_action(Uml2_action uml2_action) {
        this.uml2_actions.add(uml2_action);
    }
    public UML2_ActivityNode getUml2_activitynode() {
        return uml2_activitynode;
    }

    public void setUml2_activitynode(UML2_ActivityNode uml2_activitynode) {
        this.uml2_activitynode = uml2_activitynode;
    }
    public List<UML2_ActivityEdge> getUml2_activityedges() {
        return uml2_activityedges;
    }

    public void addUml2_activityedge(Uml2_activityedge uml2_activityedge) {
        this.uml2_activityedges.add(uml2_activityedge);
    }
    public UML2_State getUml2_state() {
        return uml2_state;
    }

    public void setUml2_state(UML2_State uml2_state) {
        this.uml2_state = uml2_state;
    }
    public UML2_ActivityEdge getUml2_activityedge() {
        return uml2_activityedge;
    }

    public void setUml2_activityedge(UML2_ActivityEdge uml2_activityedge) {
        this.uml2_activityedge = uml2_activityedge;
    }

}