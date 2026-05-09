





import java.util.List;
import java.util.ArrayList;

public class trace_M2MTraceItem extends TraceItem {






    private List<trace_EObject> trace_eobjects;


    public trace_M2MTraceItem(
    ) {
        super(
        );
        this.trace_eobjects = new ArrayList<>();
    }

    public trace_M2MTraceItem(
        ArrayList<trace_EObject> trace_eobjects    ) {
        this.trace_eobjects = trace_eobjects;
    }


    public List<trace_EObject> getTrace_eobjects() {
        return trace_eobjects;
    }

    public void addTrace_eobject(Trace_eobject trace_eobject) {
        this.trace_eobjects.add(trace_eobject);
    }

}