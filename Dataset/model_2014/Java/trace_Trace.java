





import java.util.List;
import java.util.ArrayList;

public class trace_Trace  {






    private List<trace_StepPattern> trace_steppatterns;




    private List<trace_ObjectState> trace_objectstates;




    private List<trace_TransientObject> trace_transientobjects;




    private List<trace_ParameterList> trace_parameterlists;




    private List<trace_Value> trace_values;




    private List<trace_RepeatingStep> trace_repeatingsteps;




    private List<trace_ParameterValue> trace_parametervalues;




    private List<trace_Step> trace_steps;


    public trace_Trace(
    ) {
        this.trace_steppatterns = new ArrayList<>();
        this.trace_objectstates = new ArrayList<>();
        this.trace_transientobjects = new ArrayList<>();
        this.trace_parameterlists = new ArrayList<>();
        this.trace_values = new ArrayList<>();
        this.trace_repeatingsteps = new ArrayList<>();
        this.trace_parametervalues = new ArrayList<>();
        this.trace_steps = new ArrayList<>();
    }

    public trace_Trace(
        ArrayList<trace_StepPattern> trace_steppatterns,        ArrayList<trace_ObjectState> trace_objectstates,        ArrayList<trace_TransientObject> trace_transientobjects,        ArrayList<trace_ParameterList> trace_parameterlists,        ArrayList<trace_Value> trace_values,        ArrayList<trace_RepeatingStep> trace_repeatingsteps,        ArrayList<trace_ParameterValue> trace_parametervalues,        ArrayList<trace_Step> trace_steps    ) {
        this.trace_steppatterns = trace_steppatterns;
        this.trace_objectstates = trace_objectstates;
        this.trace_transientobjects = trace_transientobjects;
        this.trace_parameterlists = trace_parameterlists;
        this.trace_values = trace_values;
        this.trace_repeatingsteps = trace_repeatingsteps;
        this.trace_parametervalues = trace_parametervalues;
        this.trace_steps = trace_steps;
    }


    public List<trace_StepPattern> getTrace_steppatterns() {
        return trace_steppatterns;
    }

    public void addTrace_steppattern(Trace_steppattern trace_steppattern) {
        this.trace_steppatterns.add(trace_steppattern);
    }
    public List<trace_ObjectState> getTrace_objectstates() {
        return trace_objectstates;
    }

    public void addTrace_objectstate(Trace_objectstate trace_objectstate) {
        this.trace_objectstates.add(trace_objectstate);
    }
    public List<trace_TransientObject> getTrace_transientobjects() {
        return trace_transientobjects;
    }

    public void addTrace_transientobject(Trace_transientobject trace_transientobject) {
        this.trace_transientobjects.add(trace_transientobject);
    }
    public List<trace_ParameterList> getTrace_parameterlists() {
        return trace_parameterlists;
    }

    public void addTrace_parameterlist(Trace_parameterlist trace_parameterlist) {
        this.trace_parameterlists.add(trace_parameterlist);
    }
    public List<trace_Value> getTrace_values() {
        return trace_values;
    }

    public void addTrace_value(Trace_value trace_value) {
        this.trace_values.add(trace_value);
    }
    public List<trace_RepeatingStep> getTrace_repeatingsteps() {
        return trace_repeatingsteps;
    }

    public void addTrace_repeatingstep(Trace_repeatingstep trace_repeatingstep) {
        this.trace_repeatingsteps.add(trace_repeatingstep);
    }
    public List<trace_ParameterValue> getTrace_parametervalues() {
        return trace_parametervalues;
    }

    public void addTrace_parametervalue(Trace_parametervalue trace_parametervalue) {
        this.trace_parametervalues.add(trace_parametervalue);
    }
    public List<trace_Step> getTrace_steps() {
        return trace_steps;
    }

    public void addTrace_step(Trace_step trace_step) {
        this.trace_steps.add(trace_step);
    }

}