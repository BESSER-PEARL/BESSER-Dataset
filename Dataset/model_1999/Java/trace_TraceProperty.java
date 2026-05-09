





import java.util.List;
import java.util.ArrayList;

public class trace_TraceProperty  {

    private boolean resolved;
    private String propertyName;





    private trace_TargetElement trace_targetelement;




    private trace_TraceLink trace_tracelink;




    private trace_TraceLink trace_tracelink;


    public trace_TraceProperty(
        boolean resolved,        String propertyName    ) {
        this.resolved = resolved;
        this.propertyName = propertyName;
    }


    public boolean getResolved() {
        return resolved;
    }

    public void setResolved(boolean resolved) {
        this.resolved = resolved;
    }
    public String getPropertyname() {
        return propertyName;
    }

    public void setPropertyname(String propertyName) {
        this.propertyName = propertyName;
    }

    public trace_TargetElement getTrace_targetelement() {
        return trace_targetelement;
    }

    public void setTrace_targetelement(trace_TargetElement trace_targetelement) {
        this.trace_targetelement = trace_targetelement;
    }
    public trace_TraceLink getTrace_tracelink() {
        return trace_tracelink;
    }

    public void setTrace_tracelink(trace_TraceLink trace_tracelink) {
        this.trace_tracelink = trace_tracelink;
    }
    public trace_TraceLink getTrace_tracelink() {
        return trace_tracelink;
    }

    public void setTrace_tracelink(trace_TraceLink trace_tracelink) {
        this.trace_tracelink = trace_tracelink;
    }

}