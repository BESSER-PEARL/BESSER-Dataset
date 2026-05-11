





import java.util.List;
import java.util.ArrayList;

public class trace_TraceLink  {

    private boolean overridden;





    private List<trace_SourceElement> trace_sourceelements;




    private trace_TargetElement trace_targetelement;




    private trace_TracedRule trace_tracedrule;




    private trace_TracedRule trace_tracedrule;




    private trace_SourceElement trace_sourceelement;




    private List<trace_TargetElement> trace_targetelements;


    public trace_TraceLink(
        boolean overridden    ) {
        this.overridden = overridden;
        this.trace_sourceelements = new ArrayList<>();
        this.trace_targetelements = new ArrayList<>();
    }

    public trace_TraceLink(
        boolean overridden        ArrayList<trace_SourceElement> trace_sourceelements,        ArrayList<trace_TargetElement> trace_targetelements    ) {
        this.overridden = overridden;
        this.trace_sourceelements = trace_sourceelements;
        this.trace_targetelements = trace_targetelements;
    }

    public boolean getOverridden() {
        return overridden;
    }

    public void setOverridden(boolean overridden) {
        this.overridden = overridden;
    }

    public List<trace_SourceElement> getTrace_sourceelements() {
        return trace_sourceelements;
    }

    public void addTrace_sourceelement(Trace_sourceelement trace_sourceelement) {
        this.trace_sourceelements.add(trace_sourceelement);
    }
    public trace_TargetElement getTrace_targetelement() {
        return trace_targetelement;
    }

    public void setTrace_targetelement(trace_TargetElement trace_targetelement) {
        this.trace_targetelement = trace_targetelement;
    }
    public trace_TracedRule getTrace_tracedrule() {
        return trace_tracedrule;
    }

    public void setTrace_tracedrule(trace_TracedRule trace_tracedrule) {
        this.trace_tracedrule = trace_tracedrule;
    }
    public trace_TracedRule getTrace_tracedrule() {
        return trace_tracedrule;
    }

    public void setTrace_tracedrule(trace_TracedRule trace_tracedrule) {
        this.trace_tracedrule = trace_tracedrule;
    }
    public trace_SourceElement getTrace_sourceelement() {
        return trace_sourceelement;
    }

    public void setTrace_sourceelement(trace_SourceElement trace_sourceelement) {
        this.trace_sourceelement = trace_sourceelement;
    }
    public List<trace_TargetElement> getTrace_targetelements() {
        return trace_targetelements;
    }

    public void addTrace_targetelement(Trace_targetelement trace_targetelement) {
        this.trace_targetelements.add(trace_targetelement);
    }

}