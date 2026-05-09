





import java.util.List;
import java.util.ArrayList;

public class trace_Trace  {






    private Events events;




    private TracedObjects tracedobjects;




    private trace_StaticObjectsPools trace_staticobjectspools;


    public trace_Trace(
    ) {
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
    public trace_StaticObjectsPools getTrace_staticobjectspools() {
        return trace_staticobjectspools;
    }

    public void setTrace_staticobjectspools(trace_StaticObjectsPools trace_staticobjectspools) {
        this.trace_staticobjectspools = trace_staticobjectspools;
    }

}