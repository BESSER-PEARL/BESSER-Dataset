





import java.util.List;
import java.util.ArrayList;

public class trace_SourceElementList  {






    private trace_TracedRule trace_tracedrule;




    private trace_TraceLinkSet trace_tracelinkset;




    private List<trace_SourceElement> trace_sourceelements;




    private trace_TracedRule trace_tracedrule;




    private trace_TraceLinkSet trace_tracelinkset;


    public trace_SourceElementList(
    ) {
        this.trace_sourceelements = new ArrayList<>();
    }

    public trace_SourceElementList(
        ArrayList<trace_SourceElement> trace_sourceelements    ) {
        this.trace_sourceelements = trace_sourceelements;
    }


    public trace_TracedRule getTrace_tracedrule() {
        return trace_tracedrule;
    }

    public void setTrace_tracedrule(trace_TracedRule trace_tracedrule) {
        this.trace_tracedrule = trace_tracedrule;
    }
    public trace_TraceLinkSet getTrace_tracelinkset() {
        return trace_tracelinkset;
    }

    public void setTrace_tracelinkset(trace_TraceLinkSet trace_tracelinkset) {
        this.trace_tracelinkset = trace_tracelinkset;
    }
    public List<trace_SourceElement> getTrace_sourceelements() {
        return trace_sourceelements;
    }

    public void addTrace_sourceelement(Trace_sourceelement trace_sourceelement) {
        this.trace_sourceelements.add(trace_sourceelement);
    }
    public trace_TracedRule getTrace_tracedrule() {
        return trace_tracedrule;
    }

    public void setTrace_tracedrule(trace_TracedRule trace_tracedrule) {
        this.trace_tracedrule = trace_tracedrule;
    }
    public trace_TraceLinkSet getTrace_tracelinkset() {
        return trace_tracelinkset;
    }

    public void setTrace_tracelinkset(trace_TraceLinkSet trace_tracelinkset) {
        this.trace_tracelinkset = trace_tracelinkset;
    }

}