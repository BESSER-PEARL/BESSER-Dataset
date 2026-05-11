





import java.util.List;
import java.util.ArrayList;

public class trace_TracedObject  {






    private List<trace_ObjectState> trace_objectstates;




    private trace_Trace trace_trace;




    private trace_ObjectState trace_objectstate;


    public trace_TracedObject(
    ) {
        this.trace_objectstates = new ArrayList<>();
    }

    public trace_TracedObject(
        ArrayList<trace_ObjectState> trace_objectstates    ) {
        this.trace_objectstates = trace_objectstates;
    }


    public List<trace_ObjectState> getTrace_objectstates() {
        return trace_objectstates;
    }

    public void addTrace_objectstate(Trace_objectstate trace_objectstate) {
        this.trace_objectstates.add(trace_objectstate);
    }
    public trace_Trace getTrace_trace() {
        return trace_trace;
    }

    public void setTrace_trace(trace_Trace trace_trace) {
        this.trace_trace = trace_trace;
    }
    public trace_ObjectState getTrace_objectstate() {
        return trace_objectstate;
    }

    public void setTrace_objectstate(trace_ObjectState trace_objectstate) {
        this.trace_objectstate = trace_objectstate;
    }

}