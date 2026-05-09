





import java.util.List;
import java.util.ArrayList;

public class analysis_trace_TraceSizeReport extends AnalysisReport {

    private String firings;
    private String dependencies;



    public analysis_trace_TraceSizeReport(
        String firings,        String dependencies    ) {
        super(
        );
        this.firings = firings;
        this.dependencies = dependencies;
    }


    public String getFirings() {
        return firings;
    }

    public void setFirings(String firings) {
        this.firings = firings;
    }
    public String getDependencies() {
        return dependencies;
    }

    public void setDependencies(String dependencies) {
        this.dependencies = dependencies;
    }


}