





import java.util.List;
import java.util.ArrayList;

public class automation_Automation extends NamedElement {






    private List<automation_Transition> automation_transitions;




    private List<automation_Output> automation_outputs;




    private List<automation_State> automation_states;




    private List<automation_Input> automation_inputs;


    public automation_Automation(
    ) {
        super(
        );
        this.automation_transitions = new ArrayList<>();
        this.automation_outputs = new ArrayList<>();
        this.automation_states = new ArrayList<>();
        this.automation_inputs = new ArrayList<>();
    }

    public automation_Automation(
        ArrayList<automation_Transition> automation_transitions,        ArrayList<automation_Output> automation_outputs,        ArrayList<automation_State> automation_states,        ArrayList<automation_Input> automation_inputs    ) {
        this.automation_transitions = automation_transitions;
        this.automation_outputs = automation_outputs;
        this.automation_states = automation_states;
        this.automation_inputs = automation_inputs;
    }


    public List<automation_Transition> getAutomation_transitions() {
        return automation_transitions;
    }

    public void addAutomation_transition(Automation_transition automation_transition) {
        this.automation_transitions.add(automation_transition);
    }
    public List<automation_Output> getAutomation_outputs() {
        return automation_outputs;
    }

    public void addAutomation_output(Automation_output automation_output) {
        this.automation_outputs.add(automation_output);
    }
    public List<automation_State> getAutomation_states() {
        return automation_states;
    }

    public void addAutomation_state(Automation_state automation_state) {
        this.automation_states.add(automation_state);
    }
    public List<automation_Input> getAutomation_inputs() {
        return automation_inputs;
    }

    public void addAutomation_input(Automation_input automation_input) {
        this.automation_inputs.add(automation_input);
    }

}