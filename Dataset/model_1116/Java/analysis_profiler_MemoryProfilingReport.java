





import java.util.List;
import java.util.ArrayList;

public class analysis_profiler_MemoryProfilingReport extends AnalysisReport {

    private String networkName;



    public analysis_profiler_MemoryProfilingReport(
        String networkName    ) {
        super(
        );
        this.networkName = networkName;
    }


    public String getNetworkname() {
        return networkName;
    }

    public void setNetworkname(String networkName) {
        this.networkName = networkName;
    }


}