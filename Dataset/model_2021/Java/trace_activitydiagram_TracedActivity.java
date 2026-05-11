





import java.util.List;
import java.util.ArrayList;

public class trace_activitydiagram_TracedActivity extends TracedNamedElement {






    private List<Activity_trace_State> activity_trace_states;




    private List<activitydiagram_TracedVariable> activitydiagram_tracedvariables;




    private List<activitydiagram_TracedActivityEdge> activitydiagram_tracedactivityedges;




    private List<activitydiagram_TracedVariable> activitydiagram_tracedvariables;




    private List<activitydiagram_TracedActivityNode> activitydiagram_tracedactivitynodes;


    public trace_activitydiagram_TracedActivity(
    ) {
        super(
        );
        this.activity_trace_states = new ArrayList<>();
        this.activitydiagram_tracedvariables = new ArrayList<>();
        this.activitydiagram_tracedactivityedges = new ArrayList<>();
        this.activitydiagram_tracedvariables = new ArrayList<>();
        this.activitydiagram_tracedactivitynodes = new ArrayList<>();
    }

    public trace_activitydiagram_TracedActivity(
        ArrayList<Activity_trace_State> activity_trace_states,        ArrayList<activitydiagram_TracedVariable> activitydiagram_tracedvariables,        ArrayList<activitydiagram_TracedActivityEdge> activitydiagram_tracedactivityedges,        ArrayList<activitydiagram_TracedVariable> activitydiagram_tracedvariables,        ArrayList<activitydiagram_TracedActivityNode> activitydiagram_tracedactivitynodes    ) {
        this.activity_trace_states = activity_trace_states;
        this.activitydiagram_tracedvariables = activitydiagram_tracedvariables;
        this.activitydiagram_tracedactivityedges = activitydiagram_tracedactivityedges;
        this.activitydiagram_tracedvariables = activitydiagram_tracedvariables;
        this.activitydiagram_tracedactivitynodes = activitydiagram_tracedactivitynodes;
    }


    public List<Activity_trace_State> getActivity_trace_states() {
        return activity_trace_states;
    }

    public void addActivity_trace_state(Activity_trace_state activity_trace_state) {
        this.activity_trace_states.add(activity_trace_state);
    }
    public List<activitydiagram_TracedVariable> getActivitydiagram_tracedvariables() {
        return activitydiagram_tracedvariables;
    }

    public void addActivitydiagram_tracedvariable(Activitydiagram_tracedvariable activitydiagram_tracedvariable) {
        this.activitydiagram_tracedvariables.add(activitydiagram_tracedvariable);
    }
    public List<activitydiagram_TracedActivityEdge> getActivitydiagram_tracedactivityedges() {
        return activitydiagram_tracedactivityedges;
    }

    public void addActivitydiagram_tracedactivityedge(Activitydiagram_tracedactivityedge activitydiagram_tracedactivityedge) {
        this.activitydiagram_tracedactivityedges.add(activitydiagram_tracedactivityedge);
    }
    public List<activitydiagram_TracedVariable> getActivitydiagram_tracedvariables() {
        return activitydiagram_tracedvariables;
    }

    public void addActivitydiagram_tracedvariable(Activitydiagram_tracedvariable activitydiagram_tracedvariable) {
        this.activitydiagram_tracedvariables.add(activitydiagram_tracedvariable);
    }
    public List<activitydiagram_TracedActivityNode> getActivitydiagram_tracedactivitynodes() {
        return activitydiagram_tracedactivitynodes;
    }

    public void addActivitydiagram_tracedactivitynode(Activitydiagram_tracedactivitynode activitydiagram_tracedactivitynode) {
        this.activitydiagram_tracedactivitynodes.add(activitydiagram_tracedactivitynode);
    }

}