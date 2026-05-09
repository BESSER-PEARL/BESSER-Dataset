





import java.util.List;
import java.util.ArrayList;

public class EtlSimpleTrace_TraceLink  {

    private String description;





    private EtlSimpleTrace_Trace etlsimpletrace_trace;


    public EtlSimpleTrace_TraceLink(
        String description    ) {
        this.description = description;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public EtlSimpleTrace_Trace getEtlsimpletrace_trace() {
        return etlsimpletrace_trace;
    }

    public void setEtlsimpletrace_trace(EtlSimpleTrace_Trace etlsimpletrace_trace) {
        this.etlsimpletrace_trace = etlsimpletrace_trace;
    }

}