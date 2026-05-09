





import java.util.List;
import java.util.ArrayList;

public class trace_ObjectAny extends Any {






    private List<trace_EObject> trace_eobjects;


    public trace_ObjectAny(
    ) {
        super(
        );
        this.trace_eobjects = new ArrayList<>();
    }

    public trace_ObjectAny(
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