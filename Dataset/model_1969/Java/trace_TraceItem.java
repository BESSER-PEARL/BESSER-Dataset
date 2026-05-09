





import java.util.List;
import java.util.ArrayList;

public class trace_TraceItem  {

    private String kind;





    private trace_TraceBySource trace_tracebysource;


    public trace_TraceItem(
        String kind    ) {
        this.kind = kind;
    }


    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public trace_TraceBySource getTrace_tracebysource() {
        return trace_tracebysource;
    }

    public void setTrace_tracebysource(trace_TraceBySource trace_tracebysource) {
        this.trace_tracebysource = trace_tracebysource;
    }

}