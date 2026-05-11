





import java.util.List;
import java.util.ArrayList;

public class umlTrace_Values_Reference_referent_Value  {






    private List<Values_umlTrace_State> values_umltrace_states;




    private Kernel_TracedObject kernel_tracedobject;


    public umlTrace_Values_Reference_referent_Value(
    ) {
        this.values_umltrace_states = new ArrayList<>();
    }

    public umlTrace_Values_Reference_referent_Value(
        ArrayList<Values_umlTrace_State> values_umltrace_states    ) {
        this.values_umltrace_states = values_umltrace_states;
    }


    public List<Values_umlTrace_State> getValues_umltrace_states() {
        return values_umltrace_states;
    }

    public void addValues_umltrace_state(Values_umltrace_state values_umltrace_state) {
        this.values_umltrace_states.add(values_umltrace_state);
    }
    public Kernel_TracedObject getKernel_tracedobject() {
        return kernel_tracedobject;
    }

    public void setKernel_tracedobject(Kernel_TracedObject kernel_tracedobject) {
        this.kernel_tracedobject = kernel_tracedobject;
    }

}