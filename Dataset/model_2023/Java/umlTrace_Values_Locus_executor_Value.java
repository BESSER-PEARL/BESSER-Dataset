





import java.util.List;
import java.util.ArrayList;

public class umlTrace_Values_Locus_executor_Value  {






    private List<Values_umlTrace_State> values_umltrace_states;




    private Loci_TracedLocus loci_tracedlocus;


    public umlTrace_Values_Locus_executor_Value(
    ) {
        this.values_umltrace_states = new ArrayList<>();
    }

    public umlTrace_Values_Locus_executor_Value(
        ArrayList<Values_umlTrace_State> values_umltrace_states    ) {
        this.values_umltrace_states = values_umltrace_states;
    }


    public List<Values_umlTrace_State> getValues_umltrace_states() {
        return values_umltrace_states;
    }

    public void addValues_umltrace_state(Values_umltrace_state values_umltrace_state) {
        this.values_umltrace_states.add(values_umltrace_state);
    }
    public Loci_TracedLocus getLoci_tracedlocus() {
        return loci_tracedlocus;
    }

    public void setLoci_tracedlocus(Loci_TracedLocus loci_tracedlocus) {
        this.loci_tracedlocus = loci_tracedlocus;
    }

}