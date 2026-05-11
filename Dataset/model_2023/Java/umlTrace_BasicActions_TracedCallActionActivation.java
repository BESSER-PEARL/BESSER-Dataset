





import java.util.List;
import java.util.ArrayList;

public class umlTrace_BasicActions_TracedCallActionActivation extends TracedInvocationActionActivation {






    private List<CallActionActivation_callExecutions_Value> callactionactivation_callexecutions_values;


    public umlTrace_BasicActions_TracedCallActionActivation(
    ) {
        super(
        );
        this.callactionactivation_callexecutions_values = new ArrayList<>();
    }

    public umlTrace_BasicActions_TracedCallActionActivation(
        ArrayList<CallActionActivation_callExecutions_Value> callactionactivation_callexecutions_values    ) {
        this.callactionactivation_callexecutions_values = callactionactivation_callexecutions_values;
    }


    public List<CallActionActivation_callExecutions_Value> getCallactionactivation_callexecutions_values() {
        return callactionactivation_callexecutions_values;
    }

    public void addCallactionactivation_callexecutions_value(Callactionactivation_callexecutions_value callactionactivation_callexecutions_value) {
        this.callactionactivation_callexecutions_values.add(callactionactivation_callexecutions_value);
    }

}