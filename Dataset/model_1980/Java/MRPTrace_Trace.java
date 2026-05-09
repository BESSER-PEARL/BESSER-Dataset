





import java.util.List;
import java.util.ArrayList;

public class MRPTrace_Trace extends NamedElement {

    private String granularity;





    private MRPTrace_TraceModel mrptrace_tracemodel;


    public MRPTrace_Trace(
        String granularity    ) {
        super(
        );
        this.granularity = granularity;
    }


    public String getGranularity() {
        return granularity;
    }

    public void setGranularity(String granularity) {
        this.granularity = granularity;
    }

    public MRPTrace_TraceModel getMrptrace_tracemodel() {
        return mrptrace_tracemodel;
    }

    public void setMrptrace_tracemodel(MRPTrace_TraceModel mrptrace_tracemodel) {
        this.mrptrace_tracemodel = mrptrace_tracemodel;
    }

}