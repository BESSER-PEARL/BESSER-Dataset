





import java.util.List;
import java.util.ArrayList;

public class analysis_trace_CompressedTraceReport extends AnalysisReport {

    private String traceFile;



    public analysis_trace_CompressedTraceReport(
        String traceFile    ) {
        super(
        );
        this.traceFile = traceFile;
    }


    public String getTracefile() {
        return traceFile;
    }

    public void setTracefile(String traceFile) {
        this.traceFile = traceFile;
    }


}