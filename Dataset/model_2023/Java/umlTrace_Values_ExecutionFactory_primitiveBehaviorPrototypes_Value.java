





import java.util.List;
import java.util.ArrayList;

public class umlTrace_Values_ExecutionFactory_primitiveBehaviorPrototypes_Value  {






    private Loci_TracedExecutionFactory loci_tracedexecutionfactory;




    private List<Values_umlTrace_State> values_umltrace_states;


    public umlTrace_Values_ExecutionFactory_primitiveBehaviorPrototypes_Value(
    ) {
        this.values_umltrace_states = new ArrayList<>();
    }

    public umlTrace_Values_ExecutionFactory_primitiveBehaviorPrototypes_Value(
        ArrayList<Values_umlTrace_State> values_umltrace_states    ) {
        this.values_umltrace_states = values_umltrace_states;
    }


    public Loci_TracedExecutionFactory getLoci_tracedexecutionfactory() {
        return loci_tracedexecutionfactory;
    }

    public void setLoci_tracedexecutionfactory(Loci_TracedExecutionFactory loci_tracedexecutionfactory) {
        this.loci_tracedexecutionfactory = loci_tracedexecutionfactory;
    }
    public List<Values_umlTrace_State> getValues_umltrace_states() {
        return values_umltrace_states;
    }

    public void addValues_umltrace_state(Values_umltrace_state values_umltrace_state) {
        this.values_umltrace_states.add(values_umltrace_state);
    }

}