





import java.util.List;
import java.util.ArrayList;

public class trace_Event extends EModelElement {

    private String timestamp;





    private trace_Trace trace_trace;




    private trace_Trace trace_trace;




    private trace_Slice trace_slice;




    private List<trace_Slice> trace_slices;


    public trace_Event(
        String timestamp    ) {
        super(
        );
        this.timestamp = timestamp;
        this.trace_slices = new ArrayList<>();
    }

    public trace_Event(
        String timestamp        ArrayList<trace_Slice> trace_slices    ) {
        this.timestamp = timestamp;
        this.trace_slices = trace_slices;
    }

    public String getTimestamp() {
        return timestamp;
    }

    public void setTimestamp(String timestamp) {
        this.timestamp = timestamp;
    }

    public trace_Trace getTrace_trace() {
        return trace_trace;
    }

    public void setTrace_trace(trace_Trace trace_trace) {
        this.trace_trace = trace_trace;
    }
    public trace_Trace getTrace_trace() {
        return trace_trace;
    }

    public void setTrace_trace(trace_Trace trace_trace) {
        this.trace_trace = trace_trace;
    }
    public trace_Slice getTrace_slice() {
        return trace_slice;
    }

    public void setTrace_slice(trace_Slice trace_slice) {
        this.trace_slice = trace_slice;
    }
    public List<trace_Slice> getTrace_slices() {
        return trace_slices;
    }

    public void addTrace_slice(Trace_slice trace_slice) {
        this.trace_slices.add(trace_slice);
    }

}