





import java.util.List;
import java.util.ArrayList;

public class trace_MappingOperationToTraceRecordMapEntry  {






    private trace_Trace trace_trace;




    private List<trace_TraceRecord> trace_tracerecords;


    public trace_MappingOperationToTraceRecordMapEntry(
    ) {
        this.trace_tracerecords = new ArrayList<>();
    }

    public trace_MappingOperationToTraceRecordMapEntry(
        ArrayList<trace_TraceRecord> trace_tracerecords    ) {
        this.trace_tracerecords = trace_tracerecords;
    }


    public trace_Trace getTrace_trace() {
        return trace_trace;
    }

    public void setTrace_trace(trace_Trace trace_trace) {
        this.trace_trace = trace_trace;
    }
    public List<trace_TraceRecord> getTrace_tracerecords() {
        return trace_tracerecords;
    }

    public void addTrace_tracerecord(Trace_tracerecord trace_tracerecord) {
        this.trace_tracerecords.add(trace_tracerecord);
    }

}