





import java.util.List;
import java.util.ArrayList;

public class trace_States_ActivityNode_running_State  {

    private boolean running;





    private List<States_trace_GlobalState> states_trace_globalstates;




    private activitydiagram_TracedActivityNode activitydiagram_tracedactivitynode;


    public trace_States_ActivityNode_running_State(
        boolean running    ) {
        this.running = running;
        this.states_trace_globalstates = new ArrayList<>();
    }

    public trace_States_ActivityNode_running_State(
        boolean running        ArrayList<States_trace_GlobalState> states_trace_globalstates    ) {
        this.running = running;
        this.states_trace_globalstates = states_trace_globalstates;
    }

    public boolean getRunning() {
        return running;
    }

    public void setRunning(boolean running) {
        this.running = running;
    }

    public List<States_trace_GlobalState> getStates_trace_globalstates() {
        return states_trace_globalstates;
    }

    public void addStates_trace_globalstate(States_trace_globalstate states_trace_globalstate) {
        this.states_trace_globalstates.add(states_trace_globalstate);
    }
    public activitydiagram_TracedActivityNode getActivitydiagram_tracedactivitynode() {
        return activitydiagram_tracedactivitynode;
    }

    public void setActivitydiagram_tracedactivitynode(activitydiagram_TracedActivityNode activitydiagram_tracedactivitynode) {
        this.activitydiagram_tracedactivitynode = activitydiagram_tracedactivitynode;
    }

}