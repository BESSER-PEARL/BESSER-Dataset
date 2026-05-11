





import java.util.List;
import java.util.ArrayList;

public class trace_States_Input_inputValues_State  {






    private List<activitydiagramConfiguration_TracedInputValue> activitydiagramconfiguration_tracedinputvalues;




    private List<States_trace_GlobalState> states_trace_globalstates;


    public trace_States_Input_inputValues_State(
    ) {
        this.activitydiagramconfiguration_tracedinputvalues = new ArrayList<>();
        this.states_trace_globalstates = new ArrayList<>();
    }

    public trace_States_Input_inputValues_State(
        ArrayList<activitydiagramConfiguration_TracedInputValue> activitydiagramconfiguration_tracedinputvalues,        ArrayList<States_trace_GlobalState> states_trace_globalstates    ) {
        this.activitydiagramconfiguration_tracedinputvalues = activitydiagramconfiguration_tracedinputvalues;
        this.states_trace_globalstates = states_trace_globalstates;
    }


    public List<activitydiagramConfiguration_TracedInputValue> getActivitydiagramconfiguration_tracedinputvalues() {
        return activitydiagramconfiguration_tracedinputvalues;
    }

    public void addActivitydiagramconfiguration_tracedinputvalue(Activitydiagramconfiguration_tracedinputvalue activitydiagramconfiguration_tracedinputvalue) {
        this.activitydiagramconfiguration_tracedinputvalues.add(activitydiagramconfiguration_tracedinputvalue);
    }
    public List<States_trace_GlobalState> getStates_trace_globalstates() {
        return states_trace_globalstates;
    }

    public void addStates_trace_globalstate(States_trace_globalstate states_trace_globalstate) {
        this.states_trace_globalstates.add(states_trace_globalstate);
    }

}