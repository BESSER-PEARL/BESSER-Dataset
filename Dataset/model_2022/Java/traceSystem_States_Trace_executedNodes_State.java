





import java.util.List;
import java.util.ArrayList;

public class traceSystem_States_Trace_executedNodes_State  {






    private List<activitydiagram_TracedActivityNode> activitydiagram_tracedactivitynodes;




    private activitydiagramConfiguration_TracedTrace activitydiagramconfiguration_tracedtrace;


    public traceSystem_States_Trace_executedNodes_State(
    ) {
        this.activitydiagram_tracedactivitynodes = new ArrayList<>();
    }

    public traceSystem_States_Trace_executedNodes_State(
        ArrayList<activitydiagram_TracedActivityNode> activitydiagram_tracedactivitynodes    ) {
        this.activitydiagram_tracedactivitynodes = activitydiagram_tracedactivitynodes;
    }


    public List<activitydiagram_TracedActivityNode> getActivitydiagram_tracedactivitynodes() {
        return activitydiagram_tracedactivitynodes;
    }

    public void addActivitydiagram_tracedactivitynode(Activitydiagram_tracedactivitynode activitydiagram_tracedactivitynode) {
        this.activitydiagram_tracedactivitynodes.add(activitydiagram_tracedactivitynode);
    }
    public activitydiagramConfiguration_TracedTrace getActivitydiagramconfiguration_tracedtrace() {
        return activitydiagramconfiguration_tracedtrace;
    }

    public void setActivitydiagramconfiguration_tracedtrace(activitydiagramConfiguration_TracedTrace activitydiagramconfiguration_tracedtrace) {
        this.activitydiagramconfiguration_tracedtrace = activitydiagramconfiguration_tracedtrace;
    }

}