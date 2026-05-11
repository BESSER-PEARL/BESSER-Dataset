





import java.util.List;
import java.util.ArrayList;

public class trace_activitydiagram_TracedActivityNode extends TracedNamedElement {






    private List<activitydiagram_TracedActivityEdge> activitydiagram_tracedactivityedges;




    private List<ActivityNode_heldTokens_State> activitynode_heldtokens_states;




    private List<ActivityNode_running_State> activitynode_running_states;




    private activitydiagram_TracedActivity activitydiagram_tracedactivity;




    private List<activitydiagram_TracedActivityEdge> activitydiagram_tracedactivityedges;


    public trace_activitydiagram_TracedActivityNode(
    ) {
        super(
        );
        this.activitydiagram_tracedactivityedges = new ArrayList<>();
        this.activitynode_heldtokens_states = new ArrayList<>();
        this.activitynode_running_states = new ArrayList<>();
        this.activitydiagram_tracedactivityedges = new ArrayList<>();
    }

    public trace_activitydiagram_TracedActivityNode(
        ArrayList<activitydiagram_TracedActivityEdge> activitydiagram_tracedactivityedges,        ArrayList<ActivityNode_heldTokens_State> activitynode_heldtokens_states,        ArrayList<ActivityNode_running_State> activitynode_running_states,        ArrayList<activitydiagram_TracedActivityEdge> activitydiagram_tracedactivityedges    ) {
        this.activitydiagram_tracedactivityedges = activitydiagram_tracedactivityedges;
        this.activitynode_heldtokens_states = activitynode_heldtokens_states;
        this.activitynode_running_states = activitynode_running_states;
        this.activitydiagram_tracedactivityedges = activitydiagram_tracedactivityedges;
    }


    public List<activitydiagram_TracedActivityEdge> getActivitydiagram_tracedactivityedges() {
        return activitydiagram_tracedactivityedges;
    }

    public void addActivitydiagram_tracedactivityedge(Activitydiagram_tracedactivityedge activitydiagram_tracedactivityedge) {
        this.activitydiagram_tracedactivityedges.add(activitydiagram_tracedactivityedge);
    }
    public List<ActivityNode_heldTokens_State> getActivitynode_heldtokens_states() {
        return activitynode_heldtokens_states;
    }

    public void addActivitynode_heldtokens_state(Activitynode_heldtokens_state activitynode_heldtokens_state) {
        this.activitynode_heldtokens_states.add(activitynode_heldtokens_state);
    }
    public List<ActivityNode_running_State> getActivitynode_running_states() {
        return activitynode_running_states;
    }

    public void addActivitynode_running_state(Activitynode_running_state activitynode_running_state) {
        this.activitynode_running_states.add(activitynode_running_state);
    }
    public activitydiagram_TracedActivity getActivitydiagram_tracedactivity() {
        return activitydiagram_tracedactivity;
    }

    public void setActivitydiagram_tracedactivity(activitydiagram_TracedActivity activitydiagram_tracedactivity) {
        this.activitydiagram_tracedactivity = activitydiagram_tracedactivity;
    }
    public List<activitydiagram_TracedActivityEdge> getActivitydiagram_tracedactivityedges() {
        return activitydiagram_tracedactivityedges;
    }

    public void addActivitydiagram_tracedactivityedge(Activitydiagram_tracedactivityedge activitydiagram_tracedactivityedge) {
        this.activitydiagram_tracedactivityedges.add(activitydiagram_tracedactivityedge);
    }

}