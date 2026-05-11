





import java.util.List;
import java.util.ArrayList;

public class traceSystem_activitydiagramConfiguration_TracedInputValue  {






    private List<InputValue_variable_State> inputvalue_variable_states;




    private List<InputValue_value_State> inputvalue_value_states;


    public traceSystem_activitydiagramConfiguration_TracedInputValue(
    ) {
        this.inputvalue_variable_states = new ArrayList<>();
        this.inputvalue_value_states = new ArrayList<>();
    }

    public traceSystem_activitydiagramConfiguration_TracedInputValue(
        ArrayList<InputValue_variable_State> inputvalue_variable_states,        ArrayList<InputValue_value_State> inputvalue_value_states    ) {
        this.inputvalue_variable_states = inputvalue_variable_states;
        this.inputvalue_value_states = inputvalue_value_states;
    }


    public List<InputValue_variable_State> getInputvalue_variable_states() {
        return inputvalue_variable_states;
    }

    public void addInputvalue_variable_state(Inputvalue_variable_state inputvalue_variable_state) {
        this.inputvalue_variable_states.add(inputvalue_variable_state);
    }
    public List<InputValue_value_State> getInputvalue_value_states() {
        return inputvalue_value_states;
    }

    public void addInputvalue_value_state(Inputvalue_value_state inputvalue_value_state) {
        this.inputvalue_value_states.add(inputvalue_value_state);
    }

}