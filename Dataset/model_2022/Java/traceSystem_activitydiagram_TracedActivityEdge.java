





import java.util.List;
import java.util.ArrayList;

public class traceSystem_activitydiagram_TracedActivityEdge extends TracedNamedElement {






    private activitydiagram_TracedActivityNode activitydiagram_tracedactivitynode;




    private activitydiagram_TracedActivityNode activitydiagram_tracedactivitynode;




    private List<ActivityEdge_offers_State> activityedge_offers_states;


    public traceSystem_activitydiagram_TracedActivityEdge(
    ) {
        super(
        );
        this.activityedge_offers_states = new ArrayList<>();
    }

    public traceSystem_activitydiagram_TracedActivityEdge(
        ArrayList<ActivityEdge_offers_State> activityedge_offers_states    ) {
        this.activityedge_offers_states = activityedge_offers_states;
    }


    public activitydiagram_TracedActivityNode getActivitydiagram_tracedactivitynode() {
        return activitydiagram_tracedactivitynode;
    }

    public void setActivitydiagram_tracedactivitynode(activitydiagram_TracedActivityNode activitydiagram_tracedactivitynode) {
        this.activitydiagram_tracedactivitynode = activitydiagram_tracedactivitynode;
    }
    public activitydiagram_TracedActivityNode getActivitydiagram_tracedactivitynode() {
        return activitydiagram_tracedactivitynode;
    }

    public void setActivitydiagram_tracedactivitynode(activitydiagram_TracedActivityNode activitydiagram_tracedactivitynode) {
        this.activitydiagram_tracedactivitynode = activitydiagram_tracedactivitynode;
    }
    public List<ActivityEdge_offers_State> getActivityedge_offers_states() {
        return activityedge_offers_states;
    }

    public void addActivityedge_offers_state(Activityedge_offers_state activityedge_offers_state) {
        this.activityedge_offers_states.add(activityedge_offers_state);
    }

}