





import java.util.List;
import java.util.ArrayList;

public class umlTrace_Values_ParameterValue_parameter_ParameterValue_Value  {






    private List<Values_umlTrace_State> values_umltrace_states;




    private BasicBehaviors_TracedParameterValue basicbehaviors_tracedparametervalue;


    public umlTrace_Values_ParameterValue_parameter_ParameterValue_Value(
    ) {
        this.values_umltrace_states = new ArrayList<>();
    }

    public umlTrace_Values_ParameterValue_parameter_ParameterValue_Value(
        ArrayList<Values_umlTrace_State> values_umltrace_states    ) {
        this.values_umltrace_states = values_umltrace_states;
    }


    public List<Values_umlTrace_State> getValues_umltrace_states() {
        return values_umltrace_states;
    }

    public void addValues_umltrace_state(Values_umltrace_state values_umltrace_state) {
        this.values_umltrace_states.add(values_umltrace_state);
    }
    public BasicBehaviors_TracedParameterValue getBasicbehaviors_tracedparametervalue() {
        return basicbehaviors_tracedparametervalue;
    }

    public void setBasicbehaviors_tracedparametervalue(BasicBehaviors_TracedParameterValue basicbehaviors_tracedparametervalue) {
        this.basicbehaviors_tracedparametervalue = basicbehaviors_tracedparametervalue;
    }

}