





import java.util.List;
import java.util.ArrayList;

public class trace_Trace  {

    private String name;





    private List<trace_Trace> trace_traces;


    public trace_Trace(
        String name    ) {
        this.name = name;
        this.trace_traces = new ArrayList<>();
    }

    public trace_Trace(
        String name        ArrayList<trace_Trace> trace_traces    ) {
        this.name = name;
        this.trace_traces = trace_traces;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<trace_Trace> getTrace_traces() {
        return trace_traces;
    }

    public void addTrace_trace(Trace_trace trace_trace) {
        this.trace_traces.add(trace_trace);
    }

}