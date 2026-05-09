





import java.util.List;
import java.util.ArrayList;

public class trace_ReferenceMapping  {

    private String type;





    private trace_EReference trace_ereference;




    private trace_EStructuralFeature trace_estructuralfeature;




    private trace_Trace trace_trace;


    public trace_ReferenceMapping(
        String type    ) {
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public trace_EReference getTrace_ereference() {
        return trace_ereference;
    }

    public void setTrace_ereference(trace_EReference trace_ereference) {
        this.trace_ereference = trace_ereference;
    }
    public trace_EStructuralFeature getTrace_estructuralfeature() {
        return trace_estructuralfeature;
    }

    public void setTrace_estructuralfeature(trace_EStructuralFeature trace_estructuralfeature) {
        this.trace_estructuralfeature = trace_estructuralfeature;
    }
    public trace_Trace getTrace_trace() {
        return trace_trace;
    }

    public void setTrace_trace(trace_Trace trace_trace) {
        this.trace_trace = trace_trace;
    }

}