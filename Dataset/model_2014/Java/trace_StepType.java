





import java.util.List;
import java.util.ArrayList;

public class trace_StepType  {

    private String stepName;





    private trace_Trace trace_trace;


    public trace_StepType(
        String stepName    ) {
        this.stepName = stepName;
    }


    public String getStepname() {
        return stepName;
    }

    public void setStepname(String stepName) {
        this.stepName = stepName;
    }

    public trace_Trace getTrace_trace() {
        return trace_trace;
    }

    public void setTrace_trace(trace_Trace trace_trace) {
        this.trace_trace = trace_trace;
    }

}