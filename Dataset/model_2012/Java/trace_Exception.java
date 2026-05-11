





import java.util.List;
import java.util.ArrayList;

public class trace_Exception  {

    private String message;





    private trace_Log trace_log;


    public trace_Exception(
        String message    ) {
        this.message = message;
    }


    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }

    public trace_Log getTrace_log() {
        return trace_log;
    }

    public void setTrace_log(trace_Log trace_log) {
        this.trace_log = trace_log;
    }

}