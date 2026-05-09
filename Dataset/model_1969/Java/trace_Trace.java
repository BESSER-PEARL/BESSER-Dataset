





import java.util.List;
import java.util.ArrayList;

public class trace_Trace  {






    private List<trace_TraceBySource> trace_tracebysources;


    public trace_Trace(
    ) {
        this.trace_tracebysources = new ArrayList<>();
    }

    public trace_Trace(
        ArrayList<trace_TraceBySource> trace_tracebysources    ) {
        this.trace_tracebysources = trace_tracebysources;
    }


    public List<trace_TraceBySource> getTrace_tracebysources() {
        return trace_tracebysources;
    }

    public void addTrace_tracebysource(Trace_tracebysource trace_tracebysource) {
        this.trace_tracebysources.add(trace_tracebysource);
    }

}