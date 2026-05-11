




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class trace_Log  {

    private String level;
    private String source;
    private LocalDate timestamp;
    private String message;





    private trace_Trace trace_trace;


    public trace_Log(
        String level,        String source,        LocalDate timestamp,        String message    ) {
        this.level = level;
        this.source = source;
        this.timestamp = timestamp;
        this.message = message;
    }


    public String getLevel() {
        return level;
    }

    public void setLevel(String level) {
        this.level = level;
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
    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }

    public trace_Trace getTrace_trace() {
        return trace_trace;
    }

    public void setTrace_trace(trace_Trace trace_trace) {
        this.trace_trace = trace_trace;
    }

}