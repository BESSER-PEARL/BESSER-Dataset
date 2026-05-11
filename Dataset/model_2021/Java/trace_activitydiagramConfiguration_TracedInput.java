





import java.util.List;
import java.util.ArrayList;

public class trace_activitydiagramConfiguration_TracedInput  {






    private List<Input_inputValues_State> input_inputvalues_states;


    public trace_activitydiagramConfiguration_TracedInput(
    ) {
        this.input_inputvalues_states = new ArrayList<>();
    }

    public trace_activitydiagramConfiguration_TracedInput(
        ArrayList<Input_inputValues_State> input_inputvalues_states    ) {
        this.input_inputvalues_states = input_inputvalues_states;
    }


    public List<Input_inputValues_State> getInput_inputvalues_states() {
        return input_inputvalues_states;
    }

    public void addInput_inputvalues_state(Input_inputvalues_state input_inputvalues_state) {
        this.input_inputvalues_states.add(input_inputvalues_state);
    }

}