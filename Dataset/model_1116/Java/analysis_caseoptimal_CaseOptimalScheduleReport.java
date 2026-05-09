





import java.util.List;
import java.util.ArrayList;

public class analysis_caseoptimal_CaseOptimalScheduleReport extends AnalysisReport {

    private String partitionFilePath;
    private String traceFile;
    private String pipeline;



    public analysis_caseoptimal_CaseOptimalScheduleReport(
        String partitionFilePath,        String traceFile,        String pipeline    ) {
        super(
        );
        this.partitionFilePath = partitionFilePath;
        this.traceFile = traceFile;
        this.pipeline = pipeline;
    }


    public String getPartitionfilepath() {
        return partitionFilePath;
    }

    public void setPartitionfilepath(String partitionFilePath) {
        this.partitionFilePath = partitionFilePath;
    }
    public String getTracefile() {
        return traceFile;
    }

    public void setTracefile(String traceFile) {
        this.traceFile = traceFile;
    }
    public String getPipeline() {
        return pipeline;
    }

    public void setPipeline(String pipeline) {
        this.pipeline = pipeline;
    }


}