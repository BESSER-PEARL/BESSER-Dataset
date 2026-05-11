




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class trace_Log  {

    private String message;
    private String source;
    private LocalDate timestamp;
    private String level;





    private trace_Trace trace_trace;


    public trace_Log(
        String message,        String source,        LocalDate timestamp,        String level    ) {
        this.message = message;
        this.source = source;
        this.timestamp = timestamp;
        this.level = level;
    }


    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }
    public String getSource() {
        return source;
    }

    public void setSource(String source) {
        this.source = source;
    }
    public LocalDate getTimestamp() {
        return timestamp;
    }

    public void setTimestamp(LocalDate timestamp) {
        this.timestamp = timestamp;
    }
    public String getLevel() {
        return level;
    }

    public void setLevel(String level) {
        this.level = level;
    }

    public trace_Trace getTrace_trace() {
        return trace_trace;
    }

    public void setTrace_trace(trace_Trace trace_trace) {
        this.trace_trace = trace_trace;
    }

}