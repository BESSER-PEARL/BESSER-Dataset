





import java.util.List;
import java.util.ArrayList;

public class traceSystem_States_Input_inputValues_State  {






    private List<activitydiagramConfiguration_TracedInputValue> activitydiagramconfiguration_tracedinputvalues;


    public traceSystem_States_Input_inputValues_State(
    ) {
        this.activitydiagramconfiguration_tracedinputvalues = new ArrayList<>();
    }

    public traceSystem_States_Input_inputValues_State(
        ArrayList<activitydiagramConfiguration_TracedInputValue> activitydiagramconfiguration_tracedinputvalues    ) {
        this.activitydiagramconfiguration_tracedinputvalues = activitydiagramconfiguration_tracedinputvalues;
    }


    public List<activitydiagramConfiguration_TracedInputValue> getActivitydiagramconfiguration_tracedinputvalues() {
        return activitydiagramconfiguration_tracedinputvalues;
    }

    public void addActivitydiagramconfiguration_tracedinputvalue(Activitydiagramconfiguration_tracedinputvalue activitydiagramconfiguration_tracedinputvalue) {
        this.activitydiagramconfiguration_tracedinputvalues.add(activitydiagramconfiguration_tracedinputvalue);
    }

}