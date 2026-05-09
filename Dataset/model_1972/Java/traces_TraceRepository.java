





import java.util.List;
import java.util.ArrayList;

public class traces_TraceRepository  {






    private List<traces_Trace> traces_traces;


    public traces_TraceRepository(
    ) {
        this.traces_traces = new ArrayList<>();
    }

    public traces_TraceRepository(
        ArrayList<traces_Trace> traces_traces    ) {
        this.traces_traces = traces_traces;
    }


    public List<traces_Trace> getTraces_traces() {
        return traces_traces;
    }

    public void addTraces_trace(Traces_trace traces_trace) {
        this.traces_traces.add(traces_trace);
    }

}