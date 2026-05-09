





import java.util.List;
import java.util.ArrayList;

public class trace_OutputFile  {

    private String outlet;
    private String fileName;





    private trace_Trace trace_trace;


    public trace_OutputFile(
        String outlet,        String fileName    ) {
        this.outlet = outlet;
        this.fileName = fileName;
    }


    public String getOutlet() {
        return outlet;
    }

    public void setOutlet(String outlet) {
        this.outlet = outlet;
    }
    public String getFilename() {
        return fileName;
    }

    public void setFilename(String fileName) {
        this.fileName = fileName;
    }

    public trace_Trace getTrace_trace() {
        return trace_trace;
    }

    public void setTrace_trace(trace_Trace trace_trace) {
        this.trace_trace = trace_trace;
    }

}