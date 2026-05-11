





import java.util.List;
import java.util.ArrayList;

public class trace_Trace  {






    private trace_StaticObjectsPools trace_staticobjectspools;




    private List<trace_GlobalState> trace_globalstates;




    private Events events;




    private TracedObjects tracedobjects;


    public trace_Trace(
    ) {
        this.trace_globalstates = new ArrayList<>();
    }

    public trace_Trace(
        ArrayList<trace_GlobalState> trace_globalstates    ) {
        this.trace_globalstates = trace_globalstates;
    }


    public trace_StaticObjectsPools getTrace_staticobjectspools() {
        return trace_staticobjectspools;
    }

    public void setTrace_staticobjectspools(trace_StaticObjectsPools trace_staticobjectspools) {
        this.trace_staticobjectspools = trace_staticobjectspools;
    }
    public List<trace_GlobalState> getTrace_globalstates() {
        return trace_globalstates;
    }

    public void addTrace_globalstate(Trace_globalstate trace_globalstate) {
        this.trace_globalstates.add(trace_globalstate);
    }
    public Events getEvents() {
        return events;
    }

    public void setEvents(Events events) {
        this.events = events;
    }
    public TracedObjects getTracedobjects() {
        return tracedobjects;
    }

    public void setTracedobjects(TracedObjects tracedobjects) {
        this.tracedobjects = tracedobjects;
    }

}