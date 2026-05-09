





import java.util.List;
import java.util.ArrayList;

public class SimpleTrace_TraceLink  {

    private String description;





    private SimpleTrace_Trace simpletrace_trace;


    public SimpleTrace_TraceLink(
        String description    ) {
        this.description = description;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public SimpleTrace_Trace getSimpletrace_trace() {
        return simpletrace_trace;
    }

    public void setSimpletrace_trace(SimpleTrace_Trace simpletrace_trace) {
        this.simpletrace_trace = simpletrace_trace;
    }

}