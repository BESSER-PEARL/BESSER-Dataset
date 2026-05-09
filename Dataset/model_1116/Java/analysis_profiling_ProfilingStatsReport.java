





import java.util.List;
import java.util.ArrayList;

public class analysis_profiling_ProfilingStatsReport extends AnalysisReport {

    private String networkName;



    public analysis_profiling_ProfilingStatsReport(
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