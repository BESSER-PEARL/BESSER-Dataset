





import java.util.List;
import java.util.ArrayList;

public class trace_TraceLink  {

    private String ruleName;





    private trace_Trace trace_trace;


    public trace_TraceLink(
        String ruleName    ) {
        this.ruleName = ruleName;
    }


    public String getRulename() {
        return ruleName;
    }

    public void setRulename(String ruleName) {
        this.ruleName = ruleName;
    }

    public trace_Trace getTrace_trace() {
        return trace_trace;
    }

    public void setTrace_trace(trace_Trace trace_trace) {
        this.trace_trace = trace_trace;
    }

}