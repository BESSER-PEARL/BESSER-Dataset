





import java.util.List;
import java.util.ArrayList;

public class trace_TraceElement  {

    private int timestamp;
    private String event;





    private trace_Trace trace_trace;


    public trace_TraceElement(
        int timestamp,        String event    ) {
        this.timestamp = timestamp;
        this.event = event;
    }


    public int getTimestamp() {
        return timestamp;
    }

    public void setTimestamp(int timestamp) {
        this.timestamp = timestamp;
    }
    public String getEvent() {
        return event;
    }

    public void setEvent(String event) {
        this.event = event;
    }

    public trace_Trace getTrace_trace() {
        return trace_trace;
    }

    public void setTrace_trace(trace_Trace trace_trace) {
        this.trace_trace = trace_trace;
    }

}