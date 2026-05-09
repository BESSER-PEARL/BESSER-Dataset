





import java.util.List;
import java.util.ArrayList;

public class trace_GenNodeTrace extends MatchingTrace {






    private trace_TraceModel trace_tracemodel;




    private List<trace_GenNodeLabelTrace> trace_gennodelabeltraces;


    public trace_GenNodeTrace(
    ) {
        super(
        );
        this.trace_gennodelabeltraces = new ArrayList<>();
    }

    public trace_GenNodeTrace(
        ArrayList<trace_GenNodeLabelTrace> trace_gennodelabeltraces    ) {
        this.trace_gennodelabeltraces = trace_gennodelabeltraces;
    }


    public trace_TraceModel getTrace_tracemodel() {
        return trace_tracemodel;
    }

    public void setTrace_tracemodel(trace_TraceModel trace_tracemodel) {
        this.trace_tracemodel = trace_tracemodel;
    }
    public List<trace_GenNodeLabelTrace> getTrace_gennodelabeltraces() {
        return trace_gennodelabeltraces;
    }

    public void addTrace_gennodelabeltrace(Trace_gennodelabeltrace trace_gennodelabeltrace) {
        this.trace_gennodelabeltraces.add(trace_gennodelabeltrace);
    }

}