





import java.util.List;
import java.util.ArrayList;

public class trace_SourceElement extends TraceElement {

    private boolean mapsToSelf;





    private trace_TraceLinkSet trace_tracelinkset;




    private trace_TraceLinkSet trace_tracelinkset;




    private List<trace_TargetElement> trace_targetelements;




    private trace_TracedRule trace_tracedrule;




    private trace_TracedRule trace_tracedrule;




    private trace_TargetElement trace_targetelement;


    public trace_SourceElement(
        boolean mapsToSelf    ) {
        super(
        );
        this.mapsToSelf = mapsToSelf;
        this.trace_targetelements = new ArrayList<>();
    }

    public trace_SourceElement(
        boolean mapsToSelf        ArrayList<trace_TargetElement> trace_targetelements    ) {
        this.mapsToSelf = mapsToSelf;
        this.trace_targetelements = trace_targetelements;
    }

    public boolean getMapstoself() {
        return mapsToSelf;
    }

    public void setMapstoself(boolean mapsToSelf) {
        this.mapsToSelf = mapsToSelf;
    }

    public trace_TraceLinkSet getTrace_tracelinkset() {
        return trace_tracelinkset;
    }

    public void setTrace_tracelinkset(trace_TraceLinkSet trace_tracelinkset) {
        this.trace_tracelinkset = trace_tracelinkset;
    }
    public trace_TraceLinkSet getTrace_tracelinkset() {
        return trace_tracelinkset;
    }

    public void setTrace_tracelinkset(trace_TraceLinkSet trace_tracelinkset) {
        this.trace_tracelinkset = trace_tracelinkset;
    }
    public List<trace_TargetElement> getTrace_targetelements() {
        return trace_targetelements;
    }

    public void addTrace_targetelement(Trace_targetelement trace_targetelement) {
        this.trace_targetelements.add(trace_targetelement);
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
    public trace_TargetElement getTrace_targetelement() {
        return trace_targetelement;
    }

    public void setTrace_targetelement(trace_TargetElement trace_targetelement) {
        this.trace_targetelement = trace_targetelement;
    }

}