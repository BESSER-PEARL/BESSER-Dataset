





import java.util.List;
import java.util.ArrayList;

public class trace_Step  {

    private String hidden;
    private String number;
    private String thread;





    private trace_Location trace_location;




    private trace_Trace trace_trace;


    public trace_Step(
        String hidden,        String number,        String thread    ) {
        this.hidden = hidden;
        this.number = number;
        this.thread = thread;
    }


    public String getHidden() {
        return hidden;
    }

    public void setHidden(String hidden) {
        this.hidden = hidden;
    }
    public String getNumber() {
        return number;
    }

    public void setNumber(String number) {
        this.number = number;
    }
    public String getThread() {
        return thread;
    }

    public void setThread(String thread) {
        this.thread = thread;
    }

    public trace_Location getTrace_location() {
        return trace_location;
    }

    public void setTrace_location(trace_Location trace_location) {
        this.trace_location = trace_location;
    }
    public trace_Trace getTrace_trace() {
        return trace_trace;
    }

    public void setTrace_trace(trace_Trace trace_trace) {
        this.trace_trace = trace_trace;
    }

}