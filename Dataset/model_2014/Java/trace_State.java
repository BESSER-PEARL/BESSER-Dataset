





import java.util.List;
import java.util.ArrayList;

public class trace_State  {






    private trace_State trace_state;




    private trace_Step trace_step;




    private List<trace_TransientObject> trace_transientobjects;




    private trace_Trace trace_trace;




    private List<trace_TransientObject> trace_transientobjects;


    public trace_State(
    ) {
        this.trace_transientobjects = new ArrayList<>();
        this.trace_transientobjects = new ArrayList<>();
    }

    public trace_State(
        ArrayList<trace_TransientObject> trace_transientobjects,        ArrayList<trace_TransientObject> trace_transientobjects    ) {
        this.trace_transientobjects = trace_transientobjects;
        this.trace_transientobjects = trace_transientobjects;
    }


    public trace_State getTrace_state() {
        return trace_state;
    }

    public void setTrace_state(trace_State trace_state) {
        this.trace_state = trace_state;
    }
    public trace_Step getTrace_step() {
        return trace_step;
    }

    public void setTrace_step(trace_Step trace_step) {
        this.trace_step = trace_step;
    }
    public List<trace_TransientObject> getTrace_transientobjects() {
        return trace_transientobjects;
    }

    public void addTrace_transientobject(Trace_transientobject trace_transientobject) {
        this.trace_transientobjects.add(trace_transientobject);
    }
    public trace_Trace getTrace_trace() {
        return trace_trace;
    }

    public void setTrace_trace(trace_Trace trace_trace) {
        this.trace_trace = trace_trace;
    }
    public List<trace_TransientObject> getTrace_transientobjects() {
        return trace_transientobjects;
    }

    public void addTrace_transientobject(Trace_transientobject trace_transientobject) {
        this.trace_transientobjects.add(trace_transientobject);
    }

}