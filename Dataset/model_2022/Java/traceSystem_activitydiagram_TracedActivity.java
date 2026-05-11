





import java.util.List;
import java.util.ArrayList;

public class traceSystem_activitydiagram_TracedActivity extends TracedNamedElement {






    private List<activitydiagram_TracedActivityNode> activitydiagram_tracedactivitynodes;




    private List<activitydiagram_TracedVariable> activitydiagram_tracedvariables;




    private List<Activity_trace_State> activity_trace_states;




    private List<activitydiagram_TracedVariable> activitydiagram_tracedvariables;


    public traceSystem_activitydiagram_TracedActivity(
    ) {
        super(
        );
        this.activitydiagram_tracedactivitynodes = new ArrayList<>();
        this.activitydiagram_tracedvariables = new ArrayList<>();
        this.activity_trace_states = new ArrayList<>();
        this.activitydiagram_tracedvariables = new ArrayList<>();
    }

    public traceSystem_activitydiagram_TracedActivity(
        ArrayList<activitydiagram_TracedActivityNode> activitydiagram_tracedactivitynodes,        ArrayList<activitydiagram_TracedVariable> activitydiagram_tracedvariables,        ArrayList<Activity_trace_State> activity_trace_states,        ArrayList<activitydiagram_TracedVariable> activitydiagram_tracedvariables    ) {
        this.activitydiagram_tracedactivitynodes = activitydiagram_tracedactivitynodes;
        this.activitydiagram_tracedvariables = activitydiagram_tracedvariables;
        this.activity_trace_states = activity_trace_states;
        this.activitydiagram_tracedvariables = activitydiagram_tracedvariables;
    }


    public List<activitydiagram_TracedActivityNode> getActivitydiagram_tracedactivitynodes() {
        return activitydiagram_tracedactivitynodes;
    }

    public void addActivitydiagram_tracedactivitynode(Activitydiagram_tracedactivitynode activitydiagram_tracedactivitynode) {
        this.activitydiagram_tracedactivitynodes.add(activitydiagram_tracedactivitynode);
    }
    public List<activitydiagram_TracedVariable> getActivitydiagram_tracedvariables() {
        return activitydiagram_tracedvariables;
    }

    public void addActivitydiagram_tracedvariable(Activitydiagram_tracedvariable activitydiagram_tracedvariable) {
        this.activitydiagram_tracedvariables.add(activitydiagram_tracedvariable);
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

}