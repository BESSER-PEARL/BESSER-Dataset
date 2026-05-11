





import java.util.List;
import java.util.ArrayList;

public class trace_ObjectValueChangeEvent extends ValueChangeEvent {






    private trace_EObject trace_eobject;


    public trace_ObjectValueChangeEvent(
    ) {
        super(
        );
    }



    public trace_EObject getTrace_eobject() {
        return trace_eobject;
    }

    public void setTrace_eobject(trace_EObject trace_eobject) {
        this.trace_eobject = trace_eobject;
    }

}