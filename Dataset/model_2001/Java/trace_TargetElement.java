





import java.util.List;
import java.util.ArrayList;

public class trace_TargetElement extends TraceElement {






    private List<trace_SourceElement> trace_sourceelements;




    private trace_SourceElement trace_sourceelement;


    public trace_TargetElement(
    ) {
        super(
        );
        this.trace_sourceelements = new ArrayList<>();
    }

    public trace_TargetElement(
        ArrayList<trace_SourceElement> trace_sourceelements    ) {
        this.trace_sourceelements = trace_sourceelements;
    }


    public List<trace_SourceElement> getTrace_sourceelements() {
        return trace_sourceelements;
    }

    public void addTrace_sourceelement(Trace_sourceelement trace_sourceelement) {
        this.trace_sourceelements.add(trace_sourceelement);
    }
    public trace_SourceElement getTrace_sourceelement() {
        return trace_sourceelement;
    }

    public void setTrace_sourceelement(trace_SourceElement trace_sourceelement) {
        this.trace_sourceelement = trace_sourceelement;
    }

}