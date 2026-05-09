





import java.util.List;
import java.util.ArrayList;

public class traces_TraceElement  {

    private String typeName;
    private String traceType;
    private String value;





    private traces_Trace traces_trace;


    public traces_TraceElement(
        String typeName,        String traceType,        String value    ) {
        this.typeName = typeName;
        this.traceType = traceType;
        this.value = value;
    }


    public String getTypename() {
        return typeName;
    }

    public void setTypename(String typeName) {
        this.typeName = typeName;
    }
    public String getTracetype() {
        return traceType;
    }

    public void setTracetype(String traceType) {
        this.traceType = traceType;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public traces_Trace getTraces_trace() {
        return traces_trace;
    }

    public void setTraces_trace(traces_Trace traces_trace) {
        this.traces_trace = traces_trace;
    }

}