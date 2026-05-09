





import java.util.List;
import java.util.ArrayList;

public class trace_TraceList  {






    private List<trace_TraceItem> trace_traceitems;




    private trace_Trace trace_trace;


    public trace_TraceList(
    ) {
        this.trace_traceitems = new ArrayList<>();
    }

    public trace_TraceList(
        ArrayList<trace_TraceItem> trace_traceitems    ) {
        this.trace_traceitems = trace_traceitems;
    }


    public List<trace_TraceItem> getTrace_traceitems() {
        return trace_traceitems;
    }

    public void addTrace_traceitem(Trace_traceitem trace_traceitem) {
        this.trace_traceitems.add(trace_traceitem);
    }
    public trace_Trace getTrace_trace() {
        return trace_trace;
    }

    public void setTrace_trace(trace_Trace trace_trace) {
        this.trace_trace = trace_trace;
    }

}