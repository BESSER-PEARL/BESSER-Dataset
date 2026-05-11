





import java.util.List;
import java.util.ArrayList;

public class traceSystem_activitydiagram_TracedVariable extends TracedNamedElement {






    private List<Variable_currentValue_State> variable_currentvalue_states;


    public traceSystem_activitydiagram_TracedVariable(
    ) {
        super(
        );
        this.variable_currentvalue_states = new ArrayList<>();
    }

    public traceSystem_activitydiagram_TracedVariable(
        ArrayList<Variable_currentValue_State> variable_currentvalue_states    ) {
        this.variable_currentvalue_states = variable_currentvalue_states;
    }


    public List<Variable_currentValue_State> getVariable_currentvalue_states() {
        return variable_currentvalue_states;
    }

    public void addVariable_currentvalue_state(Variable_currentvalue_state variable_currentvalue_state) {
        this.variable_currentvalue_states.add(variable_currentvalue_state);
    }

}