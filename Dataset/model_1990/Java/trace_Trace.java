





import java.util.List;
import java.util.ArrayList;

public class trace_Trace  {

    private String name;





    private List<trace_EObject> trace_eobjects;




    private trace_EObject trace_eobject;


    public trace_Trace(
        String name    ) {
        this.name = name;
        this.trace_eobjects = new ArrayList<>();
    }

    public trace_Trace(
        String name        ArrayList<trace_EObject> trace_eobjects    ) {
        this.name = name;
        this.trace_eobjects = trace_eobjects;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<trace_EObject> getTrace_eobjects() {
        return trace_eobjects;
    }

    public void addTrace_eobject(Trace_eobject trace_eobject) {
        this.trace_eobjects.add(trace_eobject);
    }
    public trace_EObject getTrace_eobject() {
        return trace_eobject;
    }

    public void setTrace_eobject(trace_EObject trace_eobject) {
        this.trace_eobject = trace_eobject;
    }

}