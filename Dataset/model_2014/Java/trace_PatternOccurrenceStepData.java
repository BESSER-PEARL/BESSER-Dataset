





import java.util.List;
import java.util.ArrayList;

public class trace_PatternOccurrenceStepData  {






    private List<trace_State> trace_states;




    private trace_PatternOcurrence trace_patternocurrence;




    private trace_RepeatingStep trace_repeatingstep;




    private List<trace_ParameterList> trace_parameterlists;


    public trace_PatternOccurrenceStepData(
    ) {
        this.trace_states = new ArrayList<>();
        this.trace_parameterlists = new ArrayList<>();
    }

    public trace_PatternOccurrenceStepData(
        ArrayList<trace_State> trace_states,        ArrayList<trace_ParameterList> trace_parameterlists    ) {
        this.trace_states = trace_states;
        this.trace_parameterlists = trace_parameterlists;
    }


    public List<trace_State> getTrace_states() {
        return trace_states;
    }

    public void addTrace_state(Trace_state trace_state) {
        this.trace_states.add(trace_state);
    }
    public trace_PatternOcurrence getTrace_patternocurrence() {
        return trace_patternocurrence;
    }

    public void setTrace_patternocurrence(trace_PatternOcurrence trace_patternocurrence) {
        this.trace_patternocurrence = trace_patternocurrence;
    }
    public trace_RepeatingStep getTrace_repeatingstep() {
        return trace_repeatingstep;
    }

    public void setTrace_repeatingstep(trace_RepeatingStep trace_repeatingstep) {
        this.trace_repeatingstep = trace_repeatingstep;
    }
    public List<trace_ParameterList> getTrace_parameterlists() {
        return trace_parameterlists;
    }

    public void addTrace_parameterlist(Trace_parameterlist trace_parameterlist) {
        this.trace_parameterlists.add(trace_parameterlist);
    }

}