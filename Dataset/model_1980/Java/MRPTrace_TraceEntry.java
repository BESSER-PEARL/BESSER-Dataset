





import java.util.List;
import java.util.ArrayList;

public class MRPTrace_TraceEntry  {

    private String description;





    private MRPTrace_TraceEntry mrptrace_traceentry;




    private MRPTrace_Event mrptrace_event;




    private MRPTrace_Trace mrptrace_trace;


    public MRPTrace_TraceEntry(
        String description    ) {
        this.description = description;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public MRPTrace_TraceEntry getMrptrace_traceentry() {
        return mrptrace_traceentry;
    }

    public void setMrptrace_traceentry(MRPTrace_TraceEntry mrptrace_traceentry) {
        this.mrptrace_traceentry = mrptrace_traceentry;
    }
    public MRPTrace_Event getMrptrace_event() {
        return mrptrace_event;
    }

    public void setMrptrace_event(MRPTrace_Event mrptrace_event) {
        this.mrptrace_event = mrptrace_event;
    }
    public MRPTrace_Trace getMrptrace_trace() {
        return mrptrace_trace;
    }

    public void setMrptrace_trace(MRPTrace_Trace mrptrace_trace) {
        this.mrptrace_trace = mrptrace_trace;
    }

}