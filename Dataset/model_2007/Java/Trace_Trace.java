





import java.util.List;
import java.util.ArrayList;

public class Trace_Trace  {

    private String description;





    private List<Trace_TraceLink> trace_tracelinks;


    public Trace_Trace(
        String description    ) {
        this.description = description;
        this.trace_tracelinks = new ArrayList<>();
    }

    public Trace_Trace(
        String description        ArrayList<Trace_TraceLink> trace_tracelinks    ) {
        this.description = description;
        this.trace_tracelinks = trace_tracelinks;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public List<Trace_TraceLink> getTrace_tracelinks() {
        return trace_tracelinks;
    }

    public void addTrace_tracelink(Trace_tracelink trace_tracelink) {
        this.trace_tracelinks.add(trace_tracelink);
    }

}