





import java.util.List;
import java.util.ArrayList;

public class umlTrace_BasicBehaviors_TracedExecution extends TracedObject {






    private List<Execution_context_Value> execution_context_values;




    private List<Execution_parameterValues_Value> execution_parametervalues_values;


    public umlTrace_BasicBehaviors_TracedExecution(
    ) {
        super(
        );
        this.execution_context_values = new ArrayList<>();
        this.execution_parametervalues_values = new ArrayList<>();
    }

    public umlTrace_BasicBehaviors_TracedExecution(
        ArrayList<Execution_context_Value> execution_context_values,        ArrayList<Execution_parameterValues_Value> execution_parametervalues_values    ) {
        this.execution_context_values = execution_context_values;
        this.execution_parametervalues_values = execution_parametervalues_values;
    }


    public List<Execution_context_Value> getExecution_context_values() {
        return execution_context_values;
    }

    public void addExecution_context_value(Execution_context_value execution_context_value) {
        this.execution_context_values.add(execution_context_value);
    }
    public List<Execution_parameterValues_Value> getExecution_parametervalues_values() {
        return execution_parametervalues_values;
    }

    public void addExecution_parametervalues_value(Execution_parametervalues_value execution_parametervalues_value) {
        this.execution_parametervalues_values.add(execution_parametervalues_value);
    }

}